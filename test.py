twoDArray = [[],[]]

count = 0
for i in range(len(twoDArray)):
    for j in range(5):
        twoDArray[i].append(count)
        count+=1

for i in twoDArray:
    for j in i:
        print(j, end=" ")
    print()