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
    st.session_state.offer_submitted = False  # flag to clear form on submit

# ---------- Login Screen ----------
def login_screen():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.session_state.logged_in = True
        st.session_state.user = username
        st.experimental_rerun()
        return  # Stop further execution after rerun

# ---------- Main App ----------
def main_app():
    st.sidebar.write(f"Logged in as {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.experimental_rerun()
        return  # Stop further execution after rerun

    selection = st.sidebar.radio("Menu", ["Offer Entry", "History"])
    if selection == "Offer Entry":
        show_offer_form()
    elif selection == "History":
        show_history()

# ---------- Offer Entry Form ----------
def show_offer_form():
    st.title("Rebate Offer Entry")

    # Hardcoded Data
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

    if st.session_state.offer_submitted:
        keys_to_clear = [
            "retailer", "specialist", "grower", "competitive_brand", "rationale",
            "offer_name", "brand", "volume", "uom", "offer_per_uom"
        ]
        for key in keys_to_clear:
            if key in st.session_state:
                del st.session_state[key]
        st.session_state.offer_submitted = False

    retailer = st.selectbox("Retailer", member_retailers, key="retailer")
    specialist = st.selectbox("Salesperson", crop_specialists.get(retailer, []), key="specialist")
    budget_total = budgets.get(specialist, 0)

    grower = st.text_input("Grower Name", key="grower")
    competitive_brand = st.selectbox("Competitive Brand", competitive_brands, key="competitive_brand")
    rationale = st.text_area("Competitive Rationale", key="rationale")

    offer_name = st.selectbox("Rebate Offer", rebate_offers, key="offer_name")
    brand = st.selectbox("Product Sold", brands_sold.get(offer_name, []), key="brand")
    volume = st.number_input("Volume", min_value=0.0, step=1.0, key="volume")
    uom = st.selectbox("Unit of Measure", uoms, key="uom")
    offer_per_uom = st.number_input("Offer per Unit ($)", min_value=0.0, step=1.0, key="offer_per_uom")

    offer_total = volume * offer_per_uom
    st.metric("Total Offer Value ($)", f"{offer_total:,.2f}")

    st.subheader("Budget Overview")
    budget_used = offer_total
    remaining_budget = max(0, budget_total - budget_used)
    st.write(f"Total Budget: ${budget_total:,.2f}")
    st.write(f"Used: ${budget_used:,.2f}")
    st.write(f"Remaining: ${remaining_budget:,.2f}")

    if st.button("Submit Offer"):
        new_offer = {
            "Retailer": retailer,
            "Salesperson": specialist,
            "Grower": grower,
            "Competitive Brand": competitive_brand,
            "Rationale": rationale,
            "Rebate Offer": offer_name,
            "Product Sold": brand,
            "Volume": volume,
            "Unit of Measure": uom,
            "Offer per Unit ($)": offer_per_uom,
            "Offer Total": offer_total,
        }
        st.session_state.submitted_offers.append(new_offer)
        st.success(f"Submitted offer for '{grower}' under '{offer_name}'.")
        st.session_state.offer_submitted = True
        # No rerun here — form will reset on next interaction

# ---------- History View ----------
def show_history():
    st.title("Submitted Offers History")

    if not st.session_state.submitted_offers:
        st.info("No offers submitted yet.")
        return

    df = pd.DataFrame(st.session_state.submitted_offers)
    st.dataframe(df)

# ---------- Run ----------
if st.session_state.logged_in:
    main_app()
else:
    login_screen()
