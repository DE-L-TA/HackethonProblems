

print("Number of Try do you want")
n=int(input())

def input_Money():
    print("Enter Your Budget")
    price=int(input())
    return price


def input_sample_price():
    arr={}
    print("Enter the list of Elementes")
    lst1 = [int(item) for item in input().split()]

    for i in range(0,9):
        arr[lst1[i]]=i+1
    return arr

for i in range(0,n):
    price=input_Money()
    arr=input_sample_price()
    c=min(arr)
    sample_output=""
    counter=0
    if c<= price:
        if c==1:
            amount=price
        else:
            amount=int(price/c)
  
        for i in range(0,amount):
             sample_output+=str(arr[c])
        if(sample_output!=""):
            print(sample_output)
    else:
        print("-1")