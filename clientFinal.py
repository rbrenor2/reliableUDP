import socket
import sys

kClientExpectedNumSeq = 100

ACK = 'ACK'
SYN = 'SYN'
DAT = 'DAT'

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

def sendPacket(packet,s):
    try:
        s.sendto(packet,(HOST,PORT))
    except socket.error:
        print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

def writing(s):
    while 1:
        msg = raw_input('>')
        packet = makePacket(msg,SYN,kClientExpectedNumSeq)
        sendPacket(packet,s)
        print 'Waiting...'
        d = s.recvfrom(1024)
        data = d[0]
        addr = d[1]

        print data
     
        if not data:
            break

	
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


