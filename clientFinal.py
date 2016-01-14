import socket
import sys
import math
import threading
import time



kPacketSize = 20
kPacketHeadSize = 9
kPacketDataField = kPacketSize - kPacketHeadSize

kClientExpectedNumSeq = 100

kI = 0
kNextSeqNum = 100
kBase = 100
kWindowSize = 2
kCheckEnviouTudo = 0

kListeningThread = None

packetsList = []

ACK = 'ACK'
SYN = 'SYN'
DAT = 'DAT'
EMPTY = 'EMPTY'

######### CLASSES FOR THREADING ##########

#!/usr/bin/python



exitFlag = 0

class thread2 (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        listenAcks()
        print "Exiting " + self.name
    def stop(self):
        self.stopped = True


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

    return (packet, 0)

def sendPackets(s):
    global packetsList
    global kNextSeqNum
    global kWindowSize
    global kBase
    global kI
    global kListeningThread
    
    print 'LISTA A SER ENVIADA:'
    print packetsList
    
    kCheckEnviouTudo = False
    
    kListeningThread = thread2(2, 'Thread 2', 2)
    kListeningThread.start()

    while not kCheckEnviouTudo:
        if kI < len(packetsList):
            if packetsList[kI][1] == 0:
                sendPacket(packetsList[kI],s)
                kI+=1
            else:
                kI+=1
        else:
            kI = 0
        
        if checkList(packetsList) == True:
            kCheckEnviouTudo = True

def checkList(packetsList):
    aux = 0
    for i in packetsList:
        if i[1] == 1:
            aux +=1

    if aux == len(packetsList):
        return True
    else:
        return False
    
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
    global kListeningThread
    global kI
    global packetsList
    try:
        if kNextSeqNum < kBase+kWindowSize:
            s.sendto(packet[0],(HOST,PORT))
            packetAux = packetsList[kI][0]
            packetsList[kI] = (packetAux, 1)
        #if kClientExpectedNumSeq == 101:
            #kListeningThread.stop()
            #kListeningThread = thread2(2, 'Thread 2', 2)
            #kListeningThread.start()
    except socket.error:
        print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

def writing(s):
    global packetList
    while 1:
        msg = raw_input('>')
        makePackets(msg,s)
        sendPackets(s)

def listenAcks():
    global kListeningThread
    global kNextSeqNum
    global s

    while 1:    
        print 'Waiting for Ack with numSeq:' + str(kClientExpectedNumSeq)
        try:
            s.settimeout(20.0)
            d = s.recvfrom(1024)
            data = d[0]
            addr = d[1]
            print 'LISTENacks escutou isso: ' + data

            #decode
            tamPacket = data[0:2]
            numSeq = data[2:5]
            tipoMsg = data[5:8]
            msg = data[8:]
       
        
            #base anda o numero de seq da MSG ACK que ele leu
            kBase = int(numSeq)
            #se base ficar igual o nextSeqNum, para o timer (kill thread)
            if kBase == kNextSeqNum:
                kListeningThread.stop()  
            #senao reinicia a thread
            else:
                kListeningThread = thread2(2, 'Thread 2', 2)
                kListeningThread.start()      
 
        except socket.timeout:
            print'timedOut: ferrou!'
            kListeningThread.vlock.acquire()
            kNextSeqNum = kBase
            zeraAlgunsPacketsList()
            kListeningThread.vlock.release()
        #reenviar todos os dados ainda nao confirmados e reiniciar o timer(thread)

def zeraAlgunsPacketsList():
    global kBase
    global packetsList
    
    for i in packetsList:
        if packetsList[i] > kBase:
            packetAux = packetsList[i][0]
            packetsList[i] = (packetAux, 0)

	
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

writing(s)

#cria thread
#writingThread = thread1(1, 'Thread 1', 1)

#start threads
#writingThread.start()







