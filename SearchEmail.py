import re

fhandle = open('C:\\Users\\Buser\\Documents\\sample.txt', 'r')

emails = []

for line in fhandle:
    m = re.search('(\w+[.|\w])*@(\w+[.|\w])*',line)
    emails.append(m.group(0))


for i in range(0, len(emails)):
    print(emails[i])
print('done with re.search() \n')


for line in fhandle:
    m = re.finditr('(\w+[.|\w])*@(\w+[.|\w])*',line)
    emails.append(m.group(0))

for i in range(0, len(emails)):
    print(emails[i])
print('done with re.finditr()')
    
fhandle.close()

