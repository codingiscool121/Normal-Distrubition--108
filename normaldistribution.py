import plotly.express as pd
import pandas as px
import plotly.figure_factory as pf

read=px.read_csv("heightweight.csv")
height=read["Height"].tolist()
graph=pf.create_distplot([height],["Height"], show_hist=False)
print("Creating graph for height...")
graph.show()
print("Graph for height done.")

weight=read["Weight(Pounds)"]
graph2 = pf.create_distplot([weight],["Weight"], show_hist=False)
print("Opening graph....")
graph2.show()
print("Finished graph for weight")
