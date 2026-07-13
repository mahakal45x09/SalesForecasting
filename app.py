import streamlit as st
import pandas as pd
import plotly.express as px
import os


st.set_page_config(
    page_title="AI Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main{
    background-color:#F8F9FA;
}

h1{
    color:#1F4E79;
}

div[data-testid="metric-container"]{
    background-color:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

.sidebar .sidebar-content{
    background-color:#F4F6F8;
}

</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():

    df = pd.read_csv("train.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    return df


df = load_data()


st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2933/2933245.png",
    width=90
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(

    "Go To",

    [

        "🏠 Home",

        "📊 Sales Analysis",

        "📦 Category Analysis",

        "🌍 Region Analysis",

        "📈 Forecasting",

        "📑 Model Comparison",

        "💼 Business Insights",

        "ℹ About Project"

    ]

)

st.sidebar.markdown("---")

st.sidebar.info(
    "AI Sales Forecasting Dashboard\n\n"
    "Developed using Python, Streamlit, Prophet and XGBoost."
)

if page == "🏠 Home":

    st.title("📈 AI Sales Forecasting Dashboard")

    st.write(
        """
        Welcome to the AI-powered Sales Forecasting Dashboard.

        This dashboard provides:

        ✔ Sales Analysis

        ✔ Category Analysis

        ✔ Regional Analysis

        ✔ Sales Forecasting

        ✔ Business Insights
        """
    )

    st.markdown("---")

   

    total_sales = df["Sales"].sum()

    total_orders = len(df)

    avg_sales = df["Sales"].mean()

    total_categories = df["Category"].nunique()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "💰 Total Sales",
        f"${total_sales:,.0f}"
    )

    c2.metric(
        "📦 Orders",
        f"{total_orders:,}"
    )

    c3.metric(
        "📂 Categories",
        total_categories
    )

    c4.metric(
        "💵 Average Sale",
        f"${avg_sales:.2f}"
    )

    st.markdown("---")


    monthly_sales = (

        df.groupby(

            pd.Grouper(

                key="Order Date",

                freq="ME"

            )

        )["Sales"]

        .sum()

        .reset_index()

    )

    fig = px.line(

        monthly_sales,

        x="Order Date",

        y="Sales",

        title="Monthly Sales Trend",

        markers=True

    )

    fig.update_layout(

        template="plotly_white",

        height=500

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")


    st.subheader("Dataset Preview")

    st.dataframe(df.head(10))

    st.markdown("---")

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write("Rows :", df.shape[0])

        st.write("Columns :", df.shape[1])

    with col2:

        st.write("Missing Values")

        st.write(df.isnull().sum())



elif page == "📊 Sales Analysis":

    st.title("📊 Sales Analysis Dashboard")

    st.markdown("Analyze sales trends using interactive charts.")

    st.markdown("---")


    min_date = df["Order Date"].min()
    max_date = df["Order Date"].max()

    start_date, end_date = st.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    filtered_df = df[
        (df["Order Date"] >= pd.to_datetime(start_date)) &
        (df["Order Date"] <= pd.to_datetime(end_date))
    ]


    total_sales = filtered_df["Sales"].sum()
    avg_sales = filtered_df["Sales"].mean()
    total_orders = len(filtered_df)

    c1, c2, c3 = st.columns(3)

    c1.metric("💰 Total Sales", f"${total_sales:,.0f}")
    c2.metric("📦 Orders", total_orders)
    c3.metric("💵 Average Sale", f"${avg_sales:.2f}")

    st.markdown("---")


    monthly = (
        filtered_df
        .groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="Order Date",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)


    filtered_df["Year"] = filtered_df["Order Date"].dt.year

    yearly = (
        filtered_df
        .groupby("Year")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        yearly,
        x="Year",
        y="Sales",
        color="Sales",
        title="Year-wise Sales"
    )

    st.plotly_chart(fig, use_container_width=True)


    filtered_df["Month"] = filtered_df["Order Date"].dt.month_name()

    month_order = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    month_sales = (
        filtered_df
        .groupby("Month")["Sales"]
        .sum()
        .reindex(month_order)
        .reset_index()
    )

    fig = px.bar(
        month_sales,
        x="Month",
        y="Sales",
        color="Sales",
        title="Month-wise Sales"
    )

    st.plotly_chart(fig, use_container_width=True)

   

    fig = px.histogram(
        filtered_df,
        x="Sales",
        nbins=40,
        title="Sales Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


    fig = px.box(
        filtered_df,
        y="Sales",
        title="Sales Box Plot"
    )

    st.plotly_chart(fig, use_container_width=True)


    if "Customer Name" in filtered_df.columns:

        st.subheader("🏆 Top 10 Customers")

        top_customers = (
            filtered_df
            .groupby("Customer Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            top_customers,
            x="Customer Name",
            y="Sales",
            color="Sales"
        )

        st.plotly_chart(fig, use_container_width=True)

  
    if "Product Name" in filtered_df.columns:

        st.subheader("🏆 Top 10 Products")

        top_products = (
            filtered_df
            .groupby("Product Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            top_products,
            x="Product Name",
            y="Sales",
            color="Sales"
        )

        st.plotly_chart(fig, use_container_width=True)


    st.markdown("---")

    csv = filtered_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Filtered Sales Data",
        data=csv,
        file_name="filtered_sales.csv",
        mime="text/csv"
    )


elif page == "📦 Category Analysis":

    st.title("📦 Category Analysis")

    st.markdown("Analyze sales by Category and Sub-Category")

    st.markdown("---")

   

    category = pd.read_csv("outputs/category_sales.csv")

    fig = px.bar(
        category,
        x="Category",
        y="Sales",
        color="Category",
        text_auto=".2s",
        title="Category-wise Sales"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    subcategory = pd.read_csv("outputs/subcategory_sales.csv")

    fig = px.bar(
        subcategory,
        x="Sub-Category",
        y="Sales",
        color="Sales",
        text_auto=".2s",
        title="Top Sub-Category Sales"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

 
    fig = px.pie(
        category,
        names="Category",
        values="Sales",
        hole=0.4,
        title="Category Contribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("Category Sales Table")

    st.dataframe(category)

    csv = category.to_csv(index=False)

    st.download_button(
        "📥 Download Category Report",
        csv,
        "category_sales.csv",
        "text/csv"
    )


elif page == "🌍 Region Analysis":

    st.title("🌍 Region Analysis")

    st.markdown("Analyze sales across different regions.")

    st.markdown("---")

    region = pd.read_csv("outputs/region_sales.csv")

    fig = px.bar(
        region,
        x="Region",
        y="Sales",
        color="Region",
        text_auto=".2s",
        title="Region-wise Sales"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    fig = px.pie(
        region,
        names="Region",
        values="Sales",
        hole=0.4,
        title="Regional Sales Contribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("Region Sales Table")

    st.dataframe(region)

    csv = region.to_csv(index=False)

    st.download_button(
        "📥 Download Region Report",
        csv,
        "region_sales.csv",
        "text/csv"
    )


elif page == "📈 Forecasting":

    st.title("📈 Sales Forecasting")

    st.markdown("""
This page shows sales forecasting results using:

- SARIMA
- Prophet
- XGBoost
""")

    st.markdown("---")

  

    st.header("📉 SARIMA Forecast")

    if os.path.exists("charts/task3_sarima.png"):

        st.image(
            "charts/task3_sarima.png",
            use_container_width=True
        )

    else:

        st.warning("SARIMA chart not found.")

    st.markdown("---")


    st.header("🔮 Prophet Forecast")

    if os.path.exists("outputs/prophet_forecast.csv"):

        prophet = pd.read_csv(
            "outputs/prophet_forecast.csv"
        )

        st.dataframe(prophet.head())

        if "ds" in prophet.columns and "yhat" in prophet.columns:

            fig = px.line(
                prophet,
                x="ds",
                y="yhat",
                title="Prophet Forecast"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.download_button(
            "📥 Download Prophet Forecast",
            prophet.to_csv(index=False),
            "prophet_forecast.csv",
            "text/csv"
        )

    else:

        st.warning("Prophet forecast file not found.")

    st.markdown("---")


    st.header("🚀 XGBoost Forecast")

    if os.path.exists("charts/task3_xgboost_forecast.png"):

        st.image(
            "charts/task3_xgboost_forecast.png",
            use_container_width=True
        )

    else:

        st.warning("XGBoost chart not found.")

    st.markdown("---")



    st.subheader("Saved Machine Learning Model")

    if os.path.exists("outputs/best_xgboost_model.pkl"):

        st.success("✔ Best XGBoost Model Saved Successfully")

    else:

        st.error("Model file not found.")

    st.markdown("---")

    st.info("""
Forecast Summary

✔ SARIMA captures seasonal patterns.

✔ Prophet predicts future monthly sales.

✔ XGBoost learns nonlinear relationships.

These models help estimate future business demand.
""")

elif page == "📑 Model Comparison":

    st.title("📑 Model Comparison")

    st.markdown("""
Compare forecasting models using evaluation metrics.

Evaluation Metrics:

✔ MAE (Mean Absolute Error)

✔ RMSE (Root Mean Squared Error)

✔ MAPE (Mean Absolute Percentage Error)
""")

    st.markdown("---")

    if os.path.exists("outputs/model_comparison.csv"):

        comparison = pd.read_csv("outputs/model_comparison.csv")

        st.subheader("Model Performance")

        st.dataframe(comparison, use_container_width=True)

        st.markdown("---")

     

        best = comparison.loc[
            comparison["RMSE"].idxmin()
        ]

        st.success(
            f"🏆 Best Model : {best['Model']}"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "MAE",
            f"{best['MAE']:.2f}"
        )

        c2.metric(
            "RMSE",
            f"{best['RMSE']:.2f}"
        )

        c3.metric(
            "MAPE",
            f"{best['MAPE']:.2f}%"
        )

        st.markdown("---")


        fig = px.bar(
            comparison,
            x="Model",
            y="RMSE",
            color="Model",
            text_auto=".2f",
            title="RMSE Comparison"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

     

        fig = px.bar(
            comparison,
            x="Model",
            y="MAE",
            color="Model",
            text_auto=".2f",
            title="MAE Comparison"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

      

        fig = px.bar(
            comparison,
            x="Model",
            y="MAPE",
            color="Model",
            text_auto=".2f",
            title="MAPE Comparison"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")


        radar = comparison.melt(
            id_vars="Model",
            var_name="Metric",
            value_name="Value"
        )

        fig = px.line_polar(
            radar,
            r="Value",
            theta="Metric",
            color="Model",
            line_close=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

      

        st.download_button(
            label="📥 Download Model Comparison",
            data=comparison.to_csv(index=False),
            file_name="model_comparison.csv",
            mime="text/csv"
        )

    else:

        st.error("model_comparison.csv not found in outputs folder.")
 

elif page == "💼 Business Insights":

    st.title("💼 Business Insights")

    st.markdown("""
The following insights are generated from the historical sales analysis
and forecasting models.
    """)

    st.markdown("---")

 

    category = pd.read_csv("outputs/category_sales.csv")
    top_category = category.loc[category["Sales"].idxmax()]

    st.success(
        f"🏆 Highest Sales Category : {top_category['Category']}"
    )


    region = pd.read_csv("outputs/region_sales.csv")
    top_region = region.loc[region["Sales"].idxmax()]

    st.success(
        f"🌍 Best Performing Region : {top_region['Region']}"
    )

    

    comparison = pd.read_csv("outputs/model_comparison.csv")
    best_model = comparison.loc[
        comparison["RMSE"].idxmin()
    ]

    st.success(
        f"🤖 Best Forecasting Model : {best_model['Model']}"
    )

    st.markdown("---")

    st.subheader("Key Recommendations")

    st.write("✔ Increase inventory for high-demand categories.")

    st.write("✔ Focus marketing campaigns in top-performing regions.")

    st.write("✔ Use the selected forecasting model for future sales planning.")

    st.write("✔ Monitor seasonal trends to improve demand planning.")

    st.write("✔ Update forecasting models regularly with new sales data.")

    st.markdown("---")

    st.subheader("Business Summary")

    st.info("""
• Technology products contribute the highest revenue.

• West region records the maximum sales.

• XGBoost provides the lowest forecasting error.

• Monthly forecasting helps optimize inventory planning.

• Data-driven decisions improve business performance.
    """)



elif page == "ℹ About Project":

    st.title("ℹ AI Sales Forecasting Project")

    st.markdown("---")

    st.subheader("Project Objective")

    st.write("""
This project predicts future sales using Machine Learning
and Time Series Forecasting techniques.

The dashboard enables businesses to monitor historical
sales performance and estimate future demand.
""")

    st.markdown("---")

    st.subheader("Technologies Used")

    tech = [
        "Python",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Plotly",
        "Streamlit",
        "Scikit-Learn",
        "XGBoost",
        "Prophet",
        "Statsmodels"
    ]

    for t in tech:
        st.write("✔", t)

    st.markdown("---")

    st.subheader("Forecasting Models")

    st.write("✔ SARIMA")

    st.write("✔ Prophet")

    st.write("✔ XGBoost")

    st.markdown("---")

    st.subheader("Project Features")

    st.write("✔ Sales Dashboard")

    st.write("✔ Forecasting Dashboard")

    st.write("✔ Business Insights")

    st.write("✔ Interactive Charts")

    st.write("✔ Download Reports")

    st.markdown("---")

    st.subheader("Developer")

    st.write("Ketan Mahakal")

    st.write("B.E. Information Technology")

    st.write("L.D. College of Engineering")

    st.write("Ahmedabad, Gujarat")

    st.markdown("---")

    st.success("AI Sales Forecasting Dashboard Completed Successfully ")



st.markdown("---")

st.caption(
    "© 2026 Ketan Mahakal | AI Sales Forecasting Dashboard | Built with Streamlit"
)