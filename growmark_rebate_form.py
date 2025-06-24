import streamlit as st

# ---------- Session State Login ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------- Login Screen ----------
def login_screen():
    st.markdown("""
        <style>
            .stApp {
                background-image: url("https://images.unsplash.com/photo-1602526210318-73ec0b8d8248?auto=format&fit=crop&w=1350&q=80");
                background-size: cover;
                background-position: center;
            }
            .login-box {
                background-color: rgba(255, 255, 255, 0.9);
                padding: 2rem;
                border-radius: 1rem;
                max-width: 400px;
                margin: auto;
                margin-top: 5rem;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.header("Smartwyre Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username and password:
                st.session_state.logged_in = True
                st.session_state.user = username
                st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- Main App UI ----------
def main_app():
    st.set_page_config(page_title="Smartwyre", layout="centered")
    st.markdown(
        """
        <style>
        .main {background-color: #ffffff;}
        h1 {color: #2a733b;}
        .css-18e3th9 {background-color: #ffffff;}
        </style>
        """, unsafe_allow_html=True)

    st.sidebar.success(f"Logged in as {st.session_state.user}")
    selection = st.sidebar.radio("Menu", ["Growmark Seed Program Entry"])

    if selection == "Growmark Seed Program Entry":
        show_seed_form()

# ---------- Growmark Offer Form ----------
def show_seed_form():
    st.title("Growmark Seed Program Entry")

    # Hardcoded Data
    member_retailers = ["FS Central", "FS Heartland", "FS Illinois"]
    crop_specialists = {
        "FS Central": ["Alice Smith", "Bob Jones"],
        "FS Heartland": ["Carla Evans", "David Kim"],
        "FS Illinois": ["Ellen Johnson", "Frank Miller"]
    }
    growers = ["John Deere", "Mary Agri", "Bob Farm", "Jane Ranch"]
    competitive_brands = ["Pioneer", "Dekalb", "Channel", "Stine"]
    rebate_offers = ["Early Commit", "Volume Bonus", "Competitive Match"]
    brands_sold = {
        "Early Commit": ["Growmark Seed A", "Growmark Seed B"],
        "Volume Bonus": ["Growmark Seed C", "Growmark Seed D"],
        "Competitive Match": ["Growmark Seed B", "Growmark Seed D"]
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

    retailer = st.selectbox("Member Retailer", member_retailers)
    specialist = st.selectbox("Crop Specialist", crop_specialists.get(retailer, []))
    budget_total = budgets.get(specialist, 0)

    grower = st.text_input("Grower Name", "")
    competitive_brand = st.selectbox("Current Competitive Brand", competitive_brands)
    rationale = st.text_area("Competitive Rationale")

    offer_name = st.selectbox("Rebate Offer Name", rebate_offers)
    brand = st.selectbox("Brand Sold", brands_sold.get(offer_name, []))
    volume = st.number_input("Volume Committed", min_value=0.0, step=1.0)
    uom = st.selectbox("Unit of Measure", uoms)
    offer_per_uom = st.number_input("Offer per UOM ($)", min_value=0.0, step=1.0)

    offer_total = volume * offer_per_uom
    st.metric("Offer Total ($)", f"{offer_total:,.2f}")

    st.subheader("Budget Overview")
    budget_used = offer_total
    remaining_budget = max(0, budget_total - budget_used)
    st.write(f"Total Budget: ${budget_total:,.2f}")
    st.write(f"Used: ${budget_used:,.2f}")
    st.write(f"Remaining: ${remaining_budget:,.2f}")

    if st.button("Submit Offer"):
        st.success(f"Submitted offer for '{grower}' under '{offer_name}'.")

# ---------- Run App ----------
if st.session_state.logged_in:
    main_app()
else:
    login_screen()
