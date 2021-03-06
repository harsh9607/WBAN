# Heart Sensor
import socket
import time
import random
import sys
import hashlib
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

time.sleep(0.1)
key = RSA.generate(2048)
publickey2send = key.publickey()

# Creating a TCP connection with the personal server(PS)
s = socket.socket()
host = socket.gethostname()
port = 40192

# data generated by the Sensor 
num1 = 'HEART :: Systole value: ' + str(random.randint(1,101))
num2 = 'HEART :: Distole value: ' + str(random.randint(109,700))
num3 = 'HEART :: Beats per min: ' + str(random.randint(60,71))
bye = "BYE"

#Connecting with the PS
s.connect((host,port))

# Key Exchange
ServersPubkey = RSA.importKey(s.recv(2048))  
print('Client :: Received the servers public key ')
s.send(publickey2send.exportKey());
time.sleep(2)
print('Sending our public key !')
time.sleep(1)
print('Key exchange successful ! \n')

# Authenticating Identity
data = s.recv(1024)
decrypted = key.decrypt(eval(data))
print(decrypted)
nonce = str(random.randint(0,10000))
print('Nonce sent = ' + nonce)
time.sleep(2)
E_nonce = ServersPubkey.encrypt(nonce,int(len(nonce)))
s.sendall(str(E_nonce))
temp = s.recv(2049)
R_nonce = key.decrypt(eval(temp))
print('Nonce reveiced back  = ' + R_nonce)
if str(R_nonce) == str(nonce) :
        print('Authentication successful !!')

else :
        print('Authentication failed')
        s.close()

s.send(' ')
temp2 = s.recv(2049)
d_nonce2 = key.decrypt(eval(temp2))
E_d_nonce2 = ServersPubkey.encrypt(d_nonce2,int(len(d_nonce2)))
s.sendall(str(E_d_nonce2))


# Authentication completion 

# num 1
print('Message to be sent :: ')
time.sleep(1)
print(num1)

#md5_obj = hashlib.md5()
#md5_obj.update(num1)

h = SHA256.new()
h.update(num1.encode('utf-8'))

print('Generating Digest !')
time.sleep(2)
print(h.hexdigest())
Tencypted = ServersPubkey.encrypt(num1,int(len(num1)))
print('Encrypted message looks like this ::')
time.sleep(2)
print(str(Tencypted))
print('\n')
s.sendall(str(Tencypted))
s.recv(16) #dummy recv
s.send(h.hexdigest())
time.sleep(1)
print('Sending all data to Personal server')

#num2
print('Message to be sent :: ')
time.sleep(1)
print(num2)

#md5_obj = hashlib.md5()
#md5_obj.update(num2)

h = SHA256.new()
h.update(num2.encode('utf-8'))

print('Generating Digest !')
time.sleep(2)
print(h.hexdigest())
Tencypted = ServersPubkey.encrypt(num2,int(len(num2)))
print('Encrypted message looks like this ::')
time.sleep(2)
print(str(Tencypted))
print('\n')
s.sendall(str(Tencypted))
s.recv(16) #dummy recv
s.send(h.hexdigest())
time.sleep(1)
print('Sending all data to Personal server')

# num 3
print('Message to be sent :: ')
time.sleep(1)
print(num3)

#md5_obj = hashlib.md5()
#md5_obj.update(num3)

h = SHA256.new()
h.update(num3.encode('utf-8'))


print('Generating Digest !')
time.sleep(2)
print(h.hexdigest())
Tencypted = ServersPubkey.encrypt(num3,int(len(num3)))
print('Encrypted message looks like this ::')
time.sleep(2)
print(str(Tencypted))
print('\n')
s.sendall(str(Tencypted))
s.recv(16) #dummy recv
s.send(h.hexdigest())
time.sleep(1)
print('Sending all data to Personal server')

# BYE message
print('Message to be sent :: ')
time.sleep(1)
print(bye)

#md5_obj = hashlib.md5()
#md5_obj.update(bye)

h = SHA256.new()
h.update(bye.encode('utf-8'))


print('Generating Digest !')
time.sleep(2)
print(h.hexdigest())
Tencypted = ServersPubkey.encrypt(bye,int(len(bye)))
print('Encrypted message looks like this ::')
time.sleep(2)
print(str(Tencypted))
print('\n')
s.sendall(str(Tencypted))
s.recv(16) #dummy recv
s.send(h.hexdigest())
time.sleep(1)
print('Sent all data to Personal server')
#closing connection
s.close()
