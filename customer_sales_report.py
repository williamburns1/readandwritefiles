import pandas as p
sales = p.read_csv('sales.csv')
sales_report = sales.assign(Total = sales['SubTotal'] + sales['TaxAmt'] + sales['Freight']).groupby('CustomerID').agg({'Total':'sum'})
sales_report.to_csv('salesreport.csv')