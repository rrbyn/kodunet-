sampleText = ("Kuressaare Ametikool")
lettersDict = dict()
lettersDictSorted = dict()

for x in sampleText.lower().replace(" ", ""):
    if x not in lettersDict:
        lettersDict[x] = 1
    else:
        lettersDict[x] = lettersDict[x] + 1

lettersDictSorted = {k: lettersDict[k] for k in sorted(lettersDict)}

print (lettersDictSorted)  