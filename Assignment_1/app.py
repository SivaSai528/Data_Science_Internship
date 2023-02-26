import streamlit as st

st.title("Innomatics Data App :- Assigment 1")
st.subheader("If if want to know about the App")
btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :heart_eyes:")
    st.write("This Page Contains Information about the Naruto Anime and Pokemon Anime")
    st.balloons()