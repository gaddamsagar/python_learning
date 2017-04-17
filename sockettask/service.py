import socket
try:
	host = socket.gethostname()
	port = 8889
	s = socket.socket()
	s.bind((host,port))
	s.listen(5)
	print "waiting for requests"
	co, ci = s.accept()
	co.send("Connection Established")
	recv_data = co.recv(1023)
	
except Exception as err:
	print err

finally:
	if s:
		s.close()
