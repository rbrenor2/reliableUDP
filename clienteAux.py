import socket
import sys

packetsList = []

def makePackets(msg, tipoMsg):
		sizeOfMsg = sys.getsizeof(msg)
		i = 0
		auxPacketDataField = kPacketDataField
		
		while i < sizeOfMsg :
			if ((auxPacketDataField + kPacketDataField > sizeOfMsg) | (auxPacketDataField > sizeOfMsg)):
				auxPacketDataField = sizeOfMsg
				packetMsg = packetMsg + msg[i:auxPacketDataField+1]
			    packetsList.append(packet)
				i = i + kPacketDataField + 1	
			else:
				packetMsg = packetMsg + msg[i:auxPacketDataField+1]
				packetsList.append(packet)
				i = i + kPacketDataField + 1
				auxPacketDataField = auxPacketDataField + kPacketDataField
				

def makePacket(msg, tipoMsg):
	sizeOfPacket = sys.getsizeof(lastNumSeqSent) + sys.getsizeof(tipoMsg) + sys.getsizeof(msg)
	aux = sys.getsizeof(sizeOfPacket)
	sizeOfPacket = sizeOfPacket + aux

	packet = pack(sizeOfPacket, lastNumSeqSent, tipoMsg, msg)
		
return packet