import pandas as pd
data = pd.read_csv('city-list.txt', header = None)
data.columns = ["city_id", "name", "lat", "lon"]
print(data)