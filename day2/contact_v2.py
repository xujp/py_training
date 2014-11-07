#coding:utf8
import sys,string
def search():
    search=raw_input('search info:')
    if len(search)>=3:#关键字搜索必须大于3字符个以上
      times=0#记录的标记，找到一次+1，初始值为0
      #count统计若key有相同的关键字，打印keys（）若没有再遍历value。
      for k,v in contact.items():
        if k.count(search) != 0:
           times += 1
           index=k.find(search)
           l=len(search)
           print (k[:index]+"\033[1;32;10m%s\033[0m"\
           %k[index:index+l]+k[index+l:]).ljust(24),' '.join(v)
           continue
        else:    
           for i in v:
             if i.count(search) != 0:
               index=i.find(search)          #找字符串的索引位置
               l=len(search)
               index1=v.index(i)#vlaue 中的索引
               if index1==0:
                  #print  k,[]"\033[1;32;10m %s \033[0m"%search  这是设置颜色
                   print k.ljust(15),(i[:index]+"\033[1;32;10m%s\033[0m"\
                   %i[index:index+l]+i[index+l:]).ljust(30)+v[1].ljust(15)+v[2]
                   times += 1
                   break
               elif index1==1:
                   print k.ljust(15),v[0]+'\t'+(i[:index]+"\033[1;32;10m%s\033[0m"\
                   %i[index:index+l]+i[index+l:]).ljust(30)+v[2]
                   times += 1
                   break
               elif index1==2:
                   print k.ljust(15),v[0]+'\t'+v[1].ljust(17)+i[:index]+"\033[1;32;10m%s\033[0m"\
                   %i[index:index+l]+i[index+l:]
                   times += 1
                   break     
           else:continue
      print 'find %s records'% times
    else:
        print 'Search keywords that may not be less than 3 characters'
def delete(): #删除联系表
    name=raw_input('name:')
    if contact.has_key(name)==True:
        f=file('contacts.txt','w')
        f.close()
#遍历字典，如果名字不在key中，就添加到d_list 然后重写
        for i,k in contact.items():
           if i !=name:
             d_list='\t'.join([i]+k)
             with open('contacts.txt','a+') as f:
               f.writelines(d_list)
               f.write('\n')
        print "Delete contact %s succesfull!"% name
    else:
        print "No have this name %s" % name
def modify():#修改联系表
    while True:
        print "Chooes a name!Exit to return to the main page"
        name=raw_input('name:')
        list_name=contact.get(name)
        list_s=[]
        if name in contact.keys():
        #判断修改的类容，且清空老的，重写新的文件
            which=raw_input("m:mail,p:phone number,c:company!:")
            if which=='m':
              which_c=raw_input('what do you changed:')
              if len(which_c)>=5:#输入的值必须是大于5个字节的
                  f=file('contacts.txt','w')
                  f.close()
                  for k,v in contact.items():
                     if k!=name: #输入的名字遍历keys找到不等的追加到文件
                        list_s='\t'.join([k ]+v)
                        with open('contacts.txt','a+') as f:
                          f.writelines(list_s)
                          f.write('\n')
                     else:#若输入的名字在key中找到相等的则修改列表的值，追加到文件
                        v[2]=which_c
                        list_s='\t'.join([k ]+v)
                        with open ('contacts.txt','a+') as f:
                          f.writelines(list_s)
                          f.write('\n')
                  print "Modify mail successful"
                  break
              else:
                  print "Mail Please enter the correct format"
                  continue
            elif which=='p':
                which_c=raw_input('what do you changed:')
                if len(which_c)==11 and isinstance(int(which_c),int)==True:
                    for k,v in contact.items():
                      if k!=name:
                         list_s='\t'.join([k ]+v)
                         with open('contacts.txt','a+') as f:
                           f.writelines(list_s)
                           f.write('\n')
                      else:
                         v[0]=which_c
                         list_s='\t'.join([k ]+v)
                         with open ('contacts.txt','a+') as f:
                           f.writelines(list_s)
                           f.write('\n')
                    print "Modify phone successful"
                    break
                else:
                    print "Phone Please enter the correct format"
                    continue
            elif which=='c':
                which_c=raw_input('What do you changed:')
                if len(which_c)>=5:
                    for k,v in contact.items():
                      if k!=name:
                        list_s='\t'.join([k ]+v)
                        with open('contacts.txt','a+') as f:
                          f.writelines(list_s)
                          f.write('\n')
                      else:
                        v[1]=which_c
                        list_s='\t'.join([k ]+v)
                        with open ('contacts.txt','a+') as f:
                          f.writelines(list_s)
                          f.write('\n')
                    print "Modify company successful"
                    break
                else:
                    print "Company  Please enter the correct format"
                    continue
        elif name=='exit':
            break
        else:
            print "No have this name please input again!"
            continue
def add():
    while True:
        print 'Please input you want to add information Exit to return to the main page!'
        name=raw_input('name:')
        if name=='exit':
            break
        elif name not in contact.keys():#先判断名字是否存在key中，key的值只能唯一
          yx=raw_input('mail:')
          cy=raw_input('company:')
          if len(cy)>=5 and len(yx)>=5: 
            phone=raw_input('phone number:')
            if len(phone)==11 and isinstance(int(phone),int)==True:#判断输入的值是否满足格式要求
                list=[name,'\t',phone,'\t',cy,'\t',yx]
                f=file('contacts.txt','a+')
                f.writelines(list)
                f.write('\n')
                f.close()
                print '%s add succesful'%name
                break
            else:
                print "Please enter the correct format %s"%phone
                continue
          else:
              print "Please enter the correct format mail or company!" 
              continue
        else:
            print 'This account already exists!'
            continue
def help():
   info='\t'+'''     a=add
             w=modify
             d=delete
             s=search
             h=help
             q=exit'''
   print info		  
if __name__=='__main__':
    help()      #help
    while True:#Build a dictionary     
        contact={} #空字典存用户信息，name为key
        with open('contacts.txt') as f:
           for i in f.readlines():
              line=i.strip().split()
              contact[line[0]]=line[1:]
        print contact.keys()
#delete,add,search and help
        choose=raw_input("Please choose your operation(/a/d/w/s/h/q):")
        if choose=='q':    #exit the program
           sys.exit()
        elif choose=='a':      #add contacts
	   add()	
           continue
        elif choose=='d': #delete contacts
	   delete() 	 
           continue    
        elif choose=='w':      #modify content
	   modify()
           continue        
        elif choose == 's':#search keywords
           search()
        elif choose == 'h':
           help() 
        else:
           print "No have this choose"
           continue
		 
		 
		 
		 
		 
		 
		 
