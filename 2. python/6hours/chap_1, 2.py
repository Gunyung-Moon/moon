# 2-1 숫자형 자료
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3&(3+1))

# 2-2 문자형 자료
print('풍선')
print('나비')
print('ㅋ'*9)

# 2-3 boolean = 참과 거짓
print(5 > 10)
print(5 < 10)

print(True)
print(False)
print(not True)
print(not (5 > 10))

# 2-4 변수

# 애완동물을 소개해 주세요~
# print('우리집 강아지의 이름은 연탄이에요')
# print('연탄이는 4살이며, 산책을 아주 좋아해요')
# print('연탄이는 어른일까요? True')

animal = '강아지'
name = '연탄이'
age = 4
hobby = '낮잠'
is_adult = age >= 3
# age는 정수형 자료라서 따음표 없이

print('우리집' + animal + '이름은' + 'name' + '에요')
hobby = '축구'
# print(name + '는' + str(age) + '살이며, ' + hobby + '을 아주 좋아해요')
print(name, '는' + str(age), '살이며, ',  hobby, '을 아주 좋아해요')
print(name + '는 어른일까요? ' + str(is_adult))

''' 주석처리의 다른 방법
 함수를 합치는 건 꼭 + 뿐만 아니라 , 로도 가능하다. 띄어쓰기가 하나가 들어가고 이 경우에는 str로 안 묶어도 된다.)
 boolean과 정수형 자료는 str로 감싸야한다. 
'''
hobby = '야스'

'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오.

변수명
: station

변수값 
: '사당', '신도림', '인천공항' 순서대로 입력

출력 문장
: xx행 열차가 들어오고 있습니다.
'''

station = '사당', '신도림', '인천공항'
print(station, '행 열차가 들어오고 있습니다.')