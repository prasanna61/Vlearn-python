org_str=input('Enter the string :')
temp_str=""
uniq_str=""
for i in org_str:
    if i not in temp_str:
        uniq_str+=i
        asc=ord(i)
    if i.isupper():
        b=chr(asc+32)
    else:
        b=chr(asc-32)
    temp_str+=i
    temp_str+=b
    
print(uniq_str)   

