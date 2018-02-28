
''' читаем файл и регулярные выражения '''  
 
#with open (r'first.py','r') as f:
#    print(f.read())
#f.close()
s='jjjkkkk'
i = s.find('k')



print i

import os, sys
def getlocaldata(sms,dr,flst):
   for f in flst:
    
      fullf = os.path.join(dr,f)
      if os.path.islink(fullf): continue # don't count linked files
      if os.path.isfile(fullf):
          sms[0] += os.path.getsize(fullf)
          sms[1] += 1
      else:
          sms[2] += 1
def dtstat(dtroot):
   sums = [0,0,1] # 0 bytes, 0 files, 1 directory so far
   os.path.walk(dtroot,getlocaldata,sums)

   return sums
 
report = dtstat('.')
print report
