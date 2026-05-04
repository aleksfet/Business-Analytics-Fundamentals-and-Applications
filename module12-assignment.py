# Module 12 Assignment: Business Analytics Fundamentals and Applications
# GreenGrocer Data Analysis

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Welcome message
print("=" * 60)
print("GREENGROCER BUSINESS ANALYTICS")
print("=" * 60)

# ----- USE THE FOLLOWING CODE TO CREATE SAMPLE DATA (DO NOT MODIFY) -----
# Set seed for reproducibility
np.random.seed(42)

# Store information
stores = ["Tampa", "Orlando", "Miami", "Jacksonville", "Gainesville"]
store_data = {
    "Store": stores,
    "SquareFootage": [15000, 12000, 18000, 10000, 8000],
    "StaffCount": [45, 35, 55, 30, 25],
    "YearsOpen": [5, 3, 7, 2, 1],
    "WeeklyMarketingSpend": [2500, 2000, 3000, 1800, 1500]
}

# Create store dataframe
store_df = pd.DataFrame(store_data)

# Product categories and departments
departments = ["Produce", "Dairy", "Bakery", "Grocery", "Prepared Foods"]
categories = {
    "Produce": ["Organic Vegetables", "Organic Fruits", "Fresh Herbs"],
    "Dairy": ["Milk & Cream", "Cheese", "Yogurt"],
    "Bakery": ["Bread", "Pastries", "Cakes"],
    "Grocery": ["Grains", "Canned Goods", "Snacks"],
    "Prepared Foods": ["Hot Bar", "Salad Bar", "Sandwiches"]
}

# Generate sales data for each store
sales_data = []
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

# Base performance factors for each store (relative scale)
store_performance = {
    "Tampa": 1.0, 
    "Orlando": 0.85, 
    "Miami": 1.2, 
    "Jacksonville": 0.75, 
    "Gainesville": 0.65
}

# Base performance factors for each department (relative scale)
dept_performance = {
    "Produce": 1.2,
    "Dairy": 1.0,
    "Bakery": 0.85,
    "Grocery": 0.95,
    "Prepared Foods": 1.1
}

# Generate daily sales data for each store, department, and category
for date in dates:
    # Seasonal factor (higher in summer and December)
    month = date.month
    seasonal_factor = 1.0
    if month in [6, 7, 8]:  # Summer
        seasonal_factor = 1.15
    elif month == 12:  # December
        seasonal_factor = 1.25
    elif month in [1, 2]:  # Winter
        seasonal_factor = 0.9
    
    # Day of week factor (weekends are busier)
    dow_factor = 1.3 if date.dayofweek >= 5 else 1.0  # Weekend vs weekday
    
    for store in stores:
        store_factor = store_performance[store]
        
        for dept in departments:
            dept_factor = dept_performance[dept]
            
            for category in categories[dept]:
                # Base sales amount
                base_sales = np.random.normal(loc=500, scale=100)
                
                # Calculate final sales with all factors and some randomness
                sales_amount = base_sales * store_factor * dept_factor * seasonal_factor * dow_factor
                sales_amount = sales_amount * np.random.normal(loc=1.0, scale=0.1)  # Add noise
                
                # Calculate profit margin (different base margins for departments)
                base_margin = {
                    "Produce": 0.25,
                    "Dairy": 0.22,
                    "Bakery": 0.35,
                    "Grocery": 0.20,
                    "Prepared Foods": 0.40
                }[dept]
                profit_margin = base_margin * np.random.normal(loc=1.0, scale=0.05)
                profit_margin = max(min(profit_margin, 0.5), 0.15)  # Keep within reasonable range
                
                # Calculate profit
                profit = sales_amount * profit_margin
                
                # Add record
                sales_data.append({
                    "Date": date,
                    "Store": store,
                    "Department": dept,
                    "Category": category,
                    "Sales": round(sales_amount, 2),
                    "ProfitMargin": round(profit_margin, 4),
                    "Profit": round(profit, 2)
                })

# Create sales dataframe
sales_df = pd.DataFrame(sales_data)

# Generate customer data
customer_data = []
total_customers = 5000

# Age distribution parameters
age_mean, age_std = 42, 15

# Income distribution parameters (in $1000s)
income_mean, income_std = 85, 30

# Create customer segments (will indirectly influence spending)
segments = ["Health Enthusiast", "Gourmet Cook", "Family Shopper", "Budget Organic", "Occasional Visitor"]
segment_probabilities = [0.25, 0.20, 0.30, 0.15, 0.10]

# Store preference probabilities (matches store performance somewhat)
store_probs = {
    "Tampa": 0.25,
    "Orlando": 0.20,
    "Miami": 0.30,
    "Jacksonville": 0.15,
    "Gainesville": 0.10
}

for i in range(total_customers):
    # Basic demographics
    age = int(np.random.normal(loc=age_mean, scale=age_std))
    age = max(min(age, 85), 18)  # Keep age in reasonable range
    
    gender = np.random.choice(["M", "F"], p=[0.48, 0.52])
    
    income = int(np.random.normal(loc=income_mean, scale=income_std))
    income = max(income, 20)  # Minimum income
    
    # Customer segment
    segment = np.random.choice(segments, p=segment_probabilities)
    
    # Preferred store
    preferred_store = np.random.choice(stores, p=list(store_probs.values()))
    
    # Shopping behavior - influenced by segment
    if segment == "Health Enthusiast":
        visit_frequency = np.random.randint(8, 15)  # Visits per month
        avg_basket = np.random.normal(loc=75, scale=15)
    elif segment == "Gourmet Cook":
        visit_frequency = np.random.randint(4, 10)
        avg_basket = np.random.normal(loc=120, scale=25)
    elif segment == "Family Shopper":
        visit_frequency = np.random.randint(5, 12)
        avg_basket = np.random.normal(loc=150, scale=30)
    elif segment == "Budget Organic":
        visit_frequency = np.random.randint(6, 10)
        avg_basket = np.random.normal(loc=60, scale=10)
    else:  # Occasional Visitor
        visit_frequency = np.random.randint(1, 5)
        avg_basket = np.random.normal(loc=45, scale=15)
    
    # Ensure values are reasonable
    visit_frequency = max(min(visit_frequency, 30), 1)
    avg_basket = max(avg_basket, 15)
    
    # Loyalty tier based on combination of frequency and spending
    monthly_spend = visit_frequency * avg_basket
    if monthly_spend > 1000:
        loyalty_tier = "Platinum"
    elif monthly_spend > 500:
        loyalty_tier = "Gold"
    elif monthly_spend > 200:
        loyalty_tier = "Silver"
    else:
        loyalty_tier = "Bronze"
    
    # Add to customer data
    customer_data.append({
        "CustomerID": f"C{i+1:04d}",
        "Age": age,
        "Gender": gender,
        "Income": income * 1000,  # Convert to actual income
        "Segment": segment,
        "PreferredStore": preferred_store,
        "VisitsPerMonth": visit_frequency,
        "AvgBasketSize": round(avg_basket, 2),
        "MonthlySpend": round(visit_frequency * avg_basket, 2),
        "LoyaltyTier": loyalty_tier
    })

# Create customer dataframe
customer_df = pd.DataFrame(customer_data)

# Create some calculated operational metrics for stores
operational_data = []

for store in stores:
    # Get store details
    store_row = store_df[store_df["Store"] == store].iloc[0]
    square_footage = store_row["SquareFootage"]
    staff_count = store_row["StaffCount"]
    
    # Calculate store metrics
    store_sales = sales_df[sales_df["Store"] == store]["Sales"].sum()
    store_profit = sales_df[sales_df["Store"] == store]["Profit"].sum()
    
    # Calculate derived metrics
    sales_per_sqft = store_sales / square_footage
    profit_per_sqft = store_profit / square_footage
    sales_per_staff = store_sales / staff_count
    inventory_turnover = np.random.uniform(12, 18) * store_performance[store]
    customer_satisfaction = min(5, np.random.normal(loc=4.0, scale=0.3) * 
                                (store_performance[store] ** 0.5))
    
    # Add to operational data
    operational_data.append({
        "Store": store,
        "AnnualSales": round(store_sales, 2),
        "AnnualProfit": round(store_profit, 2),
        "SalesPerSqFt": round(sales_per_sqft, 2),
        "ProfitPerSqFt": round(profit_per_sqft, 2),
        "SalesPerStaff": round(sales_per_staff, 2),
        "InventoryTurnover": round(inventory_turnover, 2),
        "CustomerSatisfaction": round(customer_satisfaction, 2)
    })

# Create operational dataframe
operational_df = pd.DataFrame(operational_data)

# Print data info
print("\nDataframes created successfully. Ready for analysis!")
print(f"Sales data shape: {sales_df.shape}")
print(f"Customer data shape: {customer_df.shape}")
print(f"Store data shape: {store_df.shape}")
print(f"Operational data shape: {operational_df.shape}")

# Print sample of each dataframe
print("\nSales Data Sample:")
print(sales_df.head(3))
print("\nCustomer Data Sample:")
print(customer_df.head(3))
print("\nStore Data Sample:")
print(store_df)
print("\nOperational Data Sample:")
print(operational_df)
# ----- END OF DATA CREATION -----


# TODO 1: Descriptive Analytics - Overview of Current Performance
# 1.1 Calculate and display basic descriptive statistics for sales and profit
# REQUIRED: Store results in variables for testing
def analyze_sales_performance():
    """
    Analyze overall sales performance with descriptive statistics
    REQUIRED: Create and return dictionary with keys:
    - 'total_sales': float
    - 'total_profit': float
    - 'avg_profit_margin': float
    - 'sales_by_store': pandas Series
    - 'sales_by_dept': pandas Series
    """
    total_sales = float(sales_df["Sales"].sum())
    total_profit = float(sales_df["Profit"].sum())
    avg_profit_margin = float(sales_df["ProfitMargin"].mean())
    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)

    print("\nSales Performance Summary:")
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Average Profit Margin: {avg_profit_margin:.2%}")
    print("\nSales by Store:")
    print(sales_by_store)
    print("\nSales by Department:")
    print(sales_by_dept)

    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "avg_profit_margin": avg_profit_margin,
        "sales_by_store": sales_by_store,
        "sales_by_dept": sales_by_dept
    }


# 1.2 Create visualizations showing sales distribution by store, department, and time
# REQUIRED: Return matplotlib figures
def visualize_sales_distribution():
    """
    Create visualizations showing how sales are distributed
    REQUIRED: Return tuple of three figures (store_fig, dept_fig, time_fig)
    """
     # Store sales figure
    store_sales = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    store_fig = plt.figure(figsize=(8, 5))
    plt.bar(store_sales.index, store_sales.values)
    plt.title("Annual Sales by Store")
    plt.xlabel("Store")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    # Department sales figure
    dept_sales = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)
    dept_fig = plt.figure(figsize=(8, 5))
    plt.bar(dept_sales.index, dept_sales.values)
    plt.title("Annual Sales by Department")
    plt.xlabel("Department")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    # Monthly sales trend figure
    monthly_sales = sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum()
    time_fig = plt.figure(figsize=(8, 5))
    plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.xticks(range(1, 13))
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    return store_fig, dept_fig, time_fig
# 1.3 Analyze customer segments and their spending patterns
# REQUIRED: Return analysis results
def analyze_customer_segments():
    """
    Analyze customer segments and their relationship to spending
    REQUIRED: Return dictionary with keys:
    - 'segment_counts': pandas Series
    - 'segment_avg_spend': pandas Series
    - 'segment_loyalty': pandas DataFrame
    """
    segment_counts = customer_df["Segment"].value_counts()
    segment_avg_spend = customer_df.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False)
    segment_loyalty = pd.crosstab(customer_df["Segment"], customer_df["LoyaltyTier"])

    print("\nCustomer Segment Counts:")
    print(segment_counts)
    print("\nAverage Monthly Spend by Segment:")
    print(segment_avg_spend)
    print("\nLoyalty Tier by Segment:")
    print(segment_loyalty)

    return {
        "segment_counts": segment_counts,
        "segment_avg_spend": segment_avg_spend,
        "segment_loyalty": segment_loyalty
    }
# TODO 2: Diagnostic Analytics - Understanding Relationships
# 2.1 Identify factors correlated with sales performance
# REQUIRED: Return correlation results
def analyze_sales_correlations():
    """
    Analyze correlations between various factors and sales performance
    REQUIRED: Return dictionary with keys:
    - 'store_correlations': pandas DataFrame
    - 'top_correlations': list of tuples (factor, correlation)
    - 'correlation_fig': matplotlib figure
    """
    store_metrics = pd.merge(store_df, operational_df, on="Store")
    store_correlations = store_metrics.drop(columns=["Store"]).corr()
    annual_sales_corr = store_correlations["AnnualSales"].drop("AnnualSales").sort_values(ascending=False)
    top_correlations = list(annual_sales_corr.items())
    correlation_fig = plt.figure(figsize=(9, 5))
    
    plt.bar(annual_sales_corr.index, annual_sales_corr.values)
    plt.title("Correlation with Annual Sales")
    plt.xlabel("Factor")
    plt.ylabel("Correlation")
    plt.xticks(rotation=45)
    plt.tight_layout()

    print("\nStore Correlation Matrix:")
    print(store_correlations)
    print("\nTop Correlations with Annual Sales:")
    for factor, value in top_correlations:
        print(f"{factor}: {value:.3f}")
    return {
        "store_correlations": store_correlations,
        "top_correlations": top_correlations,
        "correlation_fig": correlation_fig
    }
# 2.2 Compare stores based on operational metrics
# REQUIRED: Return comparison results
def compare_store_performance():
    """
    Compare stores across different operational metrics
    REQUIRED: Return dictionary with keys:
    - 'efficiency_metrics': pandas DataFrame (with SalesPerSqFt, SalesPerStaff)
    - 'performance_ranking': pandas Series (ranked by profit)
    - 'comparison_fig': matplotlib figure
    """
    efficiency_metrics = operational_df[["Store", "SalesPerSqFt", "SalesPerStaff"]].set_index("Store")
    performance_ranking = operational_df.set_index("Store")["AnnualProfit"].sort_values(ascending=False)
    comparison_fig, ax = plt.subplots(figsize=(9, 5))
    efficiency_metrics.plot(kind="bar", ax=ax)
    plt.title("Store Efficiency Comparison")
    plt.xlabel("Store")
    plt.ylabel("Value")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.title("Store Efficiency Comparison")
    plt.xlabel("Store")
    plt.ylabel("Value")
    plt.xticks(rotation=20)
    plt.tight_layout()

    print("\nEfficiency Metrics:")
    print(efficiency_metrics)
    print("\nStore Ranking by Annual Profit:")
    print(performance_ranking)

    return {
        "efficiency_metrics": efficiency_metrics,
        "performance_ranking": performance_ranking,
        "comparison_fig": comparison_fig
    }
# 2.3 Analyze seasonal patterns and their impact
# REQUIRED: Return seasonal analysis
def analyze_seasonal_patterns():
    """
    Identify and visualize seasonal patterns in sales data
    REQUIRED: Return dictionary with keys:
    - 'monthly_sales': pandas Series
    - 'dow_sales': pandas Series (day of week)
    - 'seasonal_fig': matplotlib figure
    """
    sales_copy = sales_df.copy()
    sales_copy["Month"] = sales_copy["Date"].dt.month
    sales_copy["DayOfWeek"] = sales_copy["Date"].dt.dayofweek
    monthly_sales = sales_copy.groupby("Month")["Sales"].sum()
    dow_sales = sales_copy.groupby("DayOfWeek")["Sales"].sum()
    seasonal_fig = plt.figure(figsize=(10, 5))
    plt.plot(monthly_sales.index, monthly_sales.values, marker="o", label="Monthly Sales")
    plt.title("Seasonal Sales Pattern by Month")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.xticks(range(1, 13))
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    print("\nMonthly Sales:")
    print(monthly_sales)
    print("\nDay of Week Sales:")
    print(dow_sales)

    return {
        "monthly_sales": monthly_sales,
        "dow_sales": dow_sales,
        "seasonal_fig": seasonal_fig
    }
# TODO 3: Predictive Analytics - Basic Forecasting
# 3.1 Create a simple linear regression model to predict store sales
# REQUIRED: Return model results
def predict_store_sales():
    """
    Use linear regression to predict store sales based on store characteristics
    REQUIRED: Return dictionary with keys:
    - 'coefficients': dict (feature: coefficient)
    - 'r_squared': float
    - 'predictions': pandas Series
    - 'model_fig': matplotlib figure
    """
    model_df = pd.merge(store_df, operational_df[["Store", "AnnualSales"]], on="Store")
    x = model_df["SquareFootage"]
    y = model_df["AnnualSales"]
    slope, intercept = np.polyfit(x, y, 1)
    predicted_values = intercept + slope * x
    correlation = np.corrcoef(x, y)[0, 1]
    r_squared = float(correlation ** 2)
    coefficients = {
        "SquareFootage": float(slope),
        "Intercept": float(intercept)
    }

    predictions = pd.Series(predicted_values.values, index=model_df["Store"])
    model_fig = plt.figure(figsize=(8, 5))
    plt.scatter(x, y)
    plt.plot(x, predicted_values, linestyle="--")
    plt.title("Store Sales Prediction Model")
    plt.xlabel("Square Footage")
    plt.ylabel("Annual Sales")
    plt.tight_layout()

    print("\nRegression Coefficients:")
    print(coefficients)
    print(f"R-squared: {r_squared:.4f}")
    print("\nPredicted Sales by Store:")
    print(predictions)

    return {
        "coefficients": coefficients,
        "r_squared": r_squared,
        "predictions": predictions,
        "model_fig": model_fig
    }
# 3.2 Forecast departmental sales trends
# REQUIRED: Return forecast results
def forecast_department_sales():
    """
    Analyze and forecast departmental sales trends
    REQUIRED: Return dictionary with keys:
    - 'dept_trends': pandas DataFrame
    - 'growth_rates': pandas Series
    - 'forecast_fig': matplotlib figure
    """
    sales_copy = sales_df.copy()
    sales_copy["Month"] = sales_copy["Date"].dt.month
    dept_trends = sales_copy.groupby(["Month", "Department"])["Sales"].sum().unstack()
    growth_rates = dept_trends.pct_change().mean().sort_values(ascending=False)
    forecast_fig = plt.figure(figsize=(10, 6))
    for dept in dept_trends.columns:
        plt.plot(dept_trends.index, dept_trends[dept], marker="o", label=dept)

    plt.title("Department Sales Trends by Month")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.xticks(range(1, 13))
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    print("\nDepartment Monthly Trends:")
    print(dept_trends)
    print("\nAverage Growth Rates by Department:")
    print(growth_rates)

    return {
        "dept_trends": dept_trends,
        "growth_rates": growth_rates,
        "forecast_fig": forecast_fig
    }
# TODO 4: Integrated Analysis - Business Insights and Recommendations
# 4.1 Identify the most profitable combinations of store, department, and customer segments
# REQUIRED: Return opportunity analysis
def identify_profit_opportunities():
    """
    Identify the most profitable combinations and potential opportunities
    REQUIRED: Return dictionary with keys:
    - 'top_combinations': pandas DataFrame (top 10 store-dept combinations)
    - 'underperforming': pandas DataFrame (bottom 10)
    - 'opportunity_score': pandas Series (by store)
    """
    combo_df = sales_df.groupby(["Store", "Department"])[["Sales", "Profit"]].sum().sort_values(by="Profit", ascending=False)
    top_combinations = combo_df.head(10)
    top_combinations = top_combinations.reset_index()
    underperforming = combo_df.tail(10)
    underperforming = underperforming.reset_index()
    opportunity_score = operational_df.set_index("Store")["AnnualProfit"].sort_values(ascending=False)
    
    print("\nTop Store-Department Combinations:")
    print(top_combinations)
    print("\nUnderperforming Store-Department Combinations:")
    print(underperforming)
    print("\nOpportunity Score by Store:")
    print(opportunity_score)

    return {
        "top_combinations": top_combinations,
        "underperforming": underperforming,
        "opportunity_score": opportunity_score
    }
# 4.2 Develop recommendations for improving performance
# REQUIRED: Return list of recommendations
def develop_recommendations():
    """
    Develop actionable recommendations based on the analysis
    REQUIRED: Return list of at least 5 recommendation strings
    """
    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)
    avg_spend_by_segment = customer_df.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False)
    best_store = sales_by_store.idxmax()
    weakest_store = sales_by_store.idxmin()
    top_dept = sales_by_dept.idxmax()
    top_segment = avg_spend_by_segment.idxmax()
    recommendations = [
        f"Invest more marketing and inventory support in {best_store} because it is the top-performing store.",
        f"Create an improvement plan for {weakest_store} since it has the lowest total sales.",
        f"Focus on expanding {top_dept} because it generates the strongest sales performance.",
        f"Target the {top_segment} segment with promotions because they spend the most per month on average.",
        "Increase staffing and inventory planning during summer and December since sales are stronger in those periods."
    ]

    print("\nRecommendations:")
    for i, recommendation in enumerate(recommendations, start=1):
        print(f"{i}. {recommendation}")
    return recommendations
# TODO 5: Summary Report
# REQUIRED: Generate comprehensive summary
def generate_executive_summary():
    """
    Generate an executive summary of key findings and recommendations
    REQUIRED: Print executive summary with sections:
    - Overview (1 paragraph)
    - Key Findings (3-5 bullet points)
    - Recommendations (3-5 bullet points)
    - Expected Impact (1 paragraph)
    """
    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)
    avg_spend_by_segment = customer_df.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False)
    monthly_sales = sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum()
    best_store = sales_by_store.idxmax()
    best_department = sales_by_dept.idxmax()
    best_segment = avg_spend_by_segment.idxmax()
    best_month = monthly_sales.idxmax()

    print("Overview:")
    print("This analysis reviewed GreenGrocer's sales, customer, and store operations data to understand current performance, explain major patterns, and support future decision-making. The results show clear differences between stores, departments, and customer groups, which can help management focus on the strongest opportunities for growth.")
    print("\nKey Findings:")
    print(f"- {best_store} generated the highest total annual sales.")
    print(f"- {best_department} was the strongest department based on total sales.")
    print(f"- {best_segment} customers had the highest average monthly spend.")
    print(f"- Month {best_month} had the highest sales total, showing a strong seasonal effect.")
    print("- Store size and sales showed a positive relationship in the regression model.")
    print("\nRecommendations:")
    print(f"- Continue investing in high-performing stores like {best_store}.")
    print(f"- Improve weaker store performance with targeted support and local marketing.")
    print(f"- Expand or promote the {best_department} department more aggressively.")
    print(f"- Build special offers around the {best_segment} customer segment.")
    print("- Prepare for peak months with stronger inventory and staffing plans.")
    print("\nExpected Impact:")
    print("If GreenGrocer uses these findings to guide store operations, customer targeting, and resource allocation, the company could improve sales efficiency, increase profitability, and make better decisions about future growth. Even simple descriptive and predictive analysis can help management focus on the parts of the business with the greatest return.")
# Main function to execute all analyses
# REQUIRED: Do not modify function name
def main():
    print("\n" + "=" * 60)
    print("GREENGROCER BUSINESS ANALYTICS RESULTS")
    print("=" * 60)
    
    # Execute analyses in a logical order
    # REQUIRED: Store all results for potential testing
    
    print("\n--- DESCRIPTIVE ANALYTICS: CURRENT PERFORMANCE ---")
    sales_metrics = analyze_sales_performance()
    dist_figs = visualize_sales_distribution()
    customer_analysis = analyze_customer_segments()
    
    print("\n--- DIAGNOSTIC ANALYTICS: UNDERSTANDING RELATIONSHIPS ---")
    correlations = analyze_sales_correlations()
    store_comparison = compare_store_performance()
    seasonality = analyze_seasonal_patterns()
    
    print("\n--- PREDICTIVE ANALYTICS: FORECASTING ---")
    sales_model = predict_store_sales()
    dept_forecast = forecast_department_sales()
    
    print("\n--- BUSINESS INSIGHTS AND RECOMMENDATIONS ---")
    opportunities = identify_profit_opportunities()
    recommendations = develop_recommendations()
    
    print("\n--- EXECUTIVE SUMMARY ---")
    generate_executive_summary()
    
    # Show all figures
    plt.show()
    
    # Return results for testing purposes
    return {
        'sales_metrics': sales_metrics,
        'customer_analysis': customer_analysis,
        'correlations': correlations,
        'store_comparison': store_comparison,
        'seasonality': seasonality,
        'sales_model': sales_model,
        'dept_forecast': dept_forecast,
        'opportunities': opportunities,
        'recommendations': recommendations
    }

# Run the main function
if __name__ == "__main__":
    results = main()