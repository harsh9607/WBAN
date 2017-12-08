#  :: PERSONAL SERVER ::
#  :: Communication type  :: INTRA SERVER
#  :: Hashing algo used :  MD5
#  :: Asymmetric crypto used : RSA
#  :: Authentication method used : Two way authentication
#  :: Author : Harsh Pathak and Team
#  :: Guided by : Dr. Manu Vardhan

import socket
import thread
import time  
import datetime
import sys
import hashlib
from Crypto.PublicKey import RSA

time.sleep(0.1)

# PS Socket creation
def Main():
    s = socket.socket()
    host = socket.gethostname()
    port = 40122
    s.bind((host,port))
    s.listen(10)
    print 'Sever up and running !!'
    print 'Waiting for Sensors'
#Accepting connection with the Sensor
    while True :
        c, addr = s.accept()
        thread.start_new_thread(myfun , (c,addr) )



def myfun(c,addr):
    # ~~~  Generating Keys using RSA algorithm ~~~   
    print 'Generating Keys !'
    time.sleep(2);
    key = RSA.generate(1024)
    publickey2send = key.publickey()
    print 'Keys generated !..Exchanging public keys'
    # ~~~  Exchanging public key ~~~
    c.send(publickey2send.exportKey());
    ClientsPubKey = RSA.importKey(c.recv(2048))
    time.sleep(2)
    print 'keys exchange successful!'

    # ~~~  Authentication of the sensor ! ~~~
    dummy = 'Pls authenticate yourself '
    Tencypted = ClientsPubKey.encrypt(dummy,int(len(dummy))) # Text ENCRYPTED
    c.sendall(str(Tencypted))
    #Sensor replies back with a nonce
    temp = c.recv(2017)
    d_nonce = key.decrypt(eval(temp))
    time.sleep(2)
    print 'Nonce received from sensor side'
    time.sleep(1)
    print('nonce received ->'+d_nonce)
    E_d_nonce = ClientsPubKey.encrypt(d_nonce,int(len(d_nonce)))
    c.sendall(str(E_d_nonce))
    # ~~~  Authentication complete !!  ~~~

    # ~~~ Communication Begins now !! ~~~
    time.sleep(2)

    # ~~~ Open Our File that stores the contents ~~~
    f = open("DataFile.txt","ab")
    time2 = str(datetime.datetime.now())
    f.write(time2)
    f.write('\n')

    while True :
        print 'Data recieved ! Decryption in process'
        data = c.recv(2048)
        time.sleep(1)
        print 'msg decrypted'
        msg = key.decrypt(eval(data))
        print('Decrypted msg = '+ msg)
        c.send("a")#dummy packet
        
        # Checking message authenticity
        hashrecv = c.recv(128)
        print('hash received ='+hashrecv)
        md5_obj = hashlib.md5()
        md5_obj.update(msg);
        
        if md5_obj.hexdigest() != hashrecv:
            print('hashes dont match !')
            break
        else:
            print('Matching hashes ...')
            time.sleep(2)
            print('hashes match ! msg unhampered !')
            f.write(msg)
            f.write('\n')


        if msg == "BYE":
            break
        

    f.close()
    c.close()


if __name__ == "__main__" :
    Main()

