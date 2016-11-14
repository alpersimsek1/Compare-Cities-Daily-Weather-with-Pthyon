from backend import Database
import plotly as py
import plotly.graph_objs as go



d = Database("cities.db")
print(d.view())
print(d.search(city_name="Amsterdam"))

x_axis=[]
x_axis=d.accessing_items_in_db("city_name")
y_axis=[]
y_axis=d.accessing_items_in_db("temperature")
z_axis=[]
z_axis=d.accessing_items_in_db("datenow")
x=[]
y=[]
z=[]
data = [
    go.Scatter(
         x=x_axis,
         y=y_axis,
         mode='markers'
            )
        ]
py.offline.plot(data, filename='basic-line.html')


