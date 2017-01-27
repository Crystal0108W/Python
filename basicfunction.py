#sort a given list
def selectionsort(alist):
    a = len(alist)
    while a > 0:
        high = 0
        a = a-1
        for location in range (1,a+1):
            if alist(location)>alist[high]:
                high = location
        
        temp = alist[a]
        alist[a] = alist [high]
        alist[high] = temp

alist = [43,5,65,7,689,78,2,343,878,98]
selectionsort(alist)
print(alist)

#find the nth number in a Fibonacci Sequence
def fibo(n):
    pre = 1  
    bac = 1
    while n > 2: 
        n = n-1
        temp = pre
        pre = pre + bac
        bac = temp
    return pre

print (fibo(8))
