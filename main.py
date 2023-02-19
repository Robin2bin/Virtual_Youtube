import streamlit as st
import pandas as pd
from pytube import YouTube
st.set_page_config(page_title='Robin2bin',layout="wide",page_icon='https://yt3.ggpht.com/ytc/AMLnZu-ox03apyeCNpE3H-TRf7TdP9OjSi_I8DssPSIsaA=s900-c-k-c0x00ffffff-no-rj')
hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.container(): #banner and header
    st.image('banner.png')
    st.write("---")

with st.container(): # all videos robin2bin official mail
    st.subheader("Robin2bin official mail Uploads")
    data = pd.DataFrame(pd.read_csv("Robin2bin_official_mail_edited.csv"))
    links = data['Links']
    title = data['Video_title']
    likes = data['Likes']
    views = data['Views']
    thumbnails = data['Thumbnails']
    rangeA = 0
    rangeB = 5
    while(rangeB <= len(links)):
        cols = st.columns(5)
        s = 0
        for c in range(rangeA,rangeB):
            with cols[s]:
                st.image(thumbnails[c])
                st.write("[" + title[c] + "]" + "(" + links[c] + ")")
                st.write(":eye-in-speech-bubble: " + str(views[c]) + "	:thumbsup: " + str(likes[c]))
            s += 1
        rangeA = rangeB
        rangeB += 5
    st.write("---")

with st.container(): # all videos of robin2bin
    st.subheader("Robin2bin Uploads")
    data = pd.DataFrame(pd.read_csv("Robin2bin_edited.csv"))
    links = data['Links']
    title = data['Video_title']
    likes = data['Likes']
    views = data['Views']
    thumbnails = data['Thumbnails']
    rangeA = 0
    rangeB = 5
    while(rangeB <= len(links)):
        cols = st.columns(5)
        s = 0
        for c in range(rangeA,rangeB):
            with cols[s]:
                st.image(thumbnails[c])
                st.write("[" + title[c] + "]" + "(" + links[c] + ")")
                st.write(":eye-in-speech-bubble: " + str(views[c]) + "	:thumbsup: " + str(likes[c]))
            s += 1
        rangeA = rangeB
        rangeB += 5
    st.write("---")
