import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    col1.image("images/photo.png")
with col2:
    col2.title("Poulomi Ghosh")
    content = ("I am a experienced web developer with hands-on in various technologies. "
               "From functional to object oriented programming I have done experienced it all. "
               "Now discovering myself in the magical world of python.")
    st.info(content)


content_title = """Below you can find some of the apps I have built in python. Feel free to contact me!"""


st.write(f"<h4>{content_title}</h4>",
         unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")