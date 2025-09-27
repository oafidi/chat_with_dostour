from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import pypdf
import os

load_dotenv()
def load_constitution(pdf_path="documents/Constitution_Marocain_2011.pdf"):
    reader = pypdf.PdfReader(pdf_path)
    docs = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            docs.append(Document(page_content=text, metadata={"page": i+1}))
    return docs

def build_chain(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectordb = FAISS.from_documents(chunks, embeddings)
    retriever = vectordb.as_retriever()

    llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)

if __name__ == "__main__":
    print("Chatbot Constitution Marocaine (2011)")
    print("Posez vos questions (écrivez 'exit' pour quitter)\n")

    docs = load_constitution()
    qa_chain = build_chain(docs)
    chat_history = []

    while True:
        question = input("Vous: ")
        if question.lower() in ["exit", "quit", "q"]:
            print("Au revoir!")
            break

        result = qa_chain({"question": question, "chat_history": chat_history})
        answer = result["answer"]

        print("Bot:", answer, "\n")
        chat_history.append((question, answer))
