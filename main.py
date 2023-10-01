import os
import json
import pinecone
from dotenv import load_dotenv
from flask import Flask, request
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

load_dotenv()

INDEX_NAME = 'langchain1'
app = Flask(__name__)

@app.route('/query', methods=['POST'])
def hello_world():
    data = request.json
    print(type(data))
    query = data['query']
    result = perform_similarity_search(query)
    print(result)
    return json.dumps({'result': result}), 200

def access_existing_index():
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))
    index = Pinecone.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)
    return index

def perform_similarity_search(query):
    index = access_existing_index()
    result = index.similarity_search(query)
    print('found')
    return result[0].page_content

pinecone.init(
    api_key=os.getenv('PINECONE_API_KEY'),
    environment=os.getenv('PINECONE_API_ENV'),
)

if __name__ == '__main__':
    app.run()