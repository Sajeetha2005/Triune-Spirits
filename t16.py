import csv
from datetime import datetime
import matplotlib.pyplot as plt

def aggregate_sales(file_path):
    sales_by_product = {}
    sales_by_month = {}
    
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row['product']
            amount = float(row['amount'])
            date = datetime.strptime(row['date'], "%Y-%m-%d")
            month = date.strftime("%Y-%m")   
            
            sales_by_product[product] = sales_by_product.get(product, 0) + amount
            sales_by_month[month] = sales_by_month.get(month, 0) + amount

    plt.figure(figsize=(6,4))
    plt.bar(sales_by_product.keys(), sales_by_product.values(), color='skyblue')
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales Amount")
    plt.savefig("sales_by_product.png")
    plt.close()
    
    plt.figure(figsize=(6,4))
    plt.bar(sales_by_month.keys(), sales_by_month.values(), color='lightgreen')
    plt.title("Total Sales by Month")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount")
    plt.savefig("sales_by_month.png")
    plt.close()
    
    return {"by_product": sales_by_product, "by_month": sales_by_month}
    
if __name__ == "__main__":
    summary = aggregate_sales("sales.csv")
    print("Sales Summary:", summary)

