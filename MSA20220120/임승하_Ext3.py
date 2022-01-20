# 클래스
class MeanScore:
    # 인스턴스한 객체의 (총 과목수, 총 누적 점수) 
    __count = 0
    __allTotal = 0

    def __init__(self, data):
        self.data = data
        MeanScore.__count += len(self.data)
        MeanScore.__allTotal += sum(self.data.values())
        
    
    # 개인 이름 입력시, 이름/ 총점/ 평균 리턴 
    def personalScore(self, name):
        total = 0
        value = self.data.values()
        for score in value:
            total = total + score
        return f'이름: {name} / 점수 합계:{total} / 평균:{total / len(self.data)}'


    # 인스턴스 한 객체 수에 대한 전체 점수 및 전체 평균 리턴  
    def peopleScore(self):
        allScore = MeanScore.__allTotal
        allMean = MeanScore.__allTotal / MeanScore.__count
        return f'전체 총점: {allScore} 전체 평균: {allMean}'
        

# test
if __name__ == '__main__':        
    # dic 값들
    hong1 = {'국어': 95, '영어': 90, '수학': 80, '과학': 50,}
    hong2 = {'국어': 100, '영어': 50, '수학': 90, '과학': 90,}
    hong3 = {'국어': 99, '영어': 60, '수학': 100, '과학': 40,}
    hong4 = {'국어': 55, '영어': 80, '수학': 80, '과학': 60,}
    
    # 각각 인스턴스 하여 객체 생성
    data1 = MeanScore(hong1)
    data2 = MeanScore(hong2)
    data3 = MeanScore(hong3)
    data4 = MeanScore(hong4)

    # personalScore 함수를 이용하여 개인 총점 및 평균을 구함
    result1 = data1.personalScore('홍길동1')
    result2 = data2.personalScore('홍길동2')
    result3 = data3.personalScore('홍길동3')
    result4 = data4.personalScore('홍길동4')
    
    # people함수를 이용하여 4개의 객체에 대한 전체 총점 및 전체 평균을 result5에 저장
    result5 = data4.peopleScore()
    
    # 디버깅을 위한 임시 변수
    temp = 0





