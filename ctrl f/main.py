test={"codingal":2,"is":2,"best":2,"platform":2,"for":2,"learning":2,"python":2,"and":2,"coding":2}
print("The frequency is", test )
k=2
result=0
for key, value in test.items():
    if value == k:
        result += 1
print(result)
