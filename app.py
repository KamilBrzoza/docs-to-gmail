from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Google Docs → Gmail",
    page_icon="✉️",
    layout="centered",
)

# Ukryj domyślny chrome Streamlita, żeby narzędzie wyglądało jak samodzielna apka.
st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      header {visibility: hidden;}
      footer {visibility: hidden;}
      .block-container {padding-top: 1.2rem; padding-bottom: 0rem; max-width: 820px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Całe narzędzie żyje po stronie przeglądarki (wklejanie + czyszczenie + kopiowanie),
# więc po prostu wczytujemy index.html i osadzamy go w komponencie.
html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")

components.html(html, height=680, scrolling=True)
