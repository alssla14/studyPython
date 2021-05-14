#문자열 실습
#내장함수 : 파이썬 안에 자체적으로 내장되어 있는 함수

#문자열 덧셈
str = "멋쟁이 사자처럼"
str2 = "은 좋은 동아리 입니다."

#print(str+str2)

#문자열의 곱셈
#print(str*3)

#문자열의 인덱싱 - 문자열 일부분 추출 / 첫번째 글자는 0부터 생각
#print(str[4])
#print(str[6])

#문자열의 슬라이싱 - 일부 문자를 범위로 접근
#print(str[0:6])

#1_문자열의 길이를 구하는 내장함수 : len (문자열 변수) 0이 아니라 1부터 셈
#print(len(str))

#2_문자열 내에서 특정 문자의 등장 횟수의 반환하는 내장함수 : 문자열변수.count('특수문자')
str3 = "멋쟁이 사자처럼은 사랑스러워"
#print(str3.count('사'))

#3_문자열을(특정 기준으로)나누는 내장함수 : 문자열변수.split()
#print(str3.split()) #공백 기준

str4 = "사과,바나나,포도"
#print(str4.split(','))

#4_특정 문자 인덱스를 찾아주는 내장함수 : find('문장'), index('문장')
#print("find: ",str3.find('사'))
#print("index: ",str3.index('사'))

#find와 index의 차이점
#오류가 발생했을 때, find는 -1을 반환하고, index는 ValueError라는 오류를 발생시킵니다.
print("find: ",str3.find('무'))
print("index: ",str3.index('무'))