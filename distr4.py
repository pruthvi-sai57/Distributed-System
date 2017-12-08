#!usr/bin/env python

import socket
import sys
import re

host=socket.gethostname()
UDP_PORT = 52466
BUFFER_SIZE = 1024

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',UDP_PORT))
s.listen(25)

while True:
	conn,addr = s.accept()
	file_name,addr = conn.recvfrom(1024)
	word,addr = conn.recvfrom(1024)
        count = 0
	with open(file_name) as f:
    		contents = f.read()
    		count = sum(1 for x in re.finditer(r"\b"+re.escape(word)+r"\b", contents))
		print(count)

	conn.sendto(bytes(count),(host,UDP_PORT))
	conn.close()
