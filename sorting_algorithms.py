def viewArr(n, arr):
    if n > len(arr):
        print("index out of bounds")
    else:
        i = len(arr)-n
        if i<len(arr):
            print(arr[i], end=" ")
            viewArr(n-1, arr)

def viewArrReverse(n, arr):
    if n > len(arr):
        print("index out of bounds")
    else:
        if n>0:
            print(arr[n-1], end=" ")
            viewArrReverse(n-1, arr)

def find_max(arr, n):
    if n > 0 and n<=len(arr):
        if n == 1:
            return arr[0]
        
        prev_max = find_max(arr, n - 1)
        
        if arr[n-1] > prev_max:
            return arr[n-1]
        else:
            return prev_max
    else:
        print("out of bounds")

def nbOfDigit(n):
    n = abs(n)

    if n < 10:
        return 1
    else:
        return 1 + nbOfDigit(n//10)

def searchK(n, k, arr):
    if n>0:
        if k == arr[n-1]:
            return True
        else:
            searchK(n-1, k, arr)
    
    return False

def searchK(arr, n, key):
    if n>=0 and n<=len(arr):
        if n == 0:
            return False  
        
        current_element = arr[n-1]
        if current_element == key:
            return True  
        
        return searchK(arr, n-1, key)
    else: 
        print("out of bounds")

def prime(n):
    i = 1
    factorCount = 0
    while i <= n:
        if n % i == 0:
            factorCount+=1

        i+=1
    
    if factorCount > 2:
        return False
    else: return True

def sameFactor(n, k):
    if n>k:
        biggest = n
    else: biggest = k

    for i in range(1,biggest+1):
        if ((n%i==0) and (k%i==0)) and i != 1 and i != n and i != k:
            print(i, end=" ")

def smallestSameFactor(n, k):
    if n>k:
        biggest = n
    else: biggest = k

    i = 1
    while i<biggest+1:
        if ((n%i==0) and (k%i==0)) and i != 1 and i != n and i != k:
            return i

        i+=1

def numOfDigit(n):
    if n < 0:
        n*=-1

    count = 0
    while n>0:
        count+=1
        n=n//10
    return count

def numOfUniqDigit(n):
    lookUpTable = [0,0,0,0,0,0,0,0,0,0]

    if n < 0:
        n*=-1
    if n == 0:
        return 1

    count = 0
    while n>0:
        index = n%10
        if lookUpTable[index] == 0:
            count+=1
            lookUpTable[index]+=1
        n=n//10
    return count
