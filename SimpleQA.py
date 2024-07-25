from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.groq import Groq
from llama_index.embeddings.voyageai import VoyageEmbedding
import os
from llama_index.core import (
    Settings,
)  # Defaults are set to OpenAI, this is to change that

# Groq and Voyage AI
Groq_key = os.environ.get("GROQ_KEY")
voyage_key = os.environ.get("VOYAGE_KEY")
llm = Groq(model="llama3-8b-8192", api_key=Groq_key)
embed_model = VoyageEmbedding(model_name="voyage-2", voyage_api_key=voyage_key)

# every time we invoke embeddings it is create embeddings
Settings.embed_model = embed_model

# Chucking (Nodes) the data
reader = SimpleDirectoryReader(input_files=["Sri Lanka.pdf"])
docs = reader.load_data()
print(f"Loaded {len(docs)} docs")
print(docs[0])

# This index is created local memory
index = VectorStoreIndex.from_documents(docs)

# Simple Query engine for created vector store index
query_engine = index.as_query_engine(llm=llm)
response = query_engine.query("What is the capital of Sri Lanka?")
print(response)
