# How to find square root of a large number in O(logn) time.
#OR
# Python3 implementation to find
# square root of given number
# upto given precision using
# binary search.

def search(element,precesion):
    start=0
    end=element
    ans=0

    #Finding integral part of root
    while start<=end:
        mid=int((start+end)/2)
        if mid*mid==element:
            ans=mid
            break
        elif mid*mid<element:
            start=mid+1
        else:
            end=mid-1

    #Finding fractional part of root
    increment=.1

    for i in range(0,precesion):
        while ans*ans<=element:
            ans+=increment
        ans-=increment
        increment/=10
    return ans



if __name__=="__main__":
    element=int(input("Enter Element to find root :"))
    result=search(element,4)
    print("Root is ",round(result,4))