'''
You are given few sentence as a list(python list of sentences)take a query string as a input from the user you have to pullout the sentences
matching out of query inputed by user in decresing order of relevence after converting every query and sentences to lower case
most relevent word is the maximum number of matching of word from the query
'''



def matchingword(sentence1,sentence2):
    word1=sentence1.split(" ")
    word2=sentence2.split(" ")
    score=0
    for word1 in word1:
        for word2 in word2:
            if word1.lower()==word2.lower():
                score=score+1
    return score

if __name__ == '__main__':
    sen1 = ["this is good", "Python is good", " python is in sentence like python"]
    query = input("Enter query string:")
    scores=[matchingword(query,sen) for sen in sen1]

    sortedsentscore=[sentscore for sentscore in sorted(zip(scores,sen1),reverse=True)]
    print(sortedsentscore)

    for score,item in sortedsentscore:
        print(f"{item} with a score of {score}")