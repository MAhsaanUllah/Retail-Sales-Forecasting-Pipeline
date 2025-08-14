import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("📊 Sales Analysis Dashboard")

st.header("Monthly Sales Trend")
st.image('monthly_sales_trend.png', caption='Monthly Sales Trend')

st.header("Total Sales by Region")
st.image('total_sales_by_region.png', caption='Total Sales by Region')

st.header("Top 10 Best-Selling Products")
st.image('top_10_best_selling_products.png', caption='Top 10 Best-Selling Products')

st.header("Total Sales by Customer Segment")
st.image('total_sales_by_customer_segment.png', caption='Total Sales by Customer Segment')

st.header("Sales Trend Across Weekdays")
st.image('sales_trend_across_weekdays.png', caption='Sales Trend Across Weekdays')

st.header("Sales by Category and Region")
st.image('sales_by_category_and_region.png', caption='Sales by Category and Region')

st.header("Monthly Order Volume Over Time")
st.image('monthly_order_volume_over_time.png', caption='Monthly Order Volume Over Time')

st.header("Daily Sales Trend Over Time")
st.image('daily_sales_trend_over_time.png', caption='Daily Sales Trend Over Time')

st.header("Sales by Sub-Category (Grouped by Category)")
st.image('sales_by_subcategory_grouped_by_category.png', caption='Sales by Sub-Category (Grouped by Category)')

st.header("Average Sales per Order by Sub-Category")
st.image('average_sales_per_order_by_subcategory.png', caption='Average Sales per Order by Sub-Category')

st.header("Top 10 Cities by Sales")
st.image('top_10_cities_by_sales.png', caption='Top 10 Cities by Sales')

st.header("Sales Dashboard")
st.image('sales_dashboard.png', caption='Sales Dashboard')
