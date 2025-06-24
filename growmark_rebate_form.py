import streamlit as st

# ----- Hardcoded Lookup Data -----
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

# ----- Form UI -----
st.title("GROWMARK Rebate Offer Entry")

# Retailer & Specialist
retailer = st.selectbox("Member Retailer", member_retailers)
specialist = st.selectbox("Crop Specialist", crop_specialists.get(retailer, []))
budget_total = budgets.get(specialist, 0)

# Grower & Rationale
grower = st.text_input("Grower Name (autocomplete not implemented)", "")
competitive_brand = st.selectbox("Current Competitive Brand", competitive_brands)
rationale = st.text_area("Competitive Rationale", "")

# Rebate Offer Details
offer_name = st.selectbox("Rebate Offer Name", rebate_offers)
brand = st.selectbox("Brand Sold", brands_sold.get(offer_name, []))
volume = st.number_input("Volume Committed", min_value=0.0, step=1.0)
uom = st.selectbox("Unit of Measure", uoms)
offer_per_uom = st.number_input("Offer per UOM ($)", min_value=0.0, step=1.0)

# Calculations
offer_total = volume * offer_per_uom
st.metric("Offer Total ($)", f"{offer_total:,.2f}")

# Budget Tracking
# Placeholder logic – you can enhance this later with real tracking
st.subheader("Budget Overview")
budget_used = offer_total  # simplification
remaining_budget = max(0, budget_total - budget_used)
st.write(f"Total Budget for {specialist}: ${budget_total:,.2f}")
st.write(f"Used So Far: ${budget_used:,.2f}")
st.write(f"Remaining Budget: ${remaining_budget:,.2f}")

# Submit
if st.button("Submit Offer"):
    st.success(f"Offer submitted for grower '{grower}' under program '{offer_name}'.")
