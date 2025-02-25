
        for _, row in df.iterrows():
            sentence = ', '.join([f"{col}: {row[col]}" for col in df.columns])
            table_data.append(sentence)


    return {
        'text_data': text_data,
        'table_data': table_data
    }



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
            "message": "sqwdaefrgt"
        } 
        print(text_content)
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)