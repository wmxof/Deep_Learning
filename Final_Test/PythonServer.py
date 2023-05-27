import socket
import struct
from PIL import Image
import io
import cv2
import pytesseract
import numpy as np
from keras.models import load_model

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


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)

    return buf


host = '' # 호스트 ip를 적어주세요
port = 7777          # 포트번호를 임의로 설정해주세요

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(True)

conn, addr = s.accept()
print('Connected by', addr)
length = recvall(conn, 4)
length = struct.unpack('!i', length)[0]

stringData = recvall(conn, int(length))
data = io.BytesIO(stringData)
im = Image.open(data)

im.save('received_image1.png','PNG')

conn.close()




# pytesseract에서 Tesseract OCR 경로 설정
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# # 모델 로드
# model = load_model('model_final.h5')

# def load_and_process_image(image_file):
#     # 이미지 로드 및 전처리
#     image = cv2.imread(image_file)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#     image = cv2.resize(image, (28, 28))
#     image = np.array(image, dtype=np.float32)
#     image = image / 255.0  # 이미지를 0과 1 사이의 값으로 정규화
#     image = np.expand_dims(image, axis=0)
#     image = np.expand_dims(image, axis=-1)  # 모델 입력에 맞게 차원 확장

#     return image

# def predict_expression(image_file):
#     # 이미지 전처리
#     image = load_and_process_image(image_file)

#     # 모델 예측
#     pred = model.predict(image)
#     pred_idx = np.argmax(pred, axis=1)[0]

#     return pred_idx

# def calculate_expression(expression_list):
#     # 숫자와 연산자를 인식하여 계산 결과 도출
#     result = None
#     operator = None
#     for char in expression_list:
#         if char.isdigit():
#             if result is None:
#                 result = int(char)
#             else:
#                 if operator == '+':
#                     result += int(char)
#                 elif operator == '-':
#                     result -= int(char)
#                 elif operator == 'x':
#                     result *= int(char)
#                 elif operator == '/':
#                     result /= int(char)
#             operator = None
#         elif char in ['+', '-', 'x', '/']:
#             operator = char
#     return result

# image_file = 'C:/Users/lsbls/Desktop/a+a.png'

# # 이미지에서 숫자와 연산자를 추출해서 리스트로 저장
# expression_list = []
# text = pytesseract.image_to_string(image_file, lang='eng', config='--psm 6 --oem 3')
# for char in text:
#     if char.isdigit() or char in ['+', '-', 'x', '/']:
#         expression_list.append(char)

# # 추출한 문자열 리스트를 결합해서 수식 문자열 생성
# expression_str = ''.join(expression_list)

# # 수식 문자열에서 숫자와 연산자를 인식해서 계산 결과 도출
# result = calculate_expression(expression_list)

# # 결과 출력
# print(f'{expression_str} = {result}')