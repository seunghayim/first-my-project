def personalScore2(dic, name):
    total = 0
    scoreData = list(dic.values())
    studentNum = len(dic)
    i = 0
    while i < len(dic):
        total += scoreData[i]
        i += 1
    return [name, total, total/studentNum]
  
  
hong1 = {'국어': 95, '영어': 90, '수학': 80, '과학': 50,}
hong2 = {'국어': 100, '영어': 50, '수학': 90, '과학': 90,}
hong3 = {'국어': 99, '영어': 60, '수학': 100, '과학': 40,}
hong4 = {'국어': 55, '영어': 80, '수학': 80, '과학': 60,}


data1 = personalScore2(hong1, '홍길동1')
data2 = personalScore2(hong2, '홍길동2')
data3 = personalScore2(hong3, '홍길동3')
data4 = personalScore2(hong4, '홍길동4')

totalScore = data1[1] + data2[1] + data3[1] + data4[1]
totalMean = (data1[2] + data2[2] + data3[2] + data4[2]) / 4
