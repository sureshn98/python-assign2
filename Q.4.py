#no. of uppercase and lowercase letters

str='BlaCkBErRy'
print(str)
c=0
for x in str:
    if x.isupper():
        c+=1
print('no. of uppercase letters:', c)
d=0
for y in str:
    if y.islower():
        d+=1
print('no. of lowercase letters:',d)
