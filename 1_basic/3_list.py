students = ["sam", "owen", "edgar"]
grades = [2, 1, 3]
print(students[grades[1]])
print(len(students)) #원소 수
print(min(grades)) #가장 작은 값 
print(max(grades)) 

import statistics # 통계 임포트
print(statistics.mean(grades)) # 평균 구하기

import random
print(random.choice(students)) # 랜덤 뽑기

days = ["Mon","Tue","Wed","Thur","Fri"]
print(type(days)) # list
days.reverse()