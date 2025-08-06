import pandas
import requests

url="https://fakestoreapi.com/products"
requests.get(url)
data = requests.get(url).json()
total=0

dt=pandas.DataFrame(data)[["id", "title", "price"]]
for i in data:
    total += i["price"]

print(dt)
print("\n Total price of all products:          ", total)