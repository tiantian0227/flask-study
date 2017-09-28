# coding = utf-8
import sys
import chardet


reload(sys)
sys.setdefaultencoding('utf8')
with open('C:\Users\Administrator\Desktop\qq.txt', 'rb',) as jaf:
     data = jaf.readlines()
     data_decode=data.decode('UTF-8')
     # pay = data.strip().split(',')
     for c in data:
         if c=='SUCCESS' or c=='FAILED':
             nc=c+'\n'
             print (nc)
         else:
             print (c)

print (data)
