#Code to impliment selection sort
def selection(arr1):
    n=len(arr1)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr1[j]<arr1[mini]:
                mini=j
                arr1[i],arr1[mini]=arr1[mini],arr1[i]

arr1=[24,41,33,42,17]
selection(arr1)
print("sorted array :",arr1)