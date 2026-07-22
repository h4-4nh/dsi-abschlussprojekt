#docs.streamlit.io
#https://docs.streamlit.io/develop/quick-reference/cheat-sheet
#framework
import warnings
import sys
from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from streamlit_javascript import st_javascript

BASE_DIR = Path(__file__).resolve().parent



#Name der App, Stil, Menu Leiste
st.set_page_config(
    page_title="Startseite",
    page_icon=":hearts:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "mailto:haanhhanoitran@gmail.com",
        'About': "Eine App hergestellt für die Visualisierung von Hypertonie Daten \n"
                 "Autor: Ludmila Janzen, Mahshid Ghasempour, Ha Anh Tran"
    }
)

# Pfad zum Pages-Ordner
pages_dir = Path(__file__).parent / "Pages"


# Navigation definieren
pg = st.navigation(
    [
        st.Page(
            pages_dir / "0_Startseite.py",
            title="Startseite",
            icon="🏠"
        ),
        st.Page(
            pages_dir / "1_Zeitreihenanalyse.py",
            title="Zeitreihenanalyse",
            icon="📈"
        ),
        st.Page(
            pages_dir / "2_Risikofaktoren.py",
            title="Risikofaktoren",
            icon="⚠️"
        ),
        st.Page(
            pages_dir / "3_Risiko_auf_Hypertonie.py",
            title="Risiko auf Hypertonie",
            icon="🔍"
        ),
        st.Page(
            pages_dir / "4_Impressum.py",
            title="Impressum",
            icon="ℹ️"
        )
    ]
)

pg.run()


