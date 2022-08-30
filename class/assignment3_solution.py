# 2,4,6,8,10 값을 각각 제곱 한 값을 출력하라

doubleList = []
for n in range(2, 12, 2):
    print(n**2)
    doubleList.append(n**2)
print(doubleList)

# while 문을 이용하여 10에서 50까지의 짝수만 출력하라

# num = 10
# while num <= 50:
#     print(num)
#     num += 2

# 0-9의 값을 for 문을 사용하여 하나씩 표시. 그러나 7이되면 루프를 종료

for i in range(10):
    if i == 7:
        break
    print(i)

# 0-9의 값을 하나씩 표시하라. 그러나 4의 경우는 표시하지 않는다. (continue를 사용)

for i in range(10):
    if i == 5:
        continue # continue 이후이 코드는 생략
    print(i)

# pass를 사용하여 0 ~ 9의 값을 하나씩 표시하라. 그러나 4의 경우는 표시하지 않는다 (pass를 사용)

for i in range(10):
    if i == 4:
        pass
    else:
        print(i)

# 1 ~ 10까지 목록에 저장하고 각각의 값을 제곱 한 값을 출력하라

list1 = list(range(1, 11))
for i in list1:
    print(i**2)

# 다음 dictionary 객체를 사용하여 각각의 key와 value를 가져오고 
# value가 20 이상인 경우 {key의 내용} : hot을 출력한다. 그 외의 경우 {key의 내용} : cold 출력하라
temperatures = { 'x': 24, 'y': 18, 'z': 30 }

for key, value in temperatures.items():
    # print(key, value)
    if value >= 20:
        print(key, ": hot")
    else:
        print(key, ": cold")

# (1,2,3)의 튜플의 값을 x, y, z 변수에 각각 저장하라.

x = 1
y = 2
z = 3
x, y, z = (1, 2, 3)
print(x, y, z)

'''
목록 (결합)
변수 li1에 [1,2,3]목록을 대입 변수 li2에 [4,5]목록을 할당하고 두 목록을 결합하여 출력합니다.

출력 :[1,2,3,4,5]
'''

li1 = [1, 2, 3]
li2 = [4, 4]
li3 = li1 + li2
print(li3)

'''
목록 (추가)
변수 목록 [1,2,3,4,5]을 할당하고이 목록의 끝 으로 6, 7하나씩 차례로 추가하십시오. 그 후, 최종 목록을 출력합니다.

출력 :[1,2,3,4,5,6,7]
'''

li = [1, 2, 3, 4, 5]
li.append(6)
li.append(7)
print(li)


'''
목록 (insert)
변수 목록 [1,2,3,4,5]을 만들고 0 번째와 1 번째 사이에 100 을 삽입하십시오.

출력 :[1,100,2,3,4,5]
'''
li = [1, 2, 3, 4, 5]
li.insert(1, 100)
print(li)


'''
정렬
변수 목록 [5,3,1,4,2]을 저장하고 오름차순으로 정렬 된 목록을 출력합니다.

출력 :[1,2,3,4,5]
'''
li = [1, 2, 3, 4, 5]
sort_li = sorted(li)
print(sort_li)

rsort_li = sorted(li, reverse=True)
print(rsort_li)

'''
목록 (for 의한 조사)
변수에 [1,2,3,4,5] 5 개의 요소를 가진 리스트를 포함하여 짝수의 요소만을 출력합니다.

출력: 2 4
'''
li = [1, 2, 3, 4, 5]
for n in li:
    if n % 2 == 0:
        print(n)
# append 이용해서 list 만들어보기

'''
목록 (enumerate)
변수에 [1,2,3,4,5] 5 개의 요소를 가진리스트를 포함하여 짝수가 들어 있는 요소의 index만을 출력합니다. 

예상 출력 :1 3
'''

# li = [1, 2, 3, 4, 5]
# for idx, val in enumerate



'''
사전 (values)
변수에 값 쌍으로 {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}를 가진 사전을 포함하여 
키를 요소로 하는 리스트와 값을 요소로 하는 리스트를 작성하고 출력하십시오.

['A', 'B', 'C', 'D', 'E']
[1, 2, 3, 4, 5]
'''
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
key_list = list(dic.keys())
print(key_list)
val_list = list(dic.values())
print(val_list)



'''
변수에 값 쌍으로 {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}를 가진 사전을 포함하여 
키와 값 (가치)의 조합 튜플을 요소로 하는 리스트를 작성하고 출력하십시오.

출력 :[('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)]
'''
dic ={'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
mylist = list(dic.items())
print(mylist[0][1])