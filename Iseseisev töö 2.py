results = [2, 3, 6, 6, 5]
results.sort()
repeatInt = results.count(results[-1])

while repeatInt != 1:
    results.remove(results[-1])
    repeatInt = repeatInt - 1
    
if repeatInt == 1:
    print (results[-2])
