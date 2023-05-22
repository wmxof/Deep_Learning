import socket
import struct
from PIL import Image
import io

save_path = "C:/Users/lsbls"
host = ''
port = 7777


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("서버가 시작되었습니다")

client_socket, addr = server_socket.accept()

with open(save_path, 'wb') as file:
    data = client_socket.recv(1024)
    while data:
        file.write(data)
        data = client_socket.recv(1024)
    print("이미지를 저장하였습니다")


client_socket.close()
server_socket.close()
print("서버가 종료되었습니다")   






# def recvall(sock, count):
#     buf = b''
#     while count:
#         newbuf = sock.recv(count)
#         if not newbuf: return None
#         buf += newbuf
#         count -= len(newbuf)

#     return buf


# host = '' # 호스트 ip를 적어주세요
# port = 7777          # 포트번호를 임의로 설정해주세요

# s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))
# s.listen(True)

# conn, addr = s.accept()
# print('Connected by', addr)
# length = recvall(conn, 4)
# length = struct.unpack('!i', length)[0]

# stringData = recvall(conn, int(length))
# data = io.BytesIO(stringData)
# im = Image.open(data)

# im.save('received_image.png','PNG')

# conn.close()