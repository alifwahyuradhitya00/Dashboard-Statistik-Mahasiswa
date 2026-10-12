import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Dashboard Data Statistik Mahasiswa",
    page_icon="📊",
    layout="wide"
)

html_path = Path(__file__).parent / "dashboard.html"
html = html_path.read_text(encoding="utf-8")

# Menampilkan website HTML dan JavaScript yang sudah ada di dalam aplikasi Streamlit.
components.html(html, height=2600, scrolling=True)
