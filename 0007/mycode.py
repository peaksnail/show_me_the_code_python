#!/bin/env python
"""
only calculate the python file
"""
import os

f=[]
#open the code dir,default the the current dir
for item in os.listdir('.'):
    if item.endswith(".py"):
        f.append(item)


for item in f:
    #need_file=open("resize.py")
    need_file=open(item)
    content=(line.strip() for line in need_file.readlines())
    code_num=0
    code_conment=0
    code_black=0
    #start to find content of #,""" and black 
    first=0
    flag=0
    for line in content:
        if line.startswith('#'):
            code_conment+=1
        elif line.startswith('"""') and line.endswith('"""') and len(line)>3:    #judge comment in line
            print line
            code_conment+=1
        elif line.find('"""')>0 :
            flag=1
            code_num+=1
        elif line.startswith('"""') and flag==0:
            print line
            code_conment+=1 
            if first==0:    #start
                first=1
                continue
            if first==1:    #end
                first=0
        elif line.startswith('"""') and flag==1:
            flag=0
            code_num+=1
        elif first==1 :
            print line
            code_conment+=1
        elif line == '':
            code_black+=1
        else :
            code_num+=1
    
    
    print "file is %s,comment is %d,black is %d,code is %d" % (item ,code_conment,code_black,code_num)
    #break
