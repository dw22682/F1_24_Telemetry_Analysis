import socket
from PacketStructs import Packet

x = Packet.Packet()

PORT = 20777

svr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
svr.bind(('0.0.0.0', PORT))

print(socket.gethostbyname(socket.gethostname()))
print("listening...")

while True:
    data, addr = svr.recvfrom(2048)
    print("message recieved")
