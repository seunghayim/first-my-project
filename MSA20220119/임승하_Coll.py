# 평균 점수 구하는 함수
def meanScore(dic):
    total = 0
    scoreData = dic.values()
    studentNum = len(dic)

    for score in scoreData:
        total += score

    return total / studentNum
    

# set자료 data에 num1과 num2의 공배수 구하는 함수
def comMulti(num1, num2, data):
    newData = set({})
    
    for element in data:
        if element % num1 == 0 and element % num2 == 0:
            newData.add(element)
    return newData
  


--------------------------------------------------------------------------------
assignment.py

from assignment import (meanScore, comMulti)
# 과제 1 : 딕셔너리를 이용해서 평균 점수 구하기
scoreDic = {
    '국어': 95,
    '영어': 90,
    '수학': 80,
    '과학': 50,
}
meanScore(scoreDic)

# 과제 2 : set을 이용해 1~100중에  3과 5의 공배수 구하기

# 1~100 까지 
setData1 = set(range(1, 101))
comMulti(3, 5, setData1)

# 또는
setData2 = set([i for i in range(1, 101) if i % 3 == 0])
setData3 = set([i for i in range(1, 101) if i % 5 == 0])
setData5 = setData2 & setData3

# 과제 3 : 리스트 데이터 활용

# 리스트 데이터
listData1 = [i for i in range(7, -8, -2)]
# 리스트 데이터를 -> 튜플 데이터로 변환
tupleData = tuple(listData1)


# 디버깅을 위한 임시 변수
temp = 0
