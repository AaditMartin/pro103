import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
figure=px.bar(df,x="date",y="cases",color="country")
figure.show()