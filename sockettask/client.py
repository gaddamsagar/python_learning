import socket
import sys
s=""
try:
	host = socket.gethostname()
	port = 8889
	s = socket.socket()
	s.connect((host,port))
	ack = s.recv(1024)
	print ack

except Exception as err:
	print err

finally:
	if s:
		s.close()