'''
s="car"
print(s)
s='b'+s[1:3]
print(s)
'''

'''
orm=input("ormandasin saga mi gitmek istersin sola mi?")
a=0
while orm=="sag":
    a=a+1
    print("dostum yanlis yon",a,".defa yanlis yone gidiyon")
    if(a==3):
        print(a,". defa yanlis yone donuyon malsin")
    orm=input("ormandasin saga mi gitmek istersin sola mi?2")
print("helal olsun")    
'''

print("Enter your name")
name=input()
print("enter a number")
number=input()
sumevennum=0
for i in range(len(number)):
    b=i+1
    k=int(number[i])
    if k%2==0:
        print(k,"is your",b,"th number and it is an even number")
        sumevennum=k+sumevennum
print(sumevennum,"is the sum of even numbers in your number dear",name)





