import os
import pinecone
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains.question_answering import load_qa_chain

load_dotenv()

def load_docs():
  directory = './resources'
  loader = DirectoryLoader(directory)
  docs = loader.load()
  return docs

def split_docs(docs, chunk_size=1000, chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  splitter_docs = text_splitter.split_documents(docs)
  return splitter_docs

def get_similiar_docs(query, index, k=2, score=False):
  if score:
    similar_docs = index.similarity_search_with_score(query, k=k)
  else:
    similar_docs = index.similarity_search(query, k=k)
  return similar_docs

docs = split_docs(load_docs())
print(len(docs))
embeddings = OpenAIEmbeddings(model='gpt-3.5-turbo', openai_api_key=os.getenv('OPENAI_API_KEY'))
query_result = embeddings.embed_query('Hello World')
len(query_result)
pinecone.init(
  api_key=os.getenv('PINECONE_API_KEY'),
  environment=os.getenv('PINECONE_API_ENV'),)
index_name = 'langchain1'
index = Pinecone.from_documents(documents=docs, embedding=embeddings, index_name=index_name)

query = 'What is Diabetes?'
docs = index.similarity_search(query)
print(docs[0].page_content)