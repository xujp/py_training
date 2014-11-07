import tab,re

p = re.compile(r'hello')

print p.match('hello world')

m = p.match('hello world')

if m : 
     print m.group()

p = re.compile('\d')
print p.findall('hddkdk3kdk3k399ls')

p = re.compile('\d+')
print p.split('kdkkd77llsk97lloo3pp')
print p.findall('kdkkd77llsk97lloo3pp')

print re.sub('[abc]','o','mark')
print re.sub('\d','o','7783838')
