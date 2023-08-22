import os
import API_Key
import Prompts
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = API_Key.apikey

class ChatBot:
    def __init__(self, name: str):
        # create memeory
        persist_directory = name + "'s Memory"

        # embedding
        embeddings = OpenAIEmbeddings() # text-embedding-ada-002 

        if os.path.exists(persist_directory):
            # reuse
            print(f"Activating {name}...")
        else:
            # Read file and divide into chunks
            print(f"Initialising {name}...")
            raw_documents = TextLoader(f"Settings/{name}.txt").load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
            documents = text_splitter.split_documents(raw_documents)
            # print(f"Now you have {len(documents)} documents")
            # print(documents[0])

            # Create vector database
            self.vectorstore = Chroma.from_documents(documents=documents,embedding=embeddings, persist_directory=persist_directory)
        
        # Point to vector database 
        self.vectorstore = Chroma(embedding_function=embeddings, persist_directory=persist_directory)

        # Check with similarity_search
        # docs = vectorstore.similarity_search("What is this doc about?",k=3)
        # for content in docs:
        #         print(f"{content.page_content}\n")

        # Chat model and Chain
        llm=ChatOpenAI(model="gpt-4")
        self.chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=self.vectorstore.as_retriever(search_kwargs={"k": 4}))
        self.thought = ""


    # Main Reply Function
    def reply(self, main, target, chat, last_line):
        
        # s = self.vectorstore.similarity_search(query = Prompts.objective)
        # for i in range(4):
        #     print(s[i],"\n")
        
        query = Prompts.objective.format(thought = self. thought, main = main, chat = chat, target = target, line = last_line)
        objective = self.chain({"chat_history": [],"question": query})
        # print("\n\n\nObjective Input:\n",objective)
        print("\nObjective OutPut:\n",objective["answer"])

        query = Prompts.line.format(objective = objective["answer"], chat = chat, target = target, line = last_line)
        line = self.chain({"chat_history": [],"question": query})
        # print("\n\n\nLine Input:\n",line)
        print("\nline OutPut:\n",line["answer"])

        query = Prompts.reflection.format(objective = objective["answer"])
        reflection = self.chain({"chat_history": [],"question": query})
        # print("\n\n\nReflection Input:\n",reflection)
        # print("\nReflection OutPut:\n",reflection["answer"])
        self.thought = reflection["answer"]


        return line["answer"]