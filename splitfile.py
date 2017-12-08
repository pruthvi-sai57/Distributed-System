
#!usr/bin/env python

import socket
import sys
import math
import time

start = time.time()
BUFFER_SIZE = 1024
conn1=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
conn2=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
conn3=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

distr1host = socket.gethostname()
distr1UDP_PORT= 52162
cBUFFER_SIZE = 1024

distr2host = socket.gethostname()
distr2UDP_PORT= 52262

distr3host = socket.gethostname()
distr3UDP_PORT= 52362

print("Enter the file name:")
my_file=raw_input()

print("Enter the word to be searched:")
word = raw_input()

sorting = True
hold_lines = []
with open(my_file,'r') as text_file:
    for row in text_file:
        hold_lines.append(row)
outer_count = 1
line_count = 0
i=0
while sorting:
    count = 0
    increment = (outer_count-1) *400000
    left = len(hold_lines) - increment
    file_name = "small_file_" + str(outer_count * 400000) + ".txt"
    hold_new_lines = []
    if left < 400000:
        while count < left:
            hold_new_lines.append(hold_lines[line_count])
            count += 1
            line_count += 1
        sorting = False
    else:
        while count < 400000:
            hold_new_lines.append(hold_lines[line_count])
            count += 1
            line_count += 1
    outer_count += 1
    with open(file_name,'w') as next_file:
        for row in hold_new_lines:
            next_file.write(row)
    print(file_name)
    if i==0:
    	conn1.connect(('', distr1UDP_PORT))
    	conn1.sendto(file_name,(distr1host,distr1UDP_PORT))
	conn1.sendto(word,(distr1host,distr1UDP_PORT))
    elif i==1:
        conn2.connect(('', distr2UDP_PORT))
    	conn2.sendto(file_name,(distr2host,distr2UDP_PORT))
	conn2.sendto(word,(distr2host,distr2UDP_PORT))
    elif i==2:
	conn3.connect(('', distr3UDP_PORT))
    	conn3.sendto(file_name,(distr3host,distr3UDP_PORT))
	conn3.sendto(word,(distr3host,distr3UDP_PORT))
    i=i+1
c1,addr = conn1.recvfrom(BUFFER_SIZE)
print (c1)
c2,addr = conn2.recvfrom(BUFFER_SIZE)
c3,addr = conn3.recvfrom(BUFFER_SIZE)
print (c2)
print (c3)
end = time.time()
print(end-start)
xdata=end-start
xdatastr=str(xdata)
strfile="1"+"\t"+"distrubutedsystem"+"\t"+xdatastr+"\n"
f = open("data1.dat", "a+")
f.write( str(strfile) )      # str() converts to string
f.close()




