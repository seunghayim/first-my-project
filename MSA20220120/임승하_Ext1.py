def personalScore(dic, name):
    total = 0
    scoreData = dic.values()
    studentNum = len(dic)

    for score in scoreData:
        if type(score) != str:
            total += score

    return [name, total, total/studentNum]
  
  
hong1 = {'국어': 95, '영어': 90, '수학': 80, '과학': 50,}
hong2 = {'국어': 100, '영어': 50, '수학': 90, '과학': 90,}
hong3 = {'국어': 99, '영어': 60, '수학': 100, '과학': 40,}
hong4 = {'국어': 55, '영어': 80, '수학': 80, '과학': 60,}

# 개인별 총점 / 평균
data1 = personalScore(hong1, '홍길동1')
data2 = personalScore(hong2, '홍길동2')
data3 = personalScore(hong3, '홍길동3')
data4 = personalScore(hong4, '홍길동4')

# 전체 점수 / 전체 평균
totalScore = data1[1] + data2[1] + data3[1] + data4[1]
totalMean = (data1[2] + data2[2] + data3[2] + data4[2]) / 4
