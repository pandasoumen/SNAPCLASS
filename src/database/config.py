import streamlit as st
import os

from supabase import create_client, Client

try:
    supabase_url = st.secrets.get("SUPABASE_URL")
    supabase_key = st.secrets.get("SUPABASE_KEY")
except Exception:
    supabase_url = None
    supabase_key = None

supabase_url = supabase_url or os.getenv("SUPABASE_URL")
supabase_key = supabase_key or os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    st.error("Supabase is not configured. Set SUPABASE_URL and SUPABASE_KEY.")
    st.stop()

supabase: Client = create_client(
    supabase_url,
    supabase_key
)
