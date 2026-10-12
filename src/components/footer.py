import streamlit as st


def footer_home():
    st.markdown(
        """
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with love by Soumen </p>

        # <img src='' style='max-height:25px' />
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():
    st.markdown(
        """
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with love by Soumen</p>

        # <img src='' style='max-height:25px' />

        </div>
        """,
        unsafe_allow_html=True,
    )
