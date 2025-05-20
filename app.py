import streamlit as st
from chains import main_chain
from datetime import datetime
from fpdf import FPDF

# App title and page setup
st.set_page_config(page_title="Python-Tutor", layout="wide")
st.title("📚 Your Own Python-Tutor")

# Session state for storing conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# User input
query = st.text_input("💬 Ask a question:")

# Process input
if query:
    with st.spinner("Thinking..."):
        response = main_chain.invoke(query)
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Store both query and response with timestamps
        st.session_state.conversation.append(("user", query, timestamp))
        st.session_state.conversation.append(("assistant", response, timestamp))

# Display conversation
st.markdown("---")
for role, msg, time in st.session_state.conversation:
    if role == "user":
        st.markdown(f"🧑‍💻 **You** [{time}]:")
        st.markdown(f"> {msg}")
    else:
        st.markdown(f"🤖 **Assistant** [{time}]:")
        st.markdown(f"""
        <div style='
        background-color: #ffffff;
        color: #000000;
        padding: 12px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        font-size: 16px;
        line-height: 1.6;
    '>
        {msg}
    </div>
""", unsafe_allow_html=True)

    st.markdown("---")

# Function to save as PDF
def save_to_pdf(convo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.cell(200, 10, txt="Python Assistant Conversation", ln=True, align="C")
    pdf.ln(10)

    for role, msg, time in convo:
        sender = "You" if role == "user" else "Assistant"
        pdf.multi_cell(0, 10, f"{sender} [{time}]: {msg}")
        pdf.ln(2)

    pdf_path = "conversation.pdf"
    pdf.output(pdf_path)
    return pdf_path

# PDF download button
if st.button("📄 Download as PDF"):
    pdf_path = save_to_pdf(st.session_state.conversation)
    with open(pdf_path, "rb") as f:
        st.download_button(label="Download PDF", data=f, file_name="conversation.pdf", mime="application/pdf")
