#01
name = "Codelearn"
date_of_birth = 2019
print("Name: " + name)
print("Date of birth: " + str(date_of_birth))   //nối một chuỗi và một số bằng str

#02
length = 7.8
width = 3.5
print("Area: " + str(length*width))
print("Perimeter: " + str(2*(length + width))) // in diện tích và chu vi hình chữ nhật bằng cách nối chuỗi và số bằng str

#03
name = ("Hello " + input())  // nhập name từ bàn phím và in ra Hello + với name đã nhập từ bàn phím
print(name)

#04
name=input()
age=int(input())
print("In 15 years, age of " + name + " will be " + str(age+15)) //in ra tuổi của một người sau 15 năm với tên được nhập từ bàn phím

#05
a=int(input())
b=int(input())
print("a + b = " + str(a+b))
print("a - b = " + str(a-b))
print("a * b = " + str(a*b))
print("a / b = " + str(a/b))
print("a % b = " + str(a%b))   //in ra kết quả của các phép tính cơ bản với hai số nguyên a,b được nhập từ bàn phím

#06
a = int(input())
b = int(input())
a,b = b,a
print("after swap a = " + str(a) + ", b = " + str(b)) //in ra hai số a,b được nhập từ bàn phím sau khi đã hoán đổi vị trí

#07
pi=3.14
r=float(input())
print("Circumference = " + str(2*pi*r)) //in ra chu vi hình tròn với bán kính r nhập từ bán phím và số pi được gán là 3.14 

#08
a = int(input())
h = int(input())

area = (a*h)/2

print("The area of triangle is " + str(area)) // in  ra diện tích tam giác với cạnh a và chiều cao h được nhập từ bàn phím

#09
a = int(input())
b = int(input())
print(a**b) //in ra a mũ b với a,b được nhập từ bàn phím

#10
a = int(input())
Total = int(input())
Total += a # Using += Operator
print("The Value of the Total after using += Operator is:", Total)
Total -=a # Using -= Operator
print("The Value of the Total after using -= Operator is:", Total)
Total *=a # Using *= Operator
print("The Value of the Total after using *= Operator is:", Total)
Total //=a  # Using //= Operator
print("The Value of the Total after using //= Operator is:", Total)
Total **=a  # Using **= Operator
print("The Value of the Total after using **= Operator is:", Total)
Total /=a  # Using /= Operator
print("The Value of the Total after using /= Operator is:", Total)
Total %=a  # Using %= Operator
print("The Value of the Total after using %= Operator is:", Total)




