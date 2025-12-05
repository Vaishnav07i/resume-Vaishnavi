#int
age=25
print(age)
#string
name="Diksha"
print(name)
#float
percnt=3.99
print(percnt)
#boolean-   the first letter must be capital
age2=False
print(age)
#None the first letter must be capital
a=None
print(a)
print(type(a))
print(type(age2))
num1=5
num2=4
sum=num1+num2
diff=num2-num1
print("Num:",num1)
print("Num:",num2)
print("Sum:",sum)
print("difference:",diff)
a,b=2,3
txt="@"
print(2*txt)

A,B="cap ",3
txt1="monkey "
print((A+txt1)*B)
AA,BB="4","5" #o/p=45,as 4 nd 5 are in quotation so considered as string
sum=AA+BB
print(sum)
c,d=2,3
e=4
print(c+d*e)
f=4
g=3.5
sum3=f+g
print(sum3) #or can also be written as f+g 
z=2
y=5
x=y/z
print(x)
sup=18
duh=5
res=sup//duh #o/p=3.6
print(res)
sup=-18
duh=5
res=sup//duh #o/p= -3.6 but gives lesser value or equal value as -4 is less than -3
print(res)
sup=18
duh=-5
res=sup%duh # gives -ve o/p cause denominator is -ve
print(res)
sup=-18
duh=5
res=sup%duh #gives +ve o/p as denominator is +ve well depends on denominator
print(res)
"""hey
darling
sup""" #multi line comment
name=input("Name:")
age=int(input("Age:"))
print("hello ",name)