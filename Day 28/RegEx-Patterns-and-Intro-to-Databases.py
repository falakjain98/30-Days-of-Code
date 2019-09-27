import string
n = int(input())
name=[]
for i in range(n):
    inp = str(input()).split(' ')
    person = inp[0]
    email = inp[1]
    if '@gmail.com' in email:
        name.append(person)
name.sort()
for i in name:
    print (i)
