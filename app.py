
import streamlit as st

def main():
    st.header("Welcome to the Streamlit App!")
    name = st.text_input("Enter your name:")


    col1, col2 = st.columns(2)
    with col1:
        if st.button('Display my name',type='primary', key='btn1'):
            print("Hello", name)
    with col2:
        if st.button('Clear my name',type='primary', key='btn2'):
            name = ""
    st.markdown("""

    """, unsafe_allow_html=True)
main()