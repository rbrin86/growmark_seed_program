import streamlit as st

# ---------- Session State Setup ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "login_attempt" not in st.session_state:
    st.session_state.login_attempt = False
if "logout_attempt" not in st.session_state:
    st.session_state.logout_attempt = False

# ---------- Login Screen ----------
def login_screen():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.session_state.logged_in = True
        st.session_state.user = username
        st.session_state.login_attempt = True
        st.rerun()

# ---------- Main App ----------
def main_app():
    st.title("Rebate Offer Entry")

    st.sidebar.write(f"Logged in as {st.session_state.user}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.logout_attempt = True
        st.rerun()

    selection = st.sidebar.radio("Menu", ["Offer Entry"])
    if selection == "Offer Entry":
        show_offer_form()

# ---------- Offer Entry Form ----------
def show_offer_form():
    # Hardcoded Data
    member_retailers = ["Retailer A", "Retailer B", "Retailer C"]
    crop_specialists = {
        "Retailer A": ["Alice Smith", "Bob Jones"],
        "Retailer B": ["Carla Evans", "David Kim"],
        "Retailer C": ["Ellen Johnson", "Frank Miller"]
    }
    growers = ["John Deere", "Mary Agri", "Bob Farm", "Jane Ranch"]
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

    retailer = st.selectbox("Retailer", member_retailers)
    specialist = st.selectbox("Salesperson", crop_specialists.get(retailer, []))
    budget_total = budgets.get(specialist, 0)

    grower = st.text_input("Grower Name")
    competitive_brand = st.selectbox("Competitive Brand", competitive_brands)
    rationale = st.text_area("Competitive Rationale")

    offer_name = st.selectbox("Rebate Offer", rebate_offers)
    brand = st.selectbox("Product Sold", brands_sold.get(offer_name, []))
    volume = st.number_input("Volume", min_value=0.0, step=1.0)
    uom = st.selectbox("Unit of Measure", uoms)
    offer_per_uom = st.number_input("Offer per Unit ($)", min_value=0.0, step=1.0)

    offer_total = volume * offer_per_uom
    st.metric("Total Offer Value ($)", f"{offer_total:,.2f}")

    st.subheader("Budget Overview")
    budget_used = offer_total
    remaining_budget = max(0, budget_total - budget_used)
    st.write(f"Total Budget: ${budget_total:,.2f}")
    st.write(f"Used: ${budget_used:,.2f}")
    st.write(f"Remaining: ${remaining_budget:,.2f}")

    if st.button("Submit Offer"):
        st.success(f"Submitted offer for '{grower}' under '{offer_name}'.")

# ---------- Run ----------
if st.session_state.logged_in:
    main_app()
else:
    login_screen()