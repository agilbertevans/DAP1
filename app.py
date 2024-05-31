import streamlit as st
import pandas as pd
import plotly.express as px
df=pd.read_csv('superstore.csv',encoding='latin1')
#st.write(df.head())
#get a list of product
product_list=df['Product Name'].unique()
total_sales_product=df[['Product Name','Sales']].groupby('Product Name').agg({'Sales':'sum'}).reset_index().sort_values(by='Sales',ascending=False)
st.dataframe(total_sales_product.head(10))
total_sales_product['Sales']=round(total_sales_product['Sales'],2)
total_sales_product=formatIndex(total_sales_product)
