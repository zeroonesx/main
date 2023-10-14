# 001 print 기초
# 화면에 Hello World 문자열을 출력하세요.

#print("Hello World")
#print('Hello World')

# 008 print 기초
#print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/samsung
#print("naver", "kakao", "sk", "samsung", sep="/")

#005 print 탭과 줄바꿈
#다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
#print("안녕하세요.\n 만나서\t\t반갑습니다.")

#009 print 줄바꿈
#다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 
#세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.

#print("first"); print("second")


#011 변수 사용하기
#삼성전자라는 변수로 50,000원을 바인딩해보세요. 
#삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.

#samgsung = 50000
#total = samgsung * 10
#print(total)

#012 변수 사용하기
#다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.

#항목	값
#시가총액	298조
#현재가	50,000원
#PER	15.79

시가총액 = 100
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))