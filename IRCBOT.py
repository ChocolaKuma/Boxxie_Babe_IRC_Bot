#IRC BOT FRAMEWORK
#PYTHON 3X
#Johnathan Hinebrook
#johnisadept@live.com

import socket, time
 
network = 'irc.rizon.io'
network = network.encode(encoding='UTF-8',errors='strict')
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
USR = "USER USERNAME USERNAME USERNAME :USERNAME\r\n"
nic = "NICK USERNAME \r\n"
PAS = '/msg NickServ IDENTIFY PASSWORD\r\n'
JOI = 'JOIN #brook_nise\r\n'
pi  = "hello"
po  = "PONG '\r\n'"

PING = pi.encode(encoding='UTF-8',errors='strict')
PONG = po.encode(encoding='UTF-8',errors='strict')
USER = USR.encode(encoding='UTF-8',errors='strict')
NICK = nic.encode(encoding='UTF-8',errors='strict')
PASS = PAS.encode(encoding='UTF-8',errors='strict')
JOIN = JOI.encode(encoding='UTF-8',errors='strict')

irc.connect ( ( network, port ) )
print (irc.recv ( 4096 ))

time.sleep(.5)
irc.send (USER)
time.sleep(.5)
irc.send(NICK)
time.sleep(.5)
irc.send (PASS)
time.sleep(.5)
irc.send (JOIN)

while True:
    data = irc.recv ( 4096 )
    if data.find ( PING ):
        irc.send ( PONG  )
        print (data)
   
    

