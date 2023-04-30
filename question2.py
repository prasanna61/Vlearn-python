org_str=input('Enter the string :')
temp_str=""
uniq_str=""
for i in org_str:
    if i not in temp_str:
        asc=ord(i) #ascii value
        if i.isupper(): # if it is uppercase conert into lower case
            b=chr(asc+32)
            uniq_str+=b
        else:
            uniq_str+=i #lower case add to uniq str
            b=chr(asc-32)
    temp_str+=i #add both upper and lower cases to unq str
    temp_str+=b
    
print(uniq_str)   

