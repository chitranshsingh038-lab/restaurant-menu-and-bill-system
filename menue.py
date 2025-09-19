import time

print("THE NEW RASTURANT")
print("OUR MENUE ")


a=['drinks :','masala lassi= 50','nimbu pani=20','sada lassi=40','soya milk=50']
a3=['drinks','masala lassi','nimbu pani','sada lassi','soya milk' ]
a2=[0,50,20,40,50]                                                   # price of above items 

print(a)

    
lst1=list()

while(x:=input("order :"))!="done":
    lst1.append(x)
print(lst1)                                                         # print lst of  drinks that costumer ordered
n=len(lst1)
time.sleep(1)


b=['main corse(sabzi) :','dal makhani=50','kadhai paneer=80','sahi paneer=80','mix veg=45','tandoori chap=60']
b3=['main corse','dal makhani','kadhai paneer','sahi paneer','mix veg','tandoori chap']
b4=[0,50,80,80,45,60]                                                 #prize of above items 

print(f"\n")
print(b)


lst2=list()
while True :
    food=input("order :")
    lst2.append(food)
    if(food=="done"):
        break
lst2.pop()    
print(lst2)  
num2=len(lst2)


time.sleep(1)
print(f"\n")

c=['main corse(chapati) :','garlic butter naan=12/pc','butter naan=10/pc','tawa roti=7/pc',]
c3=['chapari','garlic butter naan','butter naan','tawa roti']
c4=[0,12,10,7]                                                        #price of above items 


print(c)

lst3=list()
while True :
    chapati=input("order :")
    lst3.append(chapati)
    if(chapati=="done"):
        break
lst3.pop()    

num=len(lst3)
chapaticounting=list()
for i in range(0,num):
    
    a=int(input (f"No of {lst3[i]} :"))
    chapaticounting.append(a)
    chapaticounting2=[int(x) for x in chapaticounting]

print(f"\n")    
lst4=list()

lst4=list()
for i in range(num):
    t=chapaticounting[i],lst3[i]
    lst4.append(t)
time.sleep(1)

print(f"your final order :\n1.{lst1}\n2.{lst2}\n3.{lst4}\n")

## bill calculation ##
t=0

time.sleep(1)

# BILL CALCULATION FOR DRINKS
for i in range(0,n):
        
    if  (lst1[i]==a3[1])   :
             t=t+50
             print(f" {a3[1]}   : 50")

    elif(lst1[i]==a3[2])   :
             t=t+20
             print(f" {a3[2]}     : 20")

    elif(lst1[i]==a3[3])   :
             t=t+40
             print(f" {a3[3]}     : 40")

    elif(lst1[i]==a3[4])   :
             t=t+50 
             print(f" {a3[4]}      : 50")
             
    else :
             print("item is not in menue" )





time.sleep(0.5)

#BILL CALCULATION FOR SABI
m=0
for x in range(0,num2)      :

    if(lst2[x]==b3[1])      :
       m=m+50
       print(" Dal makhani    : 50")

    elif (lst2[x]==b3[2])   :
       m=m+80
       print(" kadhai paneer  : 80")
    elif (lst2[x]==b3[3])   : 
       m=m+80
       print(" sahi paneer    : 80")

    elif (lst2[x]==b3[4])   :
       m=m+45
       print(" mix veg        : 45")

    elif (lst2[x]==b3[5])   :
       m=m+60
       print(" tandoori chap  : 60")
total=t+m



## bill calculation of chapati ##
num3=len(chapaticounting)
a=0
b=0
c=0
for i in range (0,num):
    if (lst3[i]==c3[1]):
        a=c4[1]*chapaticounting2[i]
        print(f" garlic butter naan: {a}")

    elif (lst3[i]==c3[2]):
        b=c4[2]*chapaticounting2[i]
        print(f" butter naan    : {b}")

    elif (lst3[i]==c3[3]):
        c=c4[3]*chapaticounting2[i]
        print(f" tawa roti      : {c}")
    else:
        print("menue is not in list")

totalbill=  a+b+c+total      

print(f"your total bill : {totalbill}")

if (totalbill==0):
     print("nikal be dalle")

else:
     print("thankyou sir to  wisit our restaurant")



















# TOTAL BILL
























































































































