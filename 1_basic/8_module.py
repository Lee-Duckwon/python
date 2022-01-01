# 파이썬 내장 모듈을 알아보자
import math
print(math.ceil(1.2))
print(math.fabs(-1.2))
# 이렇게 하면 math의 모든 메소드를 다 불러오는 격

from math import ceil, fsum
# 이렇게 쓸 것만 불러오자

import Request
indeed_result = Request.get("https://www.indeed.com/jobs?as_and=python&limit=50")

#print(indeed_result.text)

from bs4 import BeautifulSoup

indeed_soup = BeautifulSoup
(indeed_result.text, "html.parser")
print(indeed_soup)