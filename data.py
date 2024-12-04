import os
import sys

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma


from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI')

llm = ChatOpenAI(model="gpt-4o-mini")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="docs",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)


# load, split, and store documents
def load_doc(file_path: str, ext: str):
    # load document
    if ext == "txt":
        loader = TextLoader(file_path)
    elif ext == "pdf":
        loader = PyPDFLoader(file_path)
    docs = loader.load()
    # print(f"Doc metadata: {docs[0].metadata}")

    # split document
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # chunk size (characters)
        chunk_overlap=200,  # chunk overlap (characters)
        add_start_index=True,  # track index in original document
    )
    splits = splitter.split_documents(docs)
    # print(f"# of splits in document {file_path}: {len(splits)}")

    # store splits
    document_ids = vector_store.add_documents(documents=splits)
    # print(f"First 3 document ids: {document_ids[:3]}")


def load_all_docs(dir_path: str):
    uploaded = []
    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"): 
            load_doc(dir_path + "/" + filename, "txt")
            uploaded.append(filename)
        elif filename.endswith(".pdf"):
            load_doc(dir_path + "/" + filename, "pdf")
            uploaded.append(filename)
        else:
            print(f"{filename} is not an acceptable file")

    # print(f"Successfully loaded the following files: {uploaded}")
    return vector_store



def main(path):
    load_all_docs(path)


if __name__ == '__main__':
    main(sys.argv[1])











