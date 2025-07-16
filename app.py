import streamlit as st
import emoji # type: ignore
def main():
    st.set_page_config(page_title="AskMyPDF", page_icon=emoji.emojize(":receipt:"), layout="wide")

    st.title(emoji.emojize(":receipt: AskMyPDF"))
    st.header("Extract Information from Given PDFs")
    st.text_input(emoji.emojize(":speech_balloon: What would you like to know from your documents?"), key="user_input")

with st.sidebar:
    st.subheader(emoji.emojize(":inbox_tray: Upload PDFs"))
    uploaded_files = st.file_uploader(
        emoji.emojize("Upload your PDFs here and click the button to start analysis :arrow_down:"),
        type=["pdf"],
        accept_multiple_files=True,
        key="pdf_uploader"
    )

    if st.button(emoji.emojize(":mag: Analyze PDFs"), key="process_button"):
        if uploaded_files:
            st.success(emoji.emojize(f":white_check_mark: {len(uploaded_files)} PDF(s) are analysed and ready for information extraction."))
        else:
            st.warning(emoji.emojize(":warning: Please upload at least one PDF before information extraction."))

if __name__ == "__main__":
    main()
