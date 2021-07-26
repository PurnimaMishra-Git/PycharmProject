import json

data='{"id":"1","name":"mira","hobbies":["reading","jog"]}'
print(data)

r=json.loads(data)
print(r)
s=r['hobbies']
print(s[0])

data2={"channel name":"codewith","cars":['bmw','audi','arteron'],"frige":('roti','rice'),"isbad":False}

to_convert_json_formate=json.dumps(data2)
print(to_convert_json_formate)

x = {
      "id":1, "Name":"Shipla","School":"High","STD":5,
"isbad":False
}

# sort the result alphabetically by keys:
a=json.dumps(x,sort_keys=False)
print(a)
