import streamlit as st

def main():
    st.set_page_config(page_title="Chat with me!", page_icon=":books:", layout="wide")
    st.header("Get information from multiple PDF sources") 
    st.text_input("Ask your question about your documents", key="user_input")

    with st.sidebar:
        st.subheader("About")
        st.write("Upload your PDFs in the main area to start interacting with them.")
        st.file_uploader("Upload your PDFs here and click on 'Process'", type=["pdf"], accept_multiple_files=True)
        st
if __name__ == "__main__":
    main()