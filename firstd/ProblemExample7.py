'''
You are given few sentence as a list(python list of sentences)take a query string as a input from the user you have to pullout the sentences
matching out of query inputed by user in decresing order of relevence after converting every query and sentences to lower case
most relevent word is the maximum number of matching of word from the query
'''
import math

def count_word(*query_str1):
    while True:
        for word in query_str:
            return f"{word}:{query_str1.count(word)}"


if __name__ == '__main__':
    list1 = ["this is good", "Python is good", " python is in sentence like python"]
    query=input("Enter query string:")
    list2 = " ".join(list1).lower()
    query_str =list2.split()
    new_str=set(query_str)
    sorted_by_alpha=sorted(new_str)

    for query in list1:
        for query in query_str:
            if list1.query == query_str.query1:
                print(list1)


    for word in sorted_by_alpha:
        # print(f"{word}:{query_str.count(word)}")
        c=zip({word},{query_str.count(word)})
        d=dict(c)
        for key,value in d.items():
            print(key,value)














# sort by decresing order
# max count of word uska statement print karvana h
#
