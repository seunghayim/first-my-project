from flask import Flask
import json, requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello():
    return 'Hello, World!'

# 공공데이터활용지원센터_코로나19 예방접종 위탁의료기관 조회서비스 
@app.route('/data')
def FlaskData():
    keyValue = r"V6lQYKtQODdLI8HPFUM%2FF1fi2FGeE%2FbXr142ghKq1Vfzozi42DXMWVzP9Hp9GI%2FI%2F1%2BbUud5Pa4JVwsu653Y8Q%3D%3D"
    address = r"%EC%A4%91%EB%9E%91%EA%B5%AC"
    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=1&perPage=10"
    dataURL += f"&cond%5BorgZipaddr%3A%3ALIKE%5D={address}"
    dataURL += f"&serviceKey={keyValue}"
    
    return requests.get(dataURL).json()

# 공공데이터활용지원센터_코로나19 예방접종센터 조회서비스
@app.route('/data2')
def FlaskData2():
    keyValue = r"V6lQYKtQODdLI8HPFUM%2FF1fi2FGeE%2FbXr142ghKq1Vfzozi42DXMWVzP9Hp9GI%2FI%2F1%2BbUud5Pa4JVwsu653Y8Q%3D%3D"
    dataURL = "http://api.odcloud.kr/api/15077586/v1/centers?"
    dataURL += "page=1&perPage=10"
    dataURL += f"&serviceKey={keyValue}"

    return requests.get(dataURL).json()


 


