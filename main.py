from flask import Flask, request, jsonify
import os
import pinecone
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import asyncio
import aiohttp

load_dotenv()

app = Flask(__name__)

def load_docs():
    directory = './resources'
    loader = DirectoryLoader(directory)
    docs = loader.load()
    return docs

def split_docs(docs, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    splitter_docs = text_splitter.split_documents(docs)
    return splitter_docs

docs = split_docs(load_docs())
embeddings = OpenAIEmbeddings(model='gpt-3.5-turbo', openai_api_key=os.getenv('OPENAI_API_KEY'))
pinecone.init(
    api_key=os.getenv('PINECONE_API_KEY'),
    environment=os.getenv('PINECONE_API_ENV'),
)
index_name = 'langchain1'
index = Pinecone.from_documents(documents=docs, embedding=embeddings, index_name=index_name)

async def perform_similarity_search(query):
    async with aiohttp.ClientSession() as session:
        result = await index.similarity_search(query, session=session)
    return result

@app.route('/query', methods=['GET'])
async def handle_query():
    query = request.args.get('query')
    
    if query:
        result = await perform_similarity_search(query)
        
        if result:
            first_result = result[0]
            return jsonify({"result": first_result.page_content})
        else:
            return jsonify({"error": "No results found"})
    else:
        return jsonify({"error": "No query provided"})

if __name__ == '__main__':
    app.run(debug=True)
