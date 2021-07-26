import requests

r=requests.get("https://newsapi.org/v2/everything?q=tesla&from=2021-04-26&sortBy=publishedAt&apiKey=c465f7fbde114936bc54e6db79ce4786")
print(type(r))
print(r.text)
print(type(r.text))
print(r.status_code)
print(r.headers["content-type"])
print(r.encoding)
print(r.json())
print(r.history)


# url="www.somthing.com"
# data={"p1":1,"p2":2}
#
# r2=requests.post(url=url,data=data)