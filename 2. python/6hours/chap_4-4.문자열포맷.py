# 문자열포맷

print('a' + 'b')
print('a', 'b')

# 방법 1 == %를 이용
print('나는 %d살입니다.' % 20) #d는 정수값만 가능.
print('나는 %s을 좋아해요.' % '파이썬') #s는 문자열만 가능.
print('Apple은 %c로 시작해요.' % "A") #c = haracter라서 한 글자만 받음.
print('나는 %s살입니다.' % 20)
# %s는 만능
print('나는 %s색과 %s색을 좋아해요.' % ('파란', '빨간'))

# 방법 2 == 중괄호를 이용
print('나는 {}살 입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란','빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란','빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란','빨간'))

# 방법 3 ==
print('나는 {age}살이며, {color}색을 좋아해요.').format(age = 20, color = '빨간')

# 방법 4 (v3.6 이상~)
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.') # print문에 f를 붙여서 사용.ㄹ