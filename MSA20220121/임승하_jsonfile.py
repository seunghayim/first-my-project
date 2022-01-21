file - mydata.json 
{
    "empid": 12345678,
    "name": "홍길동",
    "info": [
        {
            "date1": "2022-01-21",
            "home": "서울시"
        },
        {
            "dep": "개발",
            "email": "aaa@aaa.co.kr"
        }
    ]
}

-------------------------------------------------------------
# 1. 예외 처리를 이용해 json 읽기
import json

try:
    fileName = open("datalab/datalab/mydata.json", "rb")
    tempData = json.load(fileName)
    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData4 = tempData["email"]
    resultData5 = tempData["empcheck"]
except NameError as ex:
    error = str(ex)
except FileNotFoundError as ex:
    error = str(ex)
except Exception as ex:
    error = str(ex)
else:
    fileName.close()


# 2.예외 처리를 이용해 json 쓰기
# json 데이터
jsonData2 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }


# 예외처리
try:
    fileName1 = open('datalab/datalab/mydata1.json', "w", encoding="utf-8")
    json.dump(jsonData2, fileName1, ensure_ascii=False, indent=4)
except FileNotFoundError as ex:
    error = str(ex)
except Exception as ex:
    error = str(ex)
else:
    fileName1.close()




# 디버깅을 위한 임시 변수
temp = 0
