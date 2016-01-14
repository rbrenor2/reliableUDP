import socket
import sys
import math

kPacketSize = 100
kPacketHeadSize = 2
kPacketDataField = kPacketSize - kPacketHeadSize

kClientExpectedNumSeq = 100

ACK = 'ACK'
SYN = 'SYN'
DAT = 'DAT'
EMPTY = 'EMPTY'

def decode (data,s,addr):
    global kClientExpectedNumSeq
	
    tamPacket = data[0:2]
    numSeq = data[2:5]
    tipoMsg = data[5:8]
    msg = data[8:]
   
    print('-------------TamPacket: ' + tamPacket + ' ---NumSeq:' + numSeq + '---NumSeqServer: ' + str(kClientExpectedNumSeq) + '---TipoMsg: ' + tipoMsg + '----------------------')
    print('msg:' + msg)

    if tipoMsg == SYN:
	    #setar kClientExpectedNumSeq com numSeq
        kClientExpectedNumSeq = int(numSeq)
        #incrementa kClientExpectedNumSeq
        kClientExpectedNumSeq = kClientExpectedNumSeq + 1
	    #pacote com ACK e kClientExpectedNumSeq
        packet = makePacket(EMPTY,ACK,kClientExpectedNumSeq)
        sendPacket(packet,s,addr)
    elif tipoMsg == DAT:
        #checa o numero de sequencia
        if int(numSeq) == kClientExpectedNumSeq:
            #se estiver certo:
            #incrementa kClientExpectedNumSeq
            kClientExpectedNumSeq = kClientExpectedNumSeq + 1
            #printa mensagem
            #manda pacote com ACK e kClientExpectedNumSeq (proximo ja incrementado)
            packet = makePacket(EMPTY,ACK,kClientExpectedNumSeq)
            sendPacket(packet,s,addr)

        #Se estiver errado:
        #manda pacote com ACK e kClientExpectedNumSeq (sem incrementar pra indicar que nao recebeu)
        else:
            packet = makePacket(EMPTY,ACK,kClientExpectedNumSeq)
            sendPacket(packet,s,addr)
                     

def makePacket(msg, tipoMsg, numSeq):
	#get size of the packet
    sizeOfPacket = len(str(numSeq)) + len(tipoMsg) + len(msg)
    aux = len(str(sizeOfPacket))
    sizeOfPacket = sizeOfPacket + aux
	
	#make packet
    packet = str(sizeOfPacket) + str(numSeq) + tipoMsg + msg

    return packet

def sendPacket(packet,s,addr):
    print packet
    try:
        s.sendto(packet,addr)
    except socket.error:
        print 'Error: could not send packet'
        sys.exit()

def checkNumSeq(numSeq):
    #se o numSeq for igual ao esperado
    if numSeq == kClientExpectedNumSeq:
        return True
    else:
        return False

#MAIN
HOST = 'localhost'   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port

# CRIA SOCKET
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created!'
except s.error, msg:
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
    # Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#now keep talking with the client
while 1:
    print 'Waiting...'
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    decode(data,s,addr)

    if not data:
        break
