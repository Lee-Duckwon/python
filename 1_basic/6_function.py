# definition 
# 파이썬에서는 띄어쓰기가 굉장히 중요하다 
# {}이런거로 시작과 끝을 판단하지 않고 들여쓰기로 판단해. function의 바디 안을 띄어쓰기로 표현한다.
def say_hello(who):
  print("hello", who)
print("bye") # 위 print와는 전혀 달라 say_hello를 호출하지 않으면 bye만 계속 뜰거야

say_hello("Sam")

def plus(a, b):
  return a + b

def say_hi(name, age):
  return f"Hello {name} you are {age} years old"
# f는 format을 나타낸다 f를 넣고 {}를 통해 인자를 스트링 안에 넣을 수 있다. 자바스크립트의 ${}와 같은 것 같다
# 물론 "Hello" + name + 이런식으로 할 수 있다

hi = say_hi("nico", "12")
print(hi)
      

def minus(a, b):
  return a - b

minus(12, "10") # 이러면 에러가 뜬다 에러 핸들링이 필요하다 아래와 같이 설정을 할 수 있다.

def minus2(a,b):
  if type(b) is int or type(b) is float:
    return a - b
  else:
    return None

def age_check(age):
  print(f"you are {age}")
  if age <18:
    print("you cant drink")
  elif age == 18 or age == 19:
    print("you are new to this!")
  elif age > 20 and age < 25:
    print("you are still kind of young")
  else:
    print("enjoy your drink")
print(age_check(18))