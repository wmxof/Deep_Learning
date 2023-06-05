from google.cloud import vision
from google.cloud import vision
from PIL import Image

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/404/Desktop/Server 및 Google OCR/proven-country-388105-2b1fa1639dd9.json'

def calculate_expression(expression_list):
    # 숫자와 연산자를 인식하여 계산 결과 도출
    result = None
    operator = None
    for char in expression_list:
        if char.isdigit():
            if result is None:
                result = int(char)
            else:
                if operator == '+':
                    result += int(char)
                elif operator == '-':
                    result -= int(char)
                elif operator == 'x':
                    result *= int(char)
                elif operator == '/':
                    result /= int(char)
            operator = None
        elif char in ['+', '-', 'x', '/']:
            operator = char
    return result

def recognize_text(image_path):
    # 이미지 열기
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    # 이미지 데이터를 Vision API에 전송
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # 인식된 텍스트 추출
    if texts:
        return texts[0].description
    else:
        return None

image_path = r"C:/Users/404/Desktop/Server 및 Google OCR/1.png"



# 이미지에서 텍스트 인식
recognized_text = recognize_text(image_path)

if recognized_text:
    # 추출된 텍스트에서 숫자와 연산자 추출
    expression_list = []
    for char in recognized_text:
        if char.isdigit() or char in ['+', '-', 'x', '/']:
            expression_list.append(char)

    # 추출한 문자열 리스트를 결합하여 수식 문자열 생성
    expression_str = ''.join(expression_list)

    # 숫자와 연산자를 인식하여 계산 결과 도출
    result = calculate_expression(expression_list)

    # 결과 출력
    print(f'{expression_str} = {result}')
else:
    print("텍스트를 인식할 수 없습니다.")
