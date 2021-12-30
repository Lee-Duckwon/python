# definition 
# 파이썬에서는 띄어쓰기가 굉장히 중요하다 
# {}이런거로 시작과 끝을 판단하지 않고 들여쓰기로 판단해. function의 바디 안을 띄어쓰기로 표현한다.
def say_hello(who):
  print("hello", who)
print("bye") # 위 print와는 전혀 달라 say_hello를 호출하지 않으면 bye만 계속 뜰거야

say_hello("Sam")
     