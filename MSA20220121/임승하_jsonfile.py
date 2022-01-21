import json

try:
    fileName = open("datalab/datalab/mydata.json", "rb")
    tempData = json.load(fileName)
    resultData1 = tempData["name"]
    resultData1 = tempData["age"]
    resultData1 = tempData["address"]
    resultData1 = tempData["email"]
    resultData1 = tempData["empcheck"]
except NameError as ex:
    error = str(ex)
except FileNotFoundError as ex:
    error = str(ex)
except Exception as ex:
    error = str(ex)
else:
    fileName.close()


jsonData2 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }



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
