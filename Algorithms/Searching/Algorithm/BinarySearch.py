#Time complexity of this is O(logn)

def binarySearch(data,element):
    left=0
    right=len(data)-1
    while left<=right:
        mid=(left+right)//2
        if data[mid]==element:
            return mid
        elif data[mid]<element:
            left=mid+1
        else:
            right=mid-1
    else:
        return -1


if __name__=="__main__":
    data=[1,2,3,4,5,6,7,8,9,10]
    element=int(input("Enter search Element :"))
    result=binarySearch(data,element)
    if(result==-1):
        print("Data not found")
    else:
        print("Data found at index {}".format(result))