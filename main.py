from dotenv import load_dotenv
import os
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

load_dotenv()

loader = UnstructuredPDFLoader('./resources/impovement_diabetes_kz.pdf')
data = loader.load()
# print(len(data))

# embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))
# pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_API_ENV'))