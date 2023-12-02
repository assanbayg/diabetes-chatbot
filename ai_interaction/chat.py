import os
import pinecone
from dotenv import load_dotenv
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA
from langchain.agents import Tool, initialize_agent
from langchain.tools.google_scholar import GoogleScholarQueryRun
from langchain.utilities.google_scholar import GoogleScholarAPIWrapper

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_api_env = os.getenv("PINECONE_API_ENV")
serp_api_key = os.getenv("SERP_API_KEY")

model_name = "text-embedding-ada-002"
index_name = "dselect"

pinecone.init(api_key=pinecone_api_key, environment=pinecone_api_env)

embeddings = OpenAIEmbeddings(model=model_name, openai_api_key=openai_api_key)
index = pinecone.Index(index_name)
vectorstore = Pinecone(
    index,
    embeddings.embed_query,
    "text",
)


llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    model_name="gpt-3.5-turbo",
    temperature=0.0,
)

conversational_memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k=3,
    return_messages=True,
)


qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever()
)

google_scholar = GoogleScholarQueryRun(api_wrapper=GoogleScholarAPIWrapper())

tools = [
    Tool(
        name="Knowledge Base",
        func=qa.run,
        description=(
            "use this tool when answering general knowledge queries to get "
            "more information about the topic"
        ),
    ),
    Tool(
        name="Google Scholar",
        func=google_scholar.run,
        description="Search Google Scholar for research papers and summarise the research in first five papers highlighting the papers.",
    ),
]

agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    early_stopping_method="generate",
    memory=conversational_memory,
)

# Usage example
query = "What should I do when my blood sugar is high even I did't eat anything"
response = agent(query)["output"]
print("Agent Response:", response)