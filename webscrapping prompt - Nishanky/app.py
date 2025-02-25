from flask import Flask, request, jsonify, render_template
import requests 
from bs4 import BeautifulSoup
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage
from urllib.parse import urlparse


app = Flask(__name__)

def scrape_text_from_url(url):
    try:  
        response = requests.get(url) 
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')

        # text_content = soup.get_text(separator='\n', strip=True)  # Separate text by newlines
        # images = [ "\n" + img['src'] + "\n" for img in soup.find_all('img') if 'src' in img.attrs]

        # List of excluded root domains
        excluded_domains = [
            "www.socialnews.xyz",
            "www.facebook.com",
            "sb.scorecardresearch.com"
        ]
        images = []
        for img in soup.find_all('img'):
            if 'src' in img.attrs:
                img_src = img['src']
                # Parse the image URL to get the root domain
                parsed_url = urlparse(img_src)
                domain = parsed_url.netloc  # Extract the domain (e.g., "www.facebook.com")

                # Check if the domain is in the excluded list
                if domain not in excluded_domains:
                    images.append("\n" + img_src + "\n")


        # return text_content
        return images
    except Exception as e:
        return f"Error scraping the URL: {e}"



def query_openai(text_content, query):
    try:
        messages = [
        HumanMessage(content= f"based on given content= {text_content}, answer given query = {query}"),
        ]
        gateway_base_url = "https://5c43bfvqiq.us-east-2.awsapprunner.com"
        gateway_api_key = "sk-1a80c7c1638344e5a850c4"
        model = "anthropic.claude-v3.5-sonnet-AI_Team"
        
        llm = ChatOpenAI(
        model_name=model,
        temperature=0.1,
        max_tokens=4096,
        openai_api_base=gateway_base_url, # openai_api_base represents the endpoint the Langchain object will make a call to when invoked
        openai_api_key=gateway_api_key,
        )
        return llm.invoke(messages).content
    except Exception as e:
        return f"Error form OpenAI: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    # Render the HTML form on GET request
    if request.method == 'GET':
        return render_template('index.html')

 
    # Process data on POST request
    elif request.method == 'POST':

        data = request.get_json()    
        url = data.get('url')
        query = data.get('query')

        # Process the data (this is just an example)
        text_content = scrape_text_from_url(url)

        # content_from_openai = query_openai(text_content, query)

        result = {
            # "message": content_from_openai
            "message": text_content
        } 
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)