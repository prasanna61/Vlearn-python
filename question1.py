B_1 = "Introduction to Python Programming"
B_2 = "Python Libraries Cookbook"
B_3 = "Data Science in Python"
print(f"Book1={B_1}")
print(f"Book2={B_2}")
print(f"Book3={B_3}")
p_1 = 499.00 #price of book without GST
p_2 = 855.00
p_3 = 645.00
GST = 12 #12% of GST
D_C = 250.00
T_1 = p_1+(p_1*GST/100) #total price of Book 1 with GST
T_2 = p_2+(p_2*GST/100)
T_3 = p_3+(p_3*GST/100)
m=n=p=0
ch1=input('Do you want Book1 type yes or no : ')
if ch1=='yes':
    m=int(input('Enter the quantity of Book1: '))
ch2=input('Do you want Book2  type yes or no: ')
if ch2=='yes':
    n=int(input('Enter the quantity of Book2: '))
ch3=input('Do you want Book1 type yes or no: ')
if ch3=='yes':
    p=int(input('Enter the quantity of Book3: '))
invoice=m*T_1+n*T_2+p*T_3+D_C  #Including Delivery charges considering delivery charges same for delivering 1 book or for delivering many books at a time
#for one time delivery delivery charges=250.00
print(f'Total invoice amount={invoice}')    
