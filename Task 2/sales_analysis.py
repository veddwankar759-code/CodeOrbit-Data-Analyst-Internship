import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('sales_data_cleaned.xlsx')

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

print(df.info())
print(df.describe())

total_sales = df['Total_Sales'].sum()
total_orders = len(df)
total_qty = df['Quantity'].sum()
avg_order = df['Total_Sales'].mean()

print("Total Sales:", total_sales)
print("Total Orders:", total_orders)
print("Total Quantity:", total_qty)
print("Avg Order Value:", avg_order)

top_products = df.groupby('Product_Name')['Total_Sales'].sum().sort_values(ascending=False).head(5)
print(top_products)

region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print(region_sales)

cat_sales = df.groupby('Product_Category')['Total_Sales'].sum().sort_values(ascending=False)
print(cat_sales)

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
monthly = df.groupby(df['Order_Date'].dt.to_period('M'))['Total_Sales'].sum()
print(monthly)

sp = df.groupby('Salesperson').agg(
    Orders=('Order_ID', 'count'),
    Sales=('Total_Sales', 'sum')
).sort_values('Sales', ascending=False)
print(sp)

payment = df.groupby('Payment_Method')['Total_Sales'].sum().sort_values(ascending=False)
print(payment)

status = df['Order_Status'].value_counts()
print(status)

top_cust = df.groupby('Customer_Name')['Total_Sales'].sum().sort_values(ascending=False).head(5)
print(top_cust)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sales Data Analysis - 2024', fontsize=16, fontweight='bold')

region_sales.plot(kind='bar', ax=axes[0,0], color='steelblue', edgecolor='black')
axes[0,0].set_title('Sales by Region', fontweight='bold')
axes[0,0].set_ylabel('Sales (in Lakhs)')
axes[0,0].set_xlabel('Region')
axes[0,0].tick_params(axis='x', rotation=0)
axes[0,0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/100000:.0f}L'))

cat_sales.plot(kind='pie', ax=axes[0,1], autopct='%1.1f%%', startangle=90,
               colors=['#1f77b4', '#ff7f0e', '#2ca02c'])
axes[0,1].set_title('Category Share', fontweight='bold')
axes[0,1].set_ylabel('')

monthly.plot(kind='line', ax=axes[1,0], marker='o', color='green', linewidth=2)
axes[1,0].set_title('Monthly Sales Trend', fontweight='bold')
axes[1,0].set_ylabel('Sales (in Lakhs)')
axes[1,0].set_xlabel('Month')
axes[1,0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/100000:.0f}L'))
axes[1,0].grid(True, alpha=0.3)

payment.plot(kind='bar', ax=axes[1,1], color='coral', edgecolor='black')
axes[1,1].set_title('Sales by Payment Method', fontweight='bold')
axes[1,1].set_ylabel('Sales (in Lakhs)')
axes[1,1].set_xlabel('Payment Method')
axes[1,1].tick_params(axis='x', rotation=30)
axes[1,1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/100000:.0f}L'))

plt.tight_layout()
plt.savefig('sales_analysis_charts.png', dpi=150, bbox_inches='tight')
plt.show()

print("Analysis complete. Charts saved.")