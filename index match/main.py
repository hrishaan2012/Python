def matchwords (words):
    ctr=0
    list=[]
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            list.append(word)

    print("Number of words with same first and last letter:", ctr,list)
    return ctr

count = matchwords(["hello", "world", "level", "radar", "python", "civic"])
print("Words with same first and last letter:", count)