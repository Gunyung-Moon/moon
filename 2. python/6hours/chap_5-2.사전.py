# Key

# cabinet = {3:"유재석", 100:"김태호"}
# # 키 == 3, 유재석 // 키 == 100, 김태호
# print(cabinet[3])
# print(cabinet[100])
# # 사전형 자료에서 값 가져오는 방법

# print(cabinet.get(3))
# # print(cabinet[5])
# print(cabinet.get(5, '사용 가능'))
# # BUT, [] 경우에는 error / .get == 값이 없을 경우 none을 return
# print('hi')

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {'A-3:'유재석', 'B-100':'김태호'}
print(cabinet)