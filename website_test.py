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
        if st.button("Focus on rhythm first"):
            st.text("A good melody relies of a good rhythm, as does a good song. Starting with rhythm is generally a lot easier than composing the actual contour of the melody.")
    st.subheader("Find some more ideas")
    st.write("go touch grass")