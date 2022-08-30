'''
조건 : if
순환 : for, while, do while
제어 : continue, break

if 조건 [or, and 조건1] : -> 논리
    조건이 True일 경우 처리
'''

number = 3
if number > 0 :
    print('number는 양수') # 줄 바꿈에 주의해라 { }로 되어있지 않음
if number < 0 :
    print('number는 음수 입니다.')
if number == 3 :
    print('number는 3입니다')

number = int(input("정수입력 > "))
print(type(number))
if number % 2 == 0 :
    print('짝수입니다')
if number % 2 != 0 :
    print('홀수입니다')

'''
module : 다른 사람이 먼저 제작해 놓은 기능
'''

import datetime
now = datetime.datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.second)

if now.hour < 12 :
    print('현재 시간은 {}시로 오전입니다.'.format(now.hour))

## setter
setTime = datetime.datetime.strptime('2022-12-24 12:35:45','%Y-%m-%d %H:%M:%S')
print(setTime)

setTime = datetime.datetime.strptime('20221224123546','%Y%m%d%H%M%S')
print(setTime)

## 조건분기 (다수조건)
month = setTime.month
if month >= 3 and month <= 5:
    print('현재는 봄입니다')
elif 6 <= month <= 8 :
    print('현재는 여름입니다')
elif 9 <= month <= 11 :
    print('현재는 가을입니다')
else :
    print('현재는 겨울입니다')


'''
조건값은 만족했는 데 처리가 설정되지 않는 경우
'''

number = 5
if number > 0 :
    # 양수일 경우
    pass
else : 
    # 음수일 경우
    pass

## array (배열)
'''
array : 같은 자료형 변수의 묶음
    array = []
    array = [1, 2, 3]
    array[0] -> 1
    array[1] -> 2
    array[2] -> 3

list : 유동적(추가, 삭제)인 배열
'''

number = 1
number1 = 1
number2 = 2
number3 = 3

## tuple : 대입, 변경불가, 추가, 삭제불가
tu = (11, 22, 33) # 예약어
print(tu)
print(tu[0])

mylist = [0, 3 , 2 ,1]
print(mylist[2:])

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a + list_b)

list_a.insert(2, 5)
print(list_a)

list_a.extend(list_b)
print(list_a)

## CRUD = Data access object
## 추가, 삭제, 검색, 수정
## Create, Delete, Read, Update

list_a.pop(2)
print(list_a)

mylist = [ 11, 22, 33, 44, 55]
# print(33 in mylist)
# if 33 in mylist :
#     print('데이터가 있음')

# mylist[3] = 66
# print(mylist)

# mylist = [1, 9, 2, 8, 3, 7, 4]
# mylist.sort()
# print(mylist)

# mylist.sort(reverse=True)
# print(mylist)

# ## dictionary
# '''
# array, turple, list -> 접근(access) 
#  : index 0 ~ len -1
# list key -> index
#     value -> list[key]

# dictionary
#     key -> str
#     value -> object(class, list, tuple, str, int)
# '''
# dic = {
#     'name': '과일',
#     "fruits": ['사과','배','바나나'],
#     'orgin': '필리핀'
# }
# print(dic)
# print(dic['name'])
# print(dic['fruits'])
# print(
#     dic['fruits'][1]
# )
# dictionary는 키로 구성된다.

# mylist = [] # list 선언
# mylist.append('hi')
# mylist.append('good day')
# print(mylist)

# # dictionary 선언
from re import I


dic = {}
dic['name'] = '로보트'
dic['head'] = '스킨헤드'
dic['body'] = '메탈바디'
dic['weapon'] = ['미사일', '광선검', '레이저']

# print(dic)
# del dic['head']
# print(dic)

# if 'weapon' in dic:
#     print('무기가 있습니당')
# value = dic.get('name')
# print(value)

# value = dic.get('head')
# if value == None :
#     print('존재하지 않는 키값에 접근했습니다.')

# print(dic['name'])
# print(dic.get('name'))

# ## range

# mylist = list(range(5))
# print(mylist)
# a = list(range(0, 5))
# print(a)
# b = list(range(0, 10, 2))
# print(b)
# c = list(range(0, 10, 3))
# print(c)

# for i in range(10) :
#     print(i)

# _sum = 0
# for i in range(1, 11) :
#     _sum += i
# print(_sum)

# mylist = ['one', 'two', 'three', 'four', 'five']
# for a in mylist :
#     print(a)

# for i in range(0, 10, 2) :
#     print(i)

# mylist = [11, 22, 33, 44, 55]
# for i in len(mylist) :
#     print(i)
# for i in reversed(range(len)mylist) :
#     print(i)    

## enumerate
fruits = ['apple','pear','banana']

# index, value
for i, val in enumerate(fruits):
    print(i, val)

for key in dic :
    print(key, ":", dic[key])


for i in fruits:
    if i == 'apple':
        print(i)

# 1 ~ 100 사이의 숫자 안에 짝수, 홀수의 합을 각각 구하라
sum1 = 0
sum2 = 0
for i in range(1, 101) :
    if i % 2 == 0 :
        sum2 += i
    else :
        sum1 += i
print('홀수의 합: ', sum1)
print('짝수의 합: ', sum2)

### While
'''
for 변수 in (배열, 범위) :
    처리

# 반면 while의 경우
변수선언
    while 조건 : 조건이 True 이면 계속 실행
    처리
    연산
 
'''
w = 0
while w < 10 :
    print(w)
    w += 1

print(mylist)

# val = 22
# while val in mylist :
#     print(val)

### break : loop 문과 같이 사용, for, while
mylist = [1, 2, 3, 4, -2, 6, -4]
for n in mylist : 
    if n < 0 :
        break
    print(n)

myNumber = [] # -> 5개 : 양수만 입력해야 된다.
w = 0
while w < 5:
    num = int(input('숫자입력 > '))
    if num <= 0:
        print('다시 입력해 주십시오')
        continue
    myNumber.append(num)
    w += 1
print(myNumber)