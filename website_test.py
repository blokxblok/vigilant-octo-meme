import streamlit as st
var = st.empty()
varr = st.empty()
topic = None
st.title("Welcome to the Idea Generator!")
topic = st.selectbox("Please select one topic to generate ideas on.",
    ['Painting', 'Music' , 'Sculptures', 'Nonfiction', 'Fiction', 'Videos'])
if(st.button("Submit")):
    st.subheader("Some ideas to get you started")
    if topic == str("Music"):
        first = st.write("Focus on rhythm first")
        second = st.write("Get visually inspired")
    st.subheader("Find some more ideas")
    st.write("go touch grass")