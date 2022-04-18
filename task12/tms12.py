import re
def geometric_progression(n):
       while range(n,10000):
           for i in range(n,10000):
                if i >1000:
                    break
           yield n
           n *= 2
test = geometric_progression(2)
for i in test:
    print(i)


value = input('Value: ')
email_rgx = re.compile(r'''\b([0-9A-Za-z]{1,}([0-9A-Za-z!#=?/^_`{|}~%&'*+-]{0,}[.]{0,1}
|[.]{0,1}[0-9A-Za-z!#=?/^_`{|}~%&'*+-]{0,})[0-9A-Za-z]{1,})+@([A-Za-z0-9]{1,}[A-Za-z0-9-]{0,}
[A-Za-z0-9]{1,}\.[A-Za-z0-9]{1,}[A-Za-z0-9-]{0,}[A-Za-z0-9]{1,}){0,63}\b''',re.X)
if re.fullmatch(email_rgx, value):
    print('Match.')
else:
    print("Not match")