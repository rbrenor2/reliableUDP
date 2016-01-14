import socket
import sys
import math
import threading
import time



kPacketSize = 20
kPacketHeadSize = 9
kPacketDataField = kPacketSize - kPacketHeadSize

kClientExpectedNumSeq = 100
kBase = 0
kWindowSize = 2


packetsList = []

ACK = 'ACK'
SYN = 'SYN'
DAT = 'DAT'
EMPTY = 'EMPTY'

######### CLASSES FOR THREADING ##########

#!/usr/bin/python



exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name



def decode (data,s,addr):
    global kClientExpectedNumSeq
	
    tamPacket = data[0:2]
    numSeq = data[2:5]
    tipoMsg = data[5:8]
    msg = data[8:]

    if tipoMsg == ACK:
        writing(s)
    else:
        print 'NAO DECODIFICOU DIREITO'

def makePackets(msg,s):
    sizeOfMsg = len(msg)
    whileCondition = math.ceil(sizeOfMsg/float(kPacketDataField))
    #SE A MENSAGEM COUBE EM UM PACOTE O LACO VAI RODAR UMA VEZ SO
    if whileCondition == 0:
        whileCondition = 1

    i = 0
   
    global packetsList
    global kClientExpectedNumSeq

    while whileCondition > 0:
        print 'VALOR DE WHILE CONDITION:' + str(whileCondition)
        
        #SE A MENSAGEM TODA FOR MAIOR DO QUE O TAMANHO DESTINADO A DADO NO PACOTE DIVIDE
        if sizeOfMsg > kPacketSize:
            packet = makePacket(msg[i:(i+kPacketSize)], DAT, kClientExpectedNumSeq)
            packetsList.append(packet)
            i += kPacketSize
            kClientExpectedNumSeq += 1
           	
        #SE FOR UM PEDACO MENOR QUE O PACKET SIZE
        else:
            packet = makePacket(msg[i:], DAT, kClientExpectedNumSeq)
            packetsList.append(packet)
            kClientExpectedNumSeq += 1
        
        whileCondition -= 1
            

def makePacket(msg, tipoMsg, numSeq):
	#get size of the packet
    sizeOfPacket = len(str(numSeq)) + len(tipoMsg) + len(msg)
    aux = len(str(sizeOfPacket))
    sizeOfPacket = sizeOfPacket + aux
	
	#make packet
    packet = str(sizeOfPacket) + str(numSeq) + tipoMsg + msg
    print 'DEBUG:'
    print 'SIZE: ' + str(sizeOfPacket) + ' NUMSEQ: ' + str(numSeq) + ' TIPOMSG: ' + tipoMsg + ' MSG: ' + msg

    return packet

def sendPackets(s):
    global packetsList
    
    i = 0
    
    print 'LISTA A SER ENVIADA:'
    print packetsList
    
    sendPacket(packetsList[i],s)
    checkAck(s)

    #while 1
        #if nextSeqNum < kBase + kWindowSize:
            #sendPacket(packetsList[i],s)
            #nextSeqNum += 1
            
            

def checkAck(s):
    print 'Waiting for Ack...'
    s.settimeout(5.0)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    print('Timeout funcionou')

    tamPacket = data[0:2]
    numSeq = data[2:5]
    tipoMsg = data[5:8]
    msg = data[8:]

    if tipoMsg == ACK:
        print('recebeu mensagem Ack')
        print msg
        if numSeq == (kClientExpectedNumSeq):
            print('numSeq correto')
            return True
        else:
            return False
    else:
        print('NAO ENVIOU ACK')

def sendPacket(packet,s):
    try:
        s.sendto(packet,(HOST,PORT))
    except socket.error:
        print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

def writing(s):
    global packetList
    while 1:
        msg = raw_input('>')
        makePackets(msg,s)
        sendPackets(s)

        #packet = makePacket(msg,DAT,kClientExpectedNumSeq)
        #sendPacket(packet,s)

def listenAcks():
    print 'Waiting for Ack with numSeq:' + kClientExpectedNumSeq
    s.settimeout(5.0)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    print('Timeout funcionou')

    
	
HOST = 'localHost'   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port

#MAIN
# Datagram (udp) socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created!'

except s.error, msg:
    print 'Failed to create socket. Error Code :'
    sys.exit()

#checkFirstAck(s)

writing(s)



