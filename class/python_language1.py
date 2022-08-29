'''
출력
'''

# 주석문 : 컴파일되지 않는다. 설명문
# 한 줄 주석문

'''
범위주석문
'''

"""
범위 주석문
"""

print('hello python')
print("이름     나이    지역")
print("""
ㅇㅂㅇ
존나
배고파
""")
print('안녕하세요' * 3)
print('안녕하세요'[0]) # 0번지
print('안녕하세요'[1]) # 1번지
# print('안녕하세요'[5]) # 5번지 # 범위값 밖이라 error 메세지 띄움
print('안녕하세요'[-1]) # 뒤에서 -1 번지
print('안녕하세요'[-2]) # 뒤에서 -2 번지
print('안녕하세요'[2:5]) # 2~5 번지

print(len('안녕하세요')) # length == 길이
print(type('안녕하세요')) # string == 문자열
print(type(len('안녕하세요'))) # integer == 정수
print(type(123.456)) # float == 소수
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(3 // 2) # 몫(정수)
print(3 / 2)
print(3 ** 2 ) # 지수

'''
입력
'''
# s = input('당신의 키는 얼마입니까?')
# print(s)

num = str(34)
print(type(num))

'''
자료형
    정수, 실수(소수)
    문자열  "안녕하세요"
    논리형  True, False
    날짜형 '2022/08/29'
'''

numStr = 123
print(numStr)
print(type(numStr))

name = '홍길동'
print(name)
print(type(name))

floatNum = 123.456
print(floatNum)
print(type(floatNum))

boolVar = True
print(boolVar)
print(type(boolVar))

# 변수명명법 규칙
# 0ab = 123 == 숫자는 불가능
ab0 = 123
# 너무 간단히 기입을 안 하는 것이 좋다.

# str == 변수명으로 사용하지 말자!
str_a = "Hello Python Programming"
str_b = str_a
print(str_b)

'''
문자열 자르기
'''
str_split = str_b.split(" ")
print(str_split[0])

str_b = "2022/12/25"
str_split = str_b.split("/")
print("몇 월 입니까? " + str_split[1] + "월 입니다.")

str_b = "2022-12-25"
str_split = str_b.split("-") # token
print(str_split)
print(':'.join(['15', '22', '25'])) # []를 붙여서 list화

str_a = "    Python Python     Python            "
print(str_a.split())
print(str_a.replace(' ',''))

# 문자열 조사 == 영어, 한글, 숫자로 되어 있으면 True
print("TrainA10한글".isalnum()) 
# 숫자로 되어있는지 조사
print("123".isdigit())
out_str = "하이안녕안녕하세요".find("안녕") # 앞에서 찾아들어감.
print(out_str)
out_str = "하이안녕안녕하세요".rfind("안녕") # 뒤에서 찾아들어감.
print(out_str)

### 논리 True of False ###
print(10 == 100)
print(10 == 20)
print(10 != 100)
print(10 >= 100)
print("가방" < "하마") # ㄱㄴㄷㄹㅁ 순에 의해서 True

x = 5
print(x > 0 and x < 10)
print(x < 6 or x > 10)
print(0 < x < 10) # 파이썬에선 가능
