import os
import sys
import API_Key

os.environ["OPENAI_API_KEY"] = API_Key.apikey
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

embeddings = HuggingFaceEmbeddings()
# embeddings = OpenAIEmbeddings()

persist_directory = "Chatbot1"

if os.path.exists("Chatbot1"):
    # reuse
    print("Activating Chatbot1...")
    vectorstore = Chroma(embedding_function=embeddings, persist_directory=persist_directory)
else:
    '''Read file and divide into chunks'''
    from langchain.document_loaders import TextLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    print("Initialising Chatbot1...")
    raw_documents = TextLoader("Settings/Chatbot1.txt").load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
    documents = text_splitter.split_documents(raw_documents)
    # print(f"Now you have {len(documents)} documents")
    # print(documents[0])

    vectorstore = Chroma.from_documents(documents=documents,embedding=embeddings, persist_directory=persist_directory)
    vectorstore.persist()

# Check with similarity_search
# docs = vectorstore.similarity_search("What is this doc about?",k=3)
# for content in docs:
#         print(f"{content.page_content}\n")


'''Agent'''
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain import HuggingFaceHub

# llm=ChatOpenAI(model="gpt-3.5-turbo")#, temperature=1.0, max_tokens=150)
llm=HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())


'''Main Reply Function'''
def reply(line, chat_history):
    reply = chain({"question": line, "chat_history": chat_history})
    chat_history.append((line, reply["answer"]))
    return reply["answer"]


'''
def line_generation():
    Step_plan_prompt = Prompts.Objective
    Obstacles_prompt = Prompts.Obstacle
    Action_prompt = Prompts.Action
    Line_prompt = 
    Reflextion_prompt = 

    chain_of_thought = get_gpt_response(Step_plan_prompt)
    person["memory"] = person["memory"] + chain_of_thought
        
    chain_of_thought = get_gpt_response(Obstacles_prompt)
    person["memory"] = person["memory"] + chain_of_thought

    chain_of_thought = get_gpt_response(Action_prompt)
    person["memory"] = person["memory"] + chain_of_thought

    line = get_gpt_response(Line_prompt)
    person["memory"] = person["memory"] + line

    Reflextion = get_gpt_response(Reflextion_prompt)
    person["memory"] = Reflextion

    return line
'''
