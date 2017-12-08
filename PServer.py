#  :: PERSONAL SERVER ::
#  :: Communication type  :: INTRA SERVER
import socket
import thread
import datetime

# PS Socket creation
s = socket.socket()
host = socket.gethostname()
port = 40122
s.bind((host,port))
s.listen(10)

print 'Sever up and running !!'
print 'Waiting for Sensors'

#Accepting connection with the Sensor 
c, addr = s.accept()


# Open Our File that stores the contents
f = open("DataFile.txt","ab")
time = str(datetime.datetime.now())
f.write(time)
f.write('\n')

while True:
    
    print 'Got connection from',addr
    msg = c.recv(50)
    print msg
    f.write(msg)
    f.write('\n')
    if msg == "BYE":
        break    
    c.send('received your message...')
    
    

f.close()
c.close()
