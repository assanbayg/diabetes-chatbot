import os
import pinecone
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

load_dotenv()

INDEX_NAME = "langchain1"


def load_docs():
    directory = "./resources"
    loader = DirectoryLoader(directory)
    docs = loader.load()
    print("loaded")
    return docs


def split_docs(docs, chunk_size=500, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    splitter_docs = text_splitter.split_documents(docs)
    print("splitted")
    return splitter_docs


def create_index():
    docs = split_docs(load_docs())
    embeddings = OpenAIEmbeddings(
        model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    index = Pinecone.from_documents(
        documents=docs, embedding=embeddings, index_name=INDEX_NAME
    )
    return index


def access_existing_index():
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    index = Pinecone.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)
    return index


def perform_similarity_search(query):
    index = access_existing_index()
    result = index.similarity_search(query)
    print("found")
    return result


pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_API_ENV"),
)

create_index()
query = "Describe diet for type 1 diabetes"
result = perform_similarity_search(query)
if result:
    print(result[0].page_content)
else:
    print("No result")
