import tab,pickle
from prettytable import PrettyTable


a = PrettyTable(['Account', 'Date', 'Type', 'Amount', 'Interest'])

dict_a = {}

with open ("account.txt") as f:
    for line in f.readlines():
        line = line.split()
        dict_a[line[0]]=line[1:]
print dict_a

with file("picklelog.log","w") as f:
    pickle.dump(dict_a,f)

with file("picklelog.log") as f:
    d=pickle.load(f)

print d

"""
a = PrettyTable(['Account', 'Date', 'Type', 'Amount', 'Interest'])
with open("credit_record.log") as f:
    n = f.readlines()
    for i in n:
        i = i.split()
        b = ' '.join(i[1:3])
        a.add_row([i[0], b, i[3], i[4], i[5]])
    print a
"""
