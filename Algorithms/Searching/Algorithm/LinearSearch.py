#Time complexity is worst= O(n)   best=O(1)
#Space complexity is O(n)


def linearSearch(data,element):
    index=-1
    for i in range(len(data)):
        if(data[i]==element):
            index=i
            return index
    else:
        return index

if __name__=="__main__":
    data=list(map(int,input("Enter data : ").split()))
    searchElement=int(input("Enter Search Data :"))
    result=linearSearch(data,searchElement)
    print("{} is not found.".format(searchElement)) if (result==-1) else print("{element} is found in index {index}".format(index=result,element=searchElement))
