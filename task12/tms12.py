import re
def geometric_progression(n):
   while True:
       yield n
       n *= 2
test = geometric_progression(1)
for i in test:
    if i > 10000:
        break
    print(i)


value = input('Value: ')
email_rgx = re.compile(r'''\b([0-9A-Za-z]{1,}([0-9A-Za-z!#=?/^_`{|}~%&'*+-]{0,}[.]{0,1}
|[.]{0,1}[0-9A-Za-z!#=?/^_`{|}~%&'*+-]{0,})[0-9A-Za-z]{1,})+@([A-Za-z0-9]{1,}[A-Za-z0-9-]{0,}
[A-Za-z0-9]{1,}\.[A-Za-z0-9]{1,}[A-Za-z0-9-]{0,}[A-Za-z0-9]{1,}){0,63}\b''',re.X)
if re.fullmatch(email_rgx, value):
    print('Match.')
else:
    print("Not match")