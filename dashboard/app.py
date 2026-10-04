
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Delivery Operations Analytics",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 Delivery Delay & Operations Analytics")

st.write(
    "Analysis of delivery performance, delay patterns, "
    "seller hotspots, product categories, routes, and operational trends."
)

# ---------------------------------------------------------
# DATA PATH
# ---------------------------------------------------------

DATA_PATH = "/content/dashboard_data"

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

kpi = pd.read_csv(f"{DATA_PATH}/kpi_summary.csv")
monthly = pd.read_csv(f"{DATA_PATH}/monthly_analysis.csv")
seller = pd.read_csv(f"{DATA_PATH}/seller_analysis.csv")
category = pd.read_csv(f"{DATA_PATH}/category_analysis.csv")
day = pd.read_csv(f"{DATA_PATH}/day_analysis.csv")
season = pd.read_csv(f"{DATA_PATH}/season_analysis.csv")
status = pd.read_csv(f"{DATA_PATH}/delivery_status.csv")
route = pd.read_csv(f"{DATA_PATH}/route_analysis.csv")

# ---------------------------------------------------------
# KPI VALUES
# ---------------------------------------------------------

total_orders = kpi.loc[
    kpi["KPI"] == "Total Orders", "Value"
].iloc[0]

on_time_percentage = kpi.loc[
    kpi["KPI"] == "On-Time Percentage", "Value"
].iloc[0]

delayed_orders = kpi.loc[
    kpi["KPI"] == "Delayed Orders", "Value"
].iloc[0]

delay_percentage = kpi.loc[
    kpi["KPI"] == "Delay Percentage", "Value"
].iloc[0]

# ---------------------------------------------------------
# KPI CARDS
# ---------------------------------------------------------

st.subheader("📌 Key Delivery KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Orders",
    f"{int(total_orders):,}"
)

col2.metric(
    "On-Time Delivery",
    f"{float(on_time_percentage):.2f}%"
)

col3.metric(
    "Delayed Orders",
    f"{int(delayed_orders):,}"
)

col4.metric(
    "Delay Rate",
    f"{float(delay_percentage):.2f}%"
)

st.divider()

# ---------------------------------------------------------
# DELIVERY STATUS
# ---------------------------------------------------------

st.subheader("📦 Delivery Status")

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots()

    ax.bar(
        status["delivery_status"],
        status["order_count"]
    )

    ax.set_xlabel("Delivery Status")
    ax.set_ylabel("Number of Orders")
    ax.set_title("On-Time vs Delayed Orders")

    st.pyplot(fig)

with col2:

    st.dataframe(
        status,
        use_container_width=True
    )

# ---------------------------------------------------------
# MONTHLY TREND
# ---------------------------------------------------------

st.subheader("📈 Monthly Delivery Delay Trend")

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    monthly["delivery_month"],
    monthly["delay_percentage"],
    marker="o"
)

ax.set_xlabel("Month")
ax.set_ylabel("Delay Percentage (%)")
ax.set_title("Monthly Delivery Delay Percentage")

plt.xticks(rotation=45)

st.pyplot(fig)

# ---------------------------------------------------------
# SELLER HOTSPOTS
# ---------------------------------------------------------

st.subheader("🏪 Seller Delay Hotspots")

top_sellers = seller[
    seller["total_orders"] >= 100
].sort_values(
    "delay_percentage",
    ascending=False
).head(10)

st.dataframe(
    top_sellers,
    use_container_width=True
)

# ---------------------------------------------------------
# ROUTE HOTSPOTS
# ---------------------------------------------------------

st.subheader("🛣️ Route Delay Hotspots")

top_routes = route[
    route["total_orders"] >= 100
].sort_values(
    "delay_percentage",
    ascending=False
).head(10)

st.dataframe(
    top_routes,
    use_container_width=True
)

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    top_routes["route"],
    top_routes["delay_percentage"]
)

ax.set_xlabel("Seller State → Customer State")
ax.set_ylabel("Delay Percentage (%)")
ax.set_title("Top Route Proxies by Delay Percentage")

plt.xticks(rotation=45, ha="right")

st.pyplot(fig)

# ---------------------------------------------------------
# PRODUCT CATEGORY
# ---------------------------------------------------------

st.subheader("📦 Product Category Delay Analysis")

top_categories = category[
    category["total_orders"] >= 100
].sort_values(
    "delay_percentage",
    ascending=False
).head(10)

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    top_categories["product_category_name"],
    top_categories["delay_percentage"]
)

ax.set_xlabel("Product Category")
ax.set_ylabel("Delay Percentage (%)")
ax.set_title("Top Product Categories by Delay Percentage")

plt.xticks(rotation=45, ha="right")

st.pyplot(fig)

# ---------------------------------------------------------
# DAY OF WEEK
# ---------------------------------------------------------

st.subheader("📅 Delay Percentage by Day")

fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    day["delivery_day"],
    day["delay_percentage"]
)

ax.set_xlabel("Day")
ax.set_ylabel("Delay Percentage (%)")
ax.set_title("Delivery Delay by Day of Week")

st.pyplot(fig)

# ---------------------------------------------------------
# SEASON
# ---------------------------------------------------------

st.subheader("🌦️ Seasonal Delivery Performance")

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    season["season"],
    season["delay_percentage"]
)

ax.set_xlabel("Season")
ax.set_ylabel("Delay Percentage (%)")
ax.set_title("Delivery Delay Percentage by Season")

st.pyplot(fig)

# ---------------------------------------------------------
# OPERATIONAL INSIGHTS
# ---------------------------------------------------------

st.subheader("💡 Operational Insights")

st.markdown("""
- Monitor sellers with consistently high delay percentages.
- Investigate product categories with elevated delay rates.
- Monitor months with unusually high delivery-delay percentages.
- Compare weekend and weekday delivery performance.
- Consider order volume together with delay percentage when identifying hotspots.
- Investigate high-delay geographic route proxies for potential logistics bottlenecks.
""")





# ---------------------------------------------------------
# DECISION TREE DELAY-RISK MODEL
# ---------------------------------------------------------

st.subheader("🤖 Delivery Delay-Risk Model")

st.write(
    "A Decision Tree model was developed to estimate the risk "
    "of an order being delayed using order, timing, freight, "
    "and geographic features."
)

# Model performance
model_results = pd.read_csv(
    f"{DATA_PATH}/decision_tree_results.csv"
)

col1, col2, col3 = st.columns(3)

accuracy_value = model_results.loc[
    model_results["Metric"] == "Accuracy", "Value"
].iloc[0]

auc_value = model_results.loc[
    model_results["Metric"] == "ROC-AUC", "Value"
].iloc[0]

recall_value = model_results.loc[
    model_results["Metric"] == "Delayed Recall", "Value"
].iloc[0]

col1.metric(
    "Accuracy",
    f"{accuracy_value * 100:.2f}%"
)

col2.metric(
    "ROC-AUC",
    f"{auc_value:.4f}"
)

col3.metric(
    "Delayed Recall",
    f"{recall_value * 100:.0f}%"
)

# Feature importance
st.subheader("🔎 Top Delay-Risk Factors")

risk_features = pd.read_csv(
    f"{DATA_PATH}/delay_risk_features.csv"
)

risk_features = risk_features.head(10)

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    risk_features["feature"][::-1],
    risk_features["importance"][::-1]
)

ax.set_xlabel("Feature Importance")
ax.set_ylabel("Feature")
ax.set_title("Top Factors Used by the Decision Tree")

st.pyplot(fig)

st.info(
    "Feature importance indicates how strongly a feature was used "
    "by the trained Decision Tree. It does not establish causation."
)

st.subheader("📊 Model Performance")

st.dataframe(
    model_results,
    use_container_width=True,
    hide_index=True
)


# ---------------------------------------------------------
# PRIORITIZED OPERATIONAL RECOMMENDATIONS
# ---------------------------------------------------------

st.subheader("🎯 Prioritized Operational Recommendations")

recommendations = pd.read_csv(
    f"{DATA_PATH}/recommendations.csv"
)

st.dataframe(
    recommendations,
    use_container_width=True,
    hide_index=True
)

st.markdown("""
### 📌 Recommended Operational Focus

**🔴 High Priority**
- Investigate high-delay geographic route proxies.
- Review high-delay sellers and their order processing performance.

**🟡 Medium Priority**
- Review high-delay product categories.
- Improve weekend delivery capacity and scheduling.
- Plan logistics capacity for higher-delay seasons.
""")


st.divider()

st.caption(
    "Delivery Delay & Operations Analytics | Data Science Project"
)
