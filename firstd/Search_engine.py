# This is search engine program which will search user input words in given statements of list

def matchingword(sentence1,sentence2):
    word1=sentence1.split(" ")
    word2=sentence2.split(" ")
    score=0
    for wo1 in word1:
        for wo2 in word2:
            if wo1.lower()== wo2.lower():
                score += 1
    return score

if __name__ == '__main__':

    sens=[" is sentence 1","this is sentence 2","this is sentence to this check sentence search engine"]
    query=input("Enter word to check if present in sentence: ")

    for sen in sens:
        scores=matchingword(query,sen)
        print(f'''found {scores} occurrence for "{sen}"''')





