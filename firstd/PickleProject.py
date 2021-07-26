import requests
import pickle

# r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# a=r.text
#
# list1=a.split()
# list2= [item.split() for item in list1]
#
# with open("mypkliris.pkl","wb")as f:
#     pickle.dump(list2, f)

# To read data from pickle file
with open("mypkliris.pkl","rb")as f:
    data=pickle.load(f)
    print(data)