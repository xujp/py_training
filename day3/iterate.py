#encoding:utf-8
aa = [2,3,4,5]

#用生成器iter将列表aa变成一个迭代器
b  = iter(aa)
print b.next()

print '****************'
for i in iter(aa):
    print i

c=[i for i in range(10)]
print c

d=[i*i for i in range(10)]
print d
print type(d)

e=(i*i for i in range(10))
print e
print type(e)
print e.next()
