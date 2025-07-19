import streamlit as st
import emoji # type: ignore
from dotenv import load_dotenv # type: ignore
from PyPDF2 import PdfReader # type: ignore
from langchain.text_splitter import CharacterTextSplitter # type: ignore
from langchain_community.embeddings import OpenAIEmbeddings # type: ignore
from langchain_community.vectorstores import FAISS # type: ignore

def get_pdf_text(pdf_files):
    text = ""
    for pdf in pdf_files:
        pdf_reader = PdfReader(pdf)
        for i, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += page_text
            else:
                st.warning(emoji.emojize(f":warning: Page {i+1} in '{pdf.name}' has no extractable text (possibily scanned"))
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200, 
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embadding = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(text_chunks, embadding)
    return vectorstore

def main():
    load_dotenv()  # Load environment variables from .env file
    
    st.set_page_config(page_title="AskMyPDF", page_icon=emoji.emojize(":receipt:"), layout="wide", initial_sidebar_state="expanded")

    st.title(emoji.emojize(":receipt: AskMyPDF"))
    st.header("Extract Information from Given PDFs")
    st.text_input(emoji.emojize(":speech_balloon: What would you like to know from your documents?"), key="user_input")

    with st.sidebar:
        st.subheader(emoji.emojize(":inbox_tray: Upload PDFs"))
        pdf_files = st.file_uploader(
            emoji.emojize("Upload your PDFs here and click the button to start analysis :arrow_down:"),
            type=["pdf"],
            accept_multiple_files=True,
            key="pdf_uploader"
        )

        if st.button(emoji.emojize(":mag: Analyze PDFs"), key="process_button"):
            if pdf_files:
                st.success(emoji.emojize(f":white_check_mark: {len(pdf_files)} PDF{' was' if len(pdf_files) == 1 else 's were'} successfully uploaded and ready for analysis."))
                with st.spinner("Extracting text and preparing for analysis..."):
                    # get pdf text
                    raw_text = get_pdf_text(pdf_files)
                    st.write(raw_text)

                #get the text chunks
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)
            
                #create vector store
                vectorstore = get_vector_store(text_chunks)


            else:
                st.warning(emoji.emojize(":warning: Please upload at least one PDF before information extraction."))

if __name__ == "__main__":
    main()
