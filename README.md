
# Delivery Delay & Operations Analytics

## Project Overview

This project analyzes e-commerce delivery data to identify patterns associated with delayed orders and operational bottlenecks.

The project includes data preparation, delivery performance analysis, exploratory analysis, geographic route analysis, seller and product-category analysis, a Decision Tree delay-risk model, and an interactive Streamlit dashboard.

## Objectives

- Calculate delivery delay and on-time delivery metrics.
- Identify patterns in delayed deliveries.
- Analyze delays by seller, product category, day, season, month, and geographic route proxy.
- Identify high-delay operational hotspots.
- Build a Decision Tree model to estimate delay risk.
- Create an interactive dashboard.
- Provide prioritized operational recommendations.

## Dataset

The project uses the Brazilian E-Commerce Public Dataset by Olist.

The dataset contains information about:

- Orders
- Order items
- Products
- Sellers
- Customers
- Payments
- Reviews
- Geographic information

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Google Colab
- Git / GitHub

## Project Workflow

Raw E-Commerce Data
→ Data Loading
→ Data Cleaning
→ Delivery Date Processing
→ Delay Calculation
→ Exploratory Data Analysis
→ Seller Analysis
→ Product Category Analysis
→ Monthly / Day / Seasonal Analysis
→ Geographic Route Proxy Analysis
→ Decision Tree Model
→ Operational Recommendations
→ Streamlit Dashboard

## Delivery Delay Definition

Delivery difference is calculated as:

Actual Delivery Date - Estimated Delivery Date

Interpretation:

- Positive value = Delivered late
- Zero = Delivered on estimated date
- Negative value = Delivered early

Dashboard classification:

- Delayed = delay_days > 0
- On Time = delay_days <= 0

## Key Results

The analysis included 96,470 valid delivered orders.

| KPI | Result |
|---|---:|
| Total Orders | 96,470 |
| On-Time Orders | 89,936 |
| Delayed Orders | 6,534 |
| On-Time Delivery | 93.23% |
| Delay Rate | 6.77% |

## Exploratory Analysis

The project analyzes delivery delays across:

- Seller
- Product category
- Month
- Day of week
- Season
- Geographic route proxy

### Route Proxy

The Olist dataset does not provide explicit transportation route identifiers.

Therefore, seller-state to customer-state combinations were used as a geographic route proxy.

Example:

SP → RJ
SP → BA
SP → CE

These represent geographic combinations and should not be interpreted as confirmed transportation routes.

## Decision Tree Delay-Risk Model

A Decision Tree Classifier was developed to estimate whether an order was likely to be delayed.

### Model Features

- Purchase day of week
- Purchase month
- Purchase hour
- Estimated delivery lead time
- Number of items
- Total price
- Total freight
- Seller state
- Customer state
- Geographic route proxy

Actual delivery date and delay value were not used as input features to avoid data leakage.

### Model Performance

| Metric | Result |
|---|---:|
| Accuracy | 74.71% |
| ROC-AUC | 0.7366 |
| Delayed Precision | 15% |
| Delayed Recall | 60% |
| Delayed F1-Score | 24% |

The model identified approximately 60% of delayed orders in the test set.

Because delayed orders represent a relatively small portion of all orders, accuracy should not be considered alone. Delayed-order precision and recall are also important.

## Top Delay-Risk Factors

| Feature | Importance |
|---|---:|
| Purchase Month | 50.21% |
| Estimated Delivery Lead Time | 16.17% |
| Customer State — SP | 8.26% |
| Total Freight | 7.46% |
| Route — SP → RJ | 6.78% |
| Customer State — BA | 3.65% |
| Total Price | 2.52% |

Feature importance indicates how strongly a feature was used by the trained Decision Tree. It does not establish causation.

## Operational Recommendations

### High Priority

**Route**

Investigate geographic route proxies with substantially higher delay percentages and review logistics capacity and transit times.

**Seller**

Review high-delay sellers and investigate order processing and dispatch performance.

### Medium Priority

**Product Category**

Review handling, packaging, inventory availability, and fulfillment processes for high-delay categories.

**Day of Week**

Review weekend delivery capacity and scheduling.

**Season**

Monitor seasonal capacity and plan logistics resources during periods with higher delay rates.

## Streamlit Dashboard

The interactive dashboard contains:

- KPI cards
- Delivery status analysis
- Monthly delay trend
- Seller delay hotspots
- Route delay hotspots
- Product category analysis
- Day-of-week analysis
- Seasonal analysis
- Decision Tree model performance
- Delay-risk feature importance
- Prioritized operational recommendations

Run the dashboard with:

streamlit run dashboard/app.py

## Project Structure

Delivery-Delay-Operations-Analytics/

    data/
    notebooks/
    dashboard/
        app.py
    dashboard_data/
        kpi_summary.csv
        monthly_analysis.csv
        seller_analysis.csv
        category_analysis.csv
        day_analysis.csv
        season_analysis.csv
        delivery_status.csv
        route_analysis.csv
        recommendations.csv
        decision_tree_results.csv
        delay_risk_features.csv
    models/
    README.md
    requirements.txt
    .gitignore

## Dataset Limitations

The Olist dataset does not provide explicit warehouse identifiers or carrier identifiers.

Therefore:

- Warehouse-level analysis was not directly possible.
- Carrier-level analysis was not directly possible.
- Seller-state to customer-state combinations were used as route proxies.
- Route proxies should not be interpreted as confirmed transportation routes.

## Future Improvements

- Incorporate explicit carrier data.
- Incorporate warehouse-level information.
- Use real transportation routes.
- Test Random Forest and Gradient Boosting models.
- Perform hyperparameter tuning.
- Develop probability-based delay-risk scoring.
- Add model explainability using SHAP.
- Implement real-time delivery monitoring.
- Deploy the Streamlit dashboard.

## Project

Delivery Delay & Operations Analytics

Data Science / AI Project
