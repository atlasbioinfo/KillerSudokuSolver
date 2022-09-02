#check if contains all rules in csv
numbers={}
for i in range(9):
    for j in range(9):
        numbers[str(i+1)+str(j+1)]=0
        tarr.append(0)

with open("./rules.csv","r") as f:
    for line in f:
        tmp=line.strip().split(",")[:-1]
        for t in tmp:
            numbers[t]+=1

for n in numbers:
    if (numbers[n]==0 or numbers[n]==2):
        print(n)
        