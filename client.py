import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5009


print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
MESSAGE = raw_input("Enter Number:")

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data  = sock.recv(1024)
print  data
