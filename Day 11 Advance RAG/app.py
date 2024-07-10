from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import os
import json
import fastapi
import requests
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv
import streamlit as st

from langserve import add_routes
import uvicorn

app=fastapi(
    title="Practice LLM AND API",
    version="1.0",
    description="server side application"
)

add_routes(
    app,
    Ollama,
    path="/ollamalogs"
)
model = Ollama("codellama:7b")

prompt = ChatPromptTemplate.from_template(" Give me question to solve? {} so that I provide solution")

add_routes(
    app,
    model,
    path="/codellama"
)

if __name__ == "__main__":
    uvicorn.run(app,host= "localhost",port=8000)


