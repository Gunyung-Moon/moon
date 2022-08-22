python = "Python is Amazing"
print(python.lower()) # 모든 문자 소문자
print(python.upper()) # 모든 문자 대문자 처리
print(python[0].isupper()) # isupper == 대문자가 맞니 라고 묻는 거, [0]: 첫번쨰 글자
print(len(python)) # len == 길이 반환
print(python.replace("Python","Java"))

# index == 찾기

index = python.index("n") 
print(index)

index = python.index("n", index +1) #index의 시작값이 1부터 (기본값은 = 0)
print(index)

print(python.find("Java"))
# print(python.index("Java"))
print("hi")

''' 
find와 index의 다른 점은 find는 error일 경우 -1을 반환, 반면 index는 error
'''

print(python.count("n"))