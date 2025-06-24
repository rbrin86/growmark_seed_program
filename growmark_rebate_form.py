import streamlit as st
import pandas as pd

# ---------- Session State Setup ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "submitted_offers" not in st.session_state:
    st.session_state.submitted_offers = []
if "offer_submitted" not in st.session_state:
    st.session_state.offer_submitted = False
if "action" not in st.session_state:
    st.session_state.action = None  # 'login' or 'logout'

# ---------- Login Screen ----------
def login_screen():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.session_state.logged_in = True
        st.session_state.user = username
        st.session_state.action = "login"

# ---------- Main App ----------
def main_app():
    st.sidebar.write(f"Logged in as {st.session_state.user}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.action = "logout"
        return

    selection = st.sidebar.radio("Menu", ["Offer Entry", "History"])
    if selection == "Offer Entry":
        show_offer_form()
    elif selection == "History":
        show_history()

# ---------- Offer Entry Form ----------
def show_offer_form():
    st.title("Rebate Offer Entry")

    # Static Data
    member_retailers = ["Retailer A", "Retailer B", "Retailer C"]
    crop_specialists = {
        "Retailer A": ["Alice Smith", "Bob Jones"],
        "Retailer B": ["Carla Evans", "David Kim"],
        "Retailer C": ["Ellen Johnson", "Frank Miller"]
    }
    competitive_brands = ["Brand X", "Brand Y", "Brand Z"]
    rebate_offers = ["Offer 1", "Offer 2", "Offer 3"]
    brands_sold = {
        "Offer 1": ["Product A", "Product B"],
        "Offer 2": ["Product C", "Product D"],
        "Offer 3": ["Product B", "Product D"]
    }
    uoms = ["Bag", "Unit"]
    budgets = {
        "Alice Smith": 10000,
        "Bob Jones": 12000,
        "Carla Evans": 8000,
        "David Kim": 9500,
        "Ellen Johnson": 11000,
        "Frank Miller": 7000
    }
    growers = [
        {
            "name": "John Deere",
            "gln": "1234567890123",
            "address": "123 Farm Lane, Springfield, IL"
        },
        {
            "name": "Mary Agri",
            "gln": "9876543210987",
            "address": "456 Crop Rd, Lincoln, NE"
        },
        {
            "name": "Bob Farm",
            "gln": "4567891234567",
            "address": "789 Harvest Ave, Des Moines, IA"
        },
    ]

    if st.session_state.offer_submitted:
        for key in [
            "retailer", "specialist", "competitive_brand",
            "rationale", "offer_name", "brand", "volume", "uom", "offer_per_uom", "grower"
        ]:
            if key in st.session_state:
                del st.session_state[key]
        st.session_state.offer_submitted = False

    retailer = st.selectbox("Retailer", member_retailers, key="retailer")_
