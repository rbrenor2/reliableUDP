import socket
import sys

lastNumSeqReceived = 0

lastNumSeqSent = 0

kPacketSize = 100
kPacketHeadSize = 2
kPacketDataField = packetSize - packetHeadSize

kWindowSize = 5

packetsList = []

#Error codes
#101: numSeq errado

#const

kSYN = 0
kSYNACK = 1
kACK = 2

ENDCONNECTION = 3

lastMessage = ""

packetsNumber = 0

host = ''
port = 5000

kLoopI = 0

#cliente enviand:
def sendPackets(packets):	
	while (kLoopI < kWindowSize):
		
		try:
			s.sendto(packets[kLoopI], (host,port))
		except socket.error:
			print 'Error: could not send packet number' + kLoopI + 'from list'
			sys.exit()

		kLoopI = kLoopI + 1

		


def makePackets(msg, tipoMsg):
		sizeOfMsg = sys.getsizeof(msg)
		i = 0
		auxPacketDataField = kPacketDataField
		
		while i < sizeOfMsg :
			if (auxPacketDataField + kPacketDataField > sizeOfMsg) || (auxPacketDataField > sizeOfMsg):
				auxPacketDataField = sizeOfMsg
				packetMsg = packetMsg + msg[i:auxPacketDataField+1]
				global packetsList.append(packet)
				i = i + kPacketDataField + 1	
			else:
				packetMsg = packetMsg + msg[i:auxPacketDataField+1]
				global packetsList.append(packet)
				i = i + kPacketDataField + 1
				auxPacketDataField = auxPacketDataField + kPacketDataField
				

def makePacket(msg, tipoMsg):
	sizeOfPacket = sys.getsizeof(lastNumSeqSent) + sys.getsizeof(tipoMsg) + sys.getsizeof(msg)
	aux = sys.getsizeof(sizeOfPacket)
	sizeOfPacket = sizeOfPacket + aux

	packet = pack(sizeOfPacket, lastNumSeqSent, tipoMsg, msg)
		
return packet

def startListening():

	HOST = ''   # Symbolic name meaning all available interfaces
	PORT = 5000 # Arbitrary non-privileged port
 
	# Datagram (udp) socket
	try:
    	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    	print 'Socket created'
	except socket.error, msg :
    	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    	sys.exit()
 
	# Bind socket to local host and port
	try:
    	s.bind((HOST, PORT))
	except socket.error , msg:
    	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    	sys.exit()
     
	print 'Socket bind complete'
 
	#now keep talking with the client
	while 1:
    	# receive data from client (data, addr)
    	d = s.recvfrom(1024)
    	data = d[0]
    	addr = d[1]

    	decode(data)
     
    	if not data: 
        	break
     
    	reply = 'OK...' + data
     
    	s.sendto(reply , addr)
    	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
     
        s.close()

def writing ():
	msg = raw_input(">")
	packet = makePacket()

#cliente recebendo


def decode (data):
	tamPacket = data[:]
	numSeq = data[:]
	tipoMsg = data[:]
	msg = data[:]

	if tipoMsg == ACK:
       if checkAck(tamPacket, numSeq, tipoMsg):
	      msg = data[:]
      	  lastMessage = lastMessage + msg
  	   	  writing()
	   return ENDCONNECTION
	   else
	   return 101
	elif tipoMsg == SYN:
		makePacket(0, 0, SYNACK)
    elif tipoMsg:
    retu


def checkAck(tamPacket, numSeq, tipoMsg, msg):
	#Se o numero de sequencia
	if numSeq == lastNumSeqReceived + 1:
		packet = makePacket(0, 0, las)

	return True
	else:
		makePacket(0, lastNumSeqReceived, ACK)
	return False

def checkSyn(tamPacket, numSeq, tipoMsg):
	proxAck = lastPacketReceived + 1



startListening()
writing()



	




