import warnings
import sys
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import altair as alt


st.set_page_config(
    page_title="Zeitreihenanalyse",
    page_icon = ":hearts:",
    layout="wide",
    menu_items={
        'Report a bug': "mailto:haanhhanoitran@gmail.com",
        'About': "Eine App hergestellt für die Visualisierung von Hypertonie Daten \n"
                 "Autor: Ludmila Janzen, Mahshid Ghasempour, Ha Anh Tran"
    }
)

################################################################################

def country(selected_stocks):
    item_list = []
    for items in selected_stocks:
        item_list.append(items)
    return item_list


def create_chart(df, selected_stocks):
    return (
        alt.Chart(df)
        .transform_fold(
            country(selected_stocks),
            as_=["series", "value"]
        )
        .mark_line()
        .encode(
            x="timestamp:T",
            y="value:Q",
            color="series:N",
            tooltip=["timestamp:T", "series:N", "value:Q"]
        )
        .interactive()
    )


###############################################################################
st.title("Entwicklung von Hypertonie")
st.subheader(":hearts:")
#####

#dummy frame für die Zeitfilterung
np.random.seed(42)
data = pd.DataFrame({
    "timestamp": pd.date_range("2025-01-01", periods=2000, freq="D"),
    "value a": np.random.randn(2000).cumsum(),
    "value b" : np.random.randn(2000).cumsum()
})


df = pd.DataFrame({
    "timestamp": pd.date_range("2025-01-01", periods=2000, freq="D"),
    "value a": np.random.randn(2000).cumsum(),
    "value b" : np.random.randn(2000).cumsum()
})


selected_stocks = True

st.write(df)

first_date = df["timestamp"].min().to_pydatetime()
st.write(first_date)
last_date = df["timestamp"].max().to_pydatetime()


##########################################

st.sidebar.subheader("Filtereinstellung")
st.sidebar.write("Hier kannst du die Graphen filtern")

#fügt Aktiennamen in die Seitenleiste als pills und filtert duplikate
selected_stocks = st.sidebar.pills("Auswahl", data.columns[1:].drop_duplicates(), selection_mode ="multi")

#Zeiteinstelllung



#with st.sidebar.popover("Zeit-Einstellung"):
#    date_range = (first_date, last_date)
#    if selected_stocks:
#        selected_date_range = st.slider(
#            "Wähle deinen Zeitraum",
#            min_value = first_date,
#            max_value = last_date,
#            value = date_range , #setzt den Zeitrahmen auf dem vollen Zeitraum
#            format = "YYYY-MM-DD",
#            step = pd.Timedelta(weeks=1).to_pytimedelta(), #stellt sicher, dass der slider in 1 Wochen schritten arbeitet
#           key = "hallo1"
#        )
#        teste = False
#    else:
#        selected_date_range = False
#        teste = True

if selected_stocks:
    teste = False
else:
    selected_date_range = False
    teste = True

date_range = (first_date, last_date)
selected_date_range = st.sidebar.slider(
    "Wähle deinen Zeitraum",
    min_value = first_date,
    max_value = last_date,
    value = date_range , #setzt den Zeitrahmen auf dem vollen Zeitraum
    format = "YYYY-MM-DD",
    step = pd.Timedelta(weeks=1).to_pytimedelta(), #stellt sicher, dass der slider in 1 Wochen schritten arbeitet
    disabled = teste,
    key = "hallo3"
)


st.sidebar.write(selected_stocks)



#Daterange Implementierung
if selected_stocks:
    df = df[
        (df["timestamp"]>=selected_date_range[0]) &
        (df["timestamp"]<=selected_date_range[1])
    ]




#####


st.write("hallo")
spalte_1, spalte_2 = st.columns([1,2])
with spalte_1:
    options = st.multiselect(
        "What are your favorite colors?",
        ["Green", "Yellow", "Red", "Blue"],
        default=["Yellow", "Red"],
    )

st.write("You selected:", options)
for items in options:
    if items == "Green":
        st.write("Green is in the seleceted item")

st.subheader("Zeitspanne :alarm_clock:")
if selected_date_range:
    st.write(selected_date_range, selected_date_range[0], selected_date_range[1])


################################################


if selected_stocks:
    chart = create_chart(df, selected_stocks)

    tab1, tab2 = st.tabs(
        ["Streamlit theme (default)", "Altair native theme"]
    )

    with tab1:
        st.altair_chart(chart, theme="streamlit", use_container_width=True)

    with tab2:
        st.altair_chart(chart, theme=None, use_container_width=True)
else:
    st.write("Wähle in der Seitenleiste ein Land aus")



#################################################################


st.write(df[["value a", "value b"]].describe())