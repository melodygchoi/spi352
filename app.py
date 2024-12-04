import os
import sys
import data

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv

PATH = "docs"

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI')

llm = ChatOpenAI(model="gpt-4o-mini")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = InMemoryVectorStore(embeddings)

prompt = hub.pull("rlm/rag-prompt")
chain = create_stuff_documents_chain(llm, prompt)


def run():
    print("Loading documents...")
    vector_store = data.load_all_docs(PATH)
    print("------------------------------------------------")
    print("\nWelcome to Biometric Privacy Laws Chatbot \nCreated by Melody Choi and Natalia Eichmann for SPI 352")
    print("\n(q + Enter to quit)\n")
    

    run = True
    while run:
        print("------------------------\n")
        query = input("QUESTION:\n")
        if query == "q":
            run = False
        else:
            print("")
            # retrieve from database using similarity search
            contexts = vector_store.similarity_search(query)
            sources = [d.metadata["source"] for d in contexts]

            # feed contexts + prompt + query into llm
            msg = chain.invoke({"question": query, "context": contexts})
            print(f"ANSWER:\n{msg}")
            print(f"\n(Sources: {sources})")
            # print(f"\nContexts: {contexts}")


def main():
    run()

if __name__ == "__main__":
    main()
