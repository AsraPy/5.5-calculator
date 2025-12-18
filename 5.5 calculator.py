import math

def add(a,b):
 return a+b
def suntract(a,b):
 return a-b
def multiply(a,b):
 return a*b
def divide(a,b):
 if b == 0:
     return "تقسيم بر صفر ممکن نيست"
     return a/b

def power(a,b):
     return math. pow(a,b)
def sequare_root(a):
        if a<0:
            return "ريشه عدد منفي مجاز نيست"
        return math.sqrt(a)
    
def menu():
     print("/nماشين حساب پيشرفته")
     print("1.جمع")   
     print("2.تفريق")   
     print("3.ضرب")   
     print("4.تقسيم")   
     print("5.توان")   
     print("6.ريشه دوم")   
     print("7.خروج")
while True:
    menu()
    choice = input("يک گزينه انتخاب کنيد:")
    if choice == "7":
       print("برنامه پايان يافت")
       break
    if choice in ["1","2","3","4","5"]:
       num1 = float(input("عدد اول:"))
       num2 = float(input("عدد دوم:"))

    if choice == "1":
        print("نتيجه:",add(num1,num2))
    elif choice == "2":
         print("نتيجه:",suntract(num1,num2))
    elif choice == "3":
         print("نتيجه:",multiply(num1,num2))
    elif choice == "4":
         print("نتيجه:",divide(num1,num2))
    elif choice == "5":
         print("نتيجه:",power(num1,num2))
    elif choice == "6":
            num= float(input("عدد را وارد کنيد:"))
            print("نتيجه:",square_root(num))
    else:
            print("گزينه نامعتبر")

