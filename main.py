import streamlit as st
from repository.law_repository import LawRepository
from service.legal_service import LegalService
from ai.rag_engine import RAGEngine

st.set_page_config(
    page_title="AI Legal Assistant",
    page_icon="⚖️",
    layout="wide"
)

repo = LawRepository("data/laws.txt")
rag_engine = RAGEngine()
service = LegalService(repo, rag_engine)
service.initialize_data()

st.title("AI Legal Assistant")
st.markdown("---")

st.subheader("Introdu cazul")

case_text = st.text_area(
    "Descriere",
    height=200,
    placeholder="Ex: Am trecut pe roșu și am făcut accident..."
)

if st.button("Analizează cazul"):
    if not case_text.strip():
        st.warning("Te rog introdu descrierea cazului.")
    else:
        violated, favorable = service.analyze_case(case_text)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("## 🔴 Articole posibil încălcate")
            if violated:
                for article in violated:
                    st.error(f"{article.number}\n\n{article.content}")
            else:
                st.info("Nu au fost găsite articole posibil încălcate.")

        with col2:
            st.markdown("## 🟢 Articole posibil în favoare")
            if favorable:
                for article in favorable:
                    st.success(f"{article.number}\n\n{article.content}")
            else:
                st.info("Nu au fost găsite articole în favoare.")

        st.markdown("---")
        st.caption("Rezultatul este orientativ și nu reprezintă consultanță juridică.")