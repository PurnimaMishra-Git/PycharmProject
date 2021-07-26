import pickle
# pickling a python object
cars=["Audi","BMW","Lamborgini","Volkswagen"]
file="mycar.pkl"
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()

# Depickling python object

file="mycar.pkl"
fileobj=open("mycar.pkl","rb")
mycar=pickle.load(fileobj)
print(mycar)

