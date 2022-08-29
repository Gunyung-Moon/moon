# 1번

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 // 2) # 몫
print(5 % 2) # 나머지
print(5 / 2) # 나누기(소수)

# 2번
str_1 = 'some1'
print(str_1.replace('1','one'))

# 3번.
str_2 = 'How many characters?'
print(len(str_2))

# 4번.
a = '34'
b = '43'
print(int(a) + int(b))
# print(type(c)) == int

# 5번.
score_eng = input('영어 성적을 입력하세요. ') # input 앞에 int를 붙여서 숫자화 해서 쓸 수도 있음
score_math = input('수학 성적을 입력하세요. ')
print('영어 점수 : ', score_eng)
print('수학 점수 : ', score_math)
# print(type(score_eng)) # str 타입이라 계산이 안 됨.
score_sum = int(score_eng) + int(score_math)
print('합계 :', score_sum)
subject_num = len([score_eng, score_math])
score_avg = score_sum / subject_num
print('평균 :', score_avg)

# 5-1번. input 앞에 int로 숫자타입화.
score_eng = int(input('영어 성적을 입력하세요. '))
score_math = int(input('수학 성적을 입력하세요. '))
print('영어 점수 : ', score_eng)
print('수학 점수 : ', score_math)
# print(type(score_eng)) # str 타입이라 계산이 안 됨.
score_sum = score_eng + score_math
print('합계 :', score_sum)
subject_num = len([score_eng, score_math])
score_avg = score_sum / subject_num
print('평균 :', score_avg)