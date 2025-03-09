import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(
    page_title="Pharmaceutical Products Dashboard",
    page_icon="💊",
    layout="wide"
)

# Sample dataset based on the provided data
data = [
    {"id": 1, "name": "Augmentin", "price": 223.42, "is_discontinued": False, "manufacturer_name": "Glaxo SmithKline Pharm", "type": "allopathy", "pack_size_label": "strip of 10 tablets", "short_composition1": "Amoxycillin (500mg)", "short_composition2": "Clavulanic Acid (125mg)"},
    {"id": 2, "name": "Azithral 500", "price": 132.36, "is_discontinued": False, "manufacturer_name": "Alembic Pharmaceutical", "type": "allopathy", "pack_size_label": "strip of 5 tablets", "short_composition1": "Azithromycin (500mg)", "short_composition2": ""},
    {"id": 3, "name": "Ascoril LS Syrup", "price": 118, "is_discontinued": False, "manufacturer_name": "Glenmark Pharmaceutic", "type": "allopathy", "pack_size_label": "bottle of 100 ml Syrup", "short_composition1": "Ambroxol (30mg/5ml)", "short_composition2": "Levosalbutamol (1mg/5ml)"},
    {"id": 4, "name": "Allegra 120", "price": 218.81, "is_discontinued": False, "manufacturer_name": "Sanofi India Ltd", "type": "allopathy", "pack_size_label": "strip of 10 tablets", "short_composition1": "Fexofenadine (120mg)", "short_composition2": ""},
    {"id": 5, "name": "Avil 25 Tab", "price": 10.96, "is_discontinued": False, "manufacturer_name": "Sanofi India Ltd", "type": "allopathy", "pack_size_label": "strip of 15 tablets", "short_composition1": "Pheniramine (25mg)", "short_composition2": ""},
    {"id": 6, "name": "Allegra-M", "price": 241.48, "is_discontinued": False, "manufacturer_name": "Sanofi India Ltd", "type": "allopathy", "pack_size_label": "strip of 10 tablets", "short_composition1": "Montelukast (10mg)", "short_composition2": "Fexofenadine (120mg)"},
    {"id": 7, "name": "Amoxyclav", "price": 223.27, "is_discontinued": False, "manufacturer_name": "Abbott", "type": "allopathy", "pack_size_label": "strip of 10 tablets", "short_composition1": "Amoxycillin (500mg)", "short_composition2": "Clavulanic Acid (125mg)"},
    {"id": 8, "name": "Azee 500 Tab", "price": 132.38, "is_discontinued": False, "manufacturer_name": "Cipla Ltd", "type": "allopathy", "pack_size_label": "strip of 5 tablets", "short_composition1": "Azithromycin (500mg)", "short_composition2": ""},
    {"id": 9, "name": "Atarax 25mg", "price": 85.5, "is_discontinued": False, "manufacturer_name": "Dr Reddy's Laboratories", "type": "allopathy", "pack_size_label": "strip of 15 tablets", "short_composition1": "Hydroxyzine (25mg)", "short_composition2": ""},
    {"id": 10, "name": "Ascoril D Plus", "price": 129, "is_discontinued": False, "manufacturer_name": "Glenmark Pharmaceutic", "type": "allopathy", "pack_size_label": "bottle of 100 ml Syrup", "short_composition1": "Phenylephrine (5mg)", "short_composition2": "Chlorpheniramine Maleate (2mg)"},
    {"id": 11, "name": "Aciloc 150", "price": 40.94, "is_discontinued": False, "manufacturer_name": "Cadila Pharmaceuticals", "type": "allopathy", "pack_size_label": "strip of 30 tablets", "short_composition1": "Ranitidine (150mg)", "short_composition2": ""},
    {"id": 12, "name": "Alex Syrup", "price": 129, "is_discontinued": False, "manufacturer_name": "Glenmark Pharmaceutic", "type": "allopathy", "pack_size_label": "bottle of 100 ml Syrup", "short_composition1": "Phenylephrine (5mg)", "short_composition2": "Chlorpheniramine Maleate (2mg/5ml)"},
    {"id": 13, "name": "Anovate Cream", "price": 134.2, "is_discontinued": False, "manufacturer_name": "USV Ltd", "type": "allopathy", "pack_size_label": "tube of 20 gm Cream", "short_composition1": "Phenylephrine (0.10%)", "short_composition2": "Beclometasone (0.025% w/w)"},
    {"id": 14, "name": "Augmentin DDS", "price": 67.2, "is_discontinued": False, "manufacturer_name": "Glaxo SmithKline Pharm", "type": "allopathy", "pack_size_label": "bottle of 30 ml Oral Suspension", "short_composition1": "Amoxycillin (200mg)", "short_composition2": "Clavulanic Acid (28.5mg)"},
    {"id": 15, "name": "Ambrodil-S", "price": 30.2, "is_discontinued": False, "manufacturer_name": "Aristo Pharmaceuticals", "type": "allopathy", "pack_size_label": "bottle of 100 ml Syrup", "short_composition1": "Ambroxol (15mg/5ml)", "short_composition2": "Salbutamol (1mg/5ml)"},
    {"id": 16, "name": "Arkamin Tab", "price": 72.65, "is_discontinued": False, "manufacturer_name": "Torrent Pharmaceuticals", "type": "allopathy", "pack_size_label": "strip of 30 tablets", "short_composition1": "Clonidine (100mcg)", "short_composition2": ""},
    {"id": 17, "name": "Avomine Tab", "price": 55.98, "is_discontinued": False, "manufacturer_name": "Abbott", "type": "allopathy", "pack_size_label": "strip of 10 tablets", "short_composition1": "Promethazine (25mg)", "short_composition2": ""},
    {"id": 18, "name": "Asthakind-DX", "price": 70.4, "is_discontinued": False, "manufacturer_name": "Mankind Pharma Ltd", "type": "allopathy", "pack_size_label": "bottle of 60 ml Syrup", "short_composition1": "Phenylephrine (5mg)", "short_composition2": "Chlorpheniramine Maleate (2mg/5ml)"},
    {"id": 19, "name": "Allegra 180", "price": 251.2, "is_discontinued": False, "manufacturer_name": "Sanofi India Ltd", "type": "allopathy", "pack_size_label": "strip of 10 tablets", "short_composition1": "Fexofenadine (180mg)", "short_composition2": ""},
    {"id": 20, "name": "Albendazole", "price": 9.58, "is_discontinued": False, "manufacturer_name": "Cadila Pharmaceuticals", "type": "allopathy", "pack_size_label": "strip of 1 Tablet", "short_composition1": "Albendazole (400mg)", "short_composition2": ""}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Header
st.title("Pharmaceutical Products Dashboard")
st.markdown("Analyze medication data, pricing and compositions")
st.markdown("---")

# Extract unique active ingredients, manufacturers, and package types
def extract_ingredients(df):
    ingredients = set()
    for _, row in df.iterrows():
        comp1 = row['short_composition1'].split(' ')[0] if row['short_composition1'] else ""
        if comp1:
            ingredients.add(comp1)
        comp2 = row['short_composition2'].split(' ')[0] if row['short_composition2'] else ""
        if comp2:
            ingredients.add(comp2)
    return sorted(list(ingredients))

def extract_manufacturers(df):
    return sorted(df['manufacturer_name'].unique())

def extract_pack_types(df):
    pack_types = []
    for pack in df['pack_size_label'].unique():
        parts = pack.split(' of ')
        if parts[0] not in pack_types:
            pack_types.append(parts[0])
    return sorted(pack_types)

unique_ingredients = extract_ingredients(df)
unique_manufacturers = extract_manufacturers(df)
unique_pack_types = extract_pack_types(df)

# Sidebar filters
st.sidebar.title("Filters")

# Search box
search_term = st.sidebar.text_input("Search medicines or ingredients", "")

# Active Ingredient Filter
selected_ingredient = st.sidebar.selectbox(
    "Filter by Ingredient",
    ["All"] + unique_ingredients
)

# Manufacturer Filter
selected_manufacturer = st.sidebar.selectbox(
    "Filter by Manufacturer",
    ["All"] + unique_manufacturers
)

# Package Type Filter
selected_pack_type = st.sidebar.selectbox(
    "Filter by Package Type",
    ["All"] + unique_pack_types
)

# Price Range Filter
price_range = st.sidebar.slider(
    "Price Range (₹)",
    min_value=0,
    max_value=300,
    value=(0, 300)
)

# Apply filters
filtered_df = df.copy()

# Search term filter
if search_term:
    filtered_df = filtered_df[
        filtered_df['name'].str.contains(search_term, case=False) |
        filtered_df['short_composition1'].str.contains(search_term, case=False) |
        filtered_df['short_composition2'].str.contains(search_term, case=False)
    ]

# Ingredient filter
if selected_ingredient != "All":
    filtered_df = filtered_df[
        filtered_df['short_composition1'].str.contains(selected_ingredient, case=False) |
        filtered_df['short_composition2'].str.contains(selected_ingredient, case=False)
    ]

# Manufacturer filter
if selected_manufacturer != "All":
    filtered_df = filtered_df[filtered_df['manufacturer_name'] == selected_manufacturer]

# Pack type filter
if selected_pack_type != "All":
    filtered_df = filtered_df[filtered_df['pack_size_label'].str.startswith(selected_pack_type)]

# Price range filter
filtered_df = filtered_df[
    (filtered_df['price'] >= price_range[0]) &
    (filtered_df['price'] <= price_range[1])
]

# Stats Cards
st.subheader("Summary Statistics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Products",
        value=len(filtered_df)
    )

with col2:
    avg_price = filtered_df['price'].mean() if not filtered_df.empty else 0
    st.metric(
        label="Average Price",
        value=f"₹{avg_price:.2f}"
    )

with col3:
    unique_manuf_count = filtered_df['manufacturer_name'].nunique() if not filtered_df.empty else 0
    st.metric(
        label="Unique Manufacturers",
        value=unique_manuf_count
    )

with col4:
    min_price = filtered_df['price'].min() if not filtered_df.empty else 0
    max_price = filtered_df['price'].max() if not filtered_df.empty else 0
    st.metric(
        label="Price Range",
        value=f"₹{min_price:.2f} - ₹{max_price:.2f}"
    )

# Create tabs
tab1, tab2 = st.tabs(["Product List", "Analytics"])

# Tab 1 - Product List
with tab1:
    if not filtered_df.empty:
        # Format the price column with color-coding
        def format_price(price):
            if price < 50:
                return f"<span style='background-color:#d1fae5; color:#065f46; padding:4px 8px; border-radius:9999px;'>₹{price:.2f}</span>"
            elif price < 100:
                return f"<span style='background-color:#dbeafe; color:#1e40af; padding:4px 8px; border-radius:9999px;'>₹{price:.2f}</span>"
            elif price < 200:
                return f"<span style='background-color:#fef3c7; color:#92400e; padding:4px 8px; border-radius:9999px;'>₹{price:.2f}</span>"
            else:
                return f"<span style='background-color:#fee2e2; color:#991b1b; padding:4px 8px; border-radius:9999px;'>₹{price:.2f}</span>"

        # Create a copy with formatted price for display
        display_df = filtered_df.copy()
        display_df['formatted_price'] = filtered_df['price'].apply(format_price)
        
        # Select and reorder columns for display
        display_cols = ['name', 'formatted_price', 'manufacturer_name', 'pack_size_label', 'short_composition1', 'short_composition2']
        renamed_cols = {
            'name': 'Name',
            'formatted_price': 'Price',
            'manufacturer_name': 'Manufacturer',
            'pack_size_label': 'Package',
            'short_composition1': 'Composition 1',
            'short_composition2': 'Composition 2'
        }
        
        # Display the table with HTML formatting enabled
        st.write(display_df[display_cols].rename(columns=renamed_cols).to_html(escape=False, index=False), unsafe_allow_html=True)
    else:
        st.info("No products match your current filters.")

# Tab 2 - Analytics
with tab2:
    if not filtered_df.empty:
        # Create a 2x2 grid for charts
        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)

        # Top Manufacturers Chart
        with row1_col1:
            st.subheader("Top Manufacturers")
            manuf_counts = filtered_df['manufacturer_name'].value_counts().reset_index()
            manuf_counts.columns = ['manufacturer', 'count']
            manuf_counts = manuf_counts.sort_values('count', ascending=False).head(5)
            
            fig_manuf = px.bar(
                manuf_counts,
                x='manufacturer',
                y='count',
                labels={'manufacturer': 'Manufacturer', 'count': 'Number of Products'},
                color_discrete_sequence=['#3B82F6']
            )
            fig_manuf.update_layout(xaxis_title='', yaxis_title='Number of Products')
            st.plotly_chart(fig_manuf, use_container_width=True)

        # Price Distribution Chart
        with row1_col2:
            st.subheader("Price Distribution")
            price_bins = [0, 50, 100, 150, 200, 300]
            price_labels = ['< ₹50', '₹50-100', '₹100-150', '₹150-200', '> ₹200']
            filtered_df['price_range'] = pd.cut(filtered_df['price'], bins=price_bins, labels=price_labels, right=False)
            price_dist = filtered_df['price_range'].value_counts().reset_index()
            price_dist.columns = ['price_range', 'count']
            price_dist = price_dist.sort_values('price_range')
            
            fig_price = px.bar(
                price_dist,
                x='price_range',
                y='count',
                labels={'price_range': 'Price Range', 'count': 'Number of Products'},
                color_discrete_sequence=['#10B981']
            )
            fig_price.update_layout(xaxis_title='', yaxis_title='Number of Products')
            st.plotly_chart(fig_price, use_container_width=True)

        # Package Types Chart
        with row2_col1:
            st.subheader("Package Types Distribution")
            pack_counts = {}
            for _, row in filtered_df.iterrows():
                pack_type = row['pack_size_label'].split(' of ')[0]
                pack_counts[pack_type] = pack_counts.get(pack_type, 0) + 1
            
            pack_df = pd.DataFrame({
                'pack_type': list(pack_counts.keys()),
                'count': list(pack_counts.values())
            })
            
            fig_pack = px.pie(
                pack_df,
                values='count',
                names='pack_type',
                title='',
                color_discrete_sequence=px.colors.qualitative.Set1
            )
            fig_pack.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pack, use_container_width=True)

        # Top Products by Price
        with row2_col2:
            st.subheader("Top Products by Price")
            top_price_df = filtered_df.sort_values('price', ascending=False).head(5)
            
            fig_top = px.bar(
                top_price_df,
                y='name',
                x='price',
                labels={'name': 'Product', 'price': 'Price (₹)'},
                color_discrete_sequence=['#F59E0B'],
                orientation='h'
            )
            fig_top.update_layout(yaxis_title='', xaxis_title='Price (₹)')
            st.plotly_chart(fig_top, use_container_width=True)
    else:
        st.info("No data available for analytics with current filters.")

# Footer
st.markdown("---")
st.caption("Pharmaceutical Products Analysis Dashboard")



############################
