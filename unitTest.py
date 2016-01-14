import socket
import sys
import math

kClientExpectedNumSeq = 100

kPacketSize = 16
kPacketHeadSize = 9
kPacketDataField = kPacketSize - kPacketHeadSize

packetsList = []

ACK = 'ACK'
SYN = 'SYN'
DAT = 'DAT'

EMPTY = 'EMPTY'

def writing():
    global packetList
    while 1:
        msg = raw_input('>')
        makePackets(msg)
        print packetsList
        #sendPackets(s)
        

        #packet = makePacket(msg,DAT,kClientExpectedNumSeq)
        #sendPacket(packet,s)
        #print 'Waiting...'
        #d = s.recvfrom(1024)
        #data = d[0]
        #addr = d[1]

        #print data
     
        #if not data:
            #break

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

def makePackets(msg):
    sizeOfMsg = len(msg)
    whileCondition = math.ceil(int(sizeOfMsg/kPacketDataField))
    #SE A MENSAGEM COUBE EM UM PACOTE O LACO VAI RODAR UMA VEZ SO
    if whileCondition == 0:
        whileCondition = 1

    msgAux = msg
    i = 0
    auxPacketDataField = kPacketDataField
   
    global packetsList
    global kClientExpectedNumSeq

    while whileCondition > 0:
        print 'VALOR DE WHILE CONDITION:' + str(whileCondition)
        sizeOfMsg = len(msgAux)
        #SE FOR O ULTIMO PEDACO OU SE A MENSAGEM TODA FOR MENOR DO QUE O TAMANHO DESTINADO A DADO NO PACOTE
        if sizeOfMsg - auxPacketDataField < kPacketDataField:
            print 'ENTROU NO IF DO WHILE DA DIVISAO

            #vai pro fim da msg
            #auxPacketDataField = sizeOfMsg
            #pega pedaco da mensagem
            #packetMsg = msg[i:auxPacketDataField+1]
            #packetMsg = msgAux
            #cria pacote e envia
            #packet = makePacket(packetMsg, DAT, kClientExpectedNumSeq)
            #coloca pacotes na lista
            #sendPacket(packet,s)
            #packetsList.append(packet)
            #packetList.insert(len(packetsList)+1, packet)
            #incrementa num seq
            #kClientExpectedNumSeq = kClientExpectedNumSeq + 1
            #incrementa i e auxPacketDataField
            #i = i + kPacketDataField
            #auxPacketDataField = auxPacketDataField + kPacketDataField
            #decrementa whileCondition
            #whileCondition = whileCondition - 1
            

            #auxPacketDataField = sizeOfMsg
            #packetMsg = packetMsg + msg[i:auxPacketDataField+1]
            #packetsList.append(packet)
            #i = i + kPacketDataField + 1	
        #SE FOR UM PEDACO NORMAL E TIVER QUE CORTAR
        else:
            print 'ENTROU NO ELSE DO WHILE DA DIVISAO'
            
            

            #pega pedaco da mensagem
            #packetMsg = msgAux[i:auxPacketDataField]
            #msgAux = packetMsg
            #cria pacote e envia
            #packet = makePacket(packetMsg, DAT, kClientExpectedNumSeq)
            #coloca pacotes na lista
            #sendPacket(packet,s)
            #packetsList.append(packet)
            #packetList.insert(len(packetsList)+1, packet)
            #incrementa num seq
            #kClientExpectedNumSeq = kClientExpectedNumSeq + 1
            #vai pro outro pedaco
            #auxPacketDataField = auxPacketDataField + kPacketDataField
            #incrementa i e auxPacketDataField
            #i = i + kPacketDataField
            #auxPacketDataField = auxPacketDataField + kPacketDataField
            #decrementa whileCondition
            #whileCondition = whileCondition - 1
            
            
            #packetMsg = packetMsg + msg[i:auxPacketDataField+1]
            #packetsList.append(packet)
            #i = i + kPacketDataField + 1
            #auxPacketDataField = auxPacketDataField + kPacketDataField
    
        

writing()

