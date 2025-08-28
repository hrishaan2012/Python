s1={2,1,3}
s2={"a","b","c"}
s3=list(zip(s1,s2))
print(s3)

list1=[10,20,30,40,50,60]
list2=[100,200,300,400,500,600]
for x,y in zip(list1,list2):
    print(x,y)

stocks=["Infoysis","TCS","Relience"]
prices=[1000,2000,3000]
for stock,price in zip(stocks,prices):
    print(f"{stock} : {price}")