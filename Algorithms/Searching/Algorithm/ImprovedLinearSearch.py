
#time complexity
#If element found at last then O(n) to O(1)
#if element not found then O(n) to O(n/2)
def search(data,element):
    left=0
    right=len(data)-1
    index=-1
    print("Hello")
    while(left<=right):
        if data[left]==element:
            index=left
            return index
        if data[right]==element:
            index=right
            return index
        left+=1
        right-=1
    else:
        return index



if __name__=="__main__":
    data=[1,2,3,4,5,6,7,8,9,10]
    element=int(input("Enter searching elemet :"))
    result=search(data=data,element=element)

    if(result==-1):
        print("Data not found")
    else:
        print("{} is found at index {}".format(element,result))