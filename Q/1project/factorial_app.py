#20221379 이인서 팩토리얼을 통한 재귀함수와 반복문의 차이 이해하기
import time
class FactorialApp:
    def factorial_rec(self, n):
        """재귀함수를 이용한 팩토리얼 계산"""
        if n == 0 or n == 1:
            return 1 #팩토리얼은 0! = 0이 될 수 없으므로 1로 반환
        elif n < 0:
            return "ValueError" #음수 팩토리얼은 정의되지 않으므로 ValueError 반환
        else:
            return n * self.factorial_rec(n - 1) #팩토리얼 계산(재귀)

    def factorial_iter(self, n):
        """반복문을 이용한 팩토리얼 계산"""
        result = 1
        
        if n < 0:
            return "ValueError" 
        for i in range(2, n + 1): #반복문을 통한 팩토리얼 계산
            result *= i
        return result
# ----------------------------
# 함수 정의 끝났고 테스트 코드 ---------------------
while(1): #true는 오류발생가능성이 있다고함
    print("팩토리얼 계산기 (반복/재귀) - 정수  n>=0 을 입력하세요")
    print("=================Factorial Tester==========")
    print("1) 반복법으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("3) 두 방식 모두 계산 후 결과/시간 비교")
    print("4) 준비된 테스트 데이터 일괄 실행")
    print("q) 종료")
    print("---------------------------------------")
    choice = input("선택 : ") # 입력받는 부분 scanf랑 비슷한 역할

    if choice == '1':
        n = int(input("정수 n을 입력하세요 :"))
        if n < 0:
            print("ValueError: 음수 팩토리얼은 정의되지 않습니다.")
            continue
        print("반복법 : ", FactorialApp().factorial_iter(n))
    elif choice == '2':
        n = int(input("정수 n을 입력하세요 :"))
        if n < 0:
            print("ValueError: 음수 팩토리얼은 정의되지 않습니다.")
            continue
        print("재귀법 : ", FactorialApp().factorial_rec(n))
    elif choice == '3':
        import time
        n = int(input("정수 n을 입력하세요 :"))
        if n < 0:
            print("ValueError: 음수 팩토리얼은 정의되지 않습니다.")
            continue
        
        start = time.time()
        result_iter = FactorialApp().factorial_iter(n)
        end = time.time()
        iter_time = end - start
        #시작 시간과 함수가 종료되었을 때의 시차를 구하는 과정

        start = time.time()
        result_rec = FactorialApp().factorial_rec(n)
        end = time.time()
        rec_time = end - start

        print(f"반복법 결과: {result_iter}, 시간: {iter_time:.10f}초")
        print(f"재귀법 결과: {result_rec}, 시간: {rec_time:.10f}초")
    elif choice =="q":
        print("프로그램을 종료합니다")
        break
    elif choice == '4':
        print("준비된 테스트 데이터 일괄 실행")
        test_values = [0, 1, 2, 3, 5,10, 20, 30, 50, 100]
        for n in test_values:
            print("[테스트 데이터 실행]")
            start = time.time()
            result_iter = FactorialApp().factorial_iter(n)
            iter_time = time.time() - start

            start = time.time()
            result_rec = FactorialApp().factorial_rec(n)
            rec_time = time.time() - start

            print(f"n={n}: 반복법 결과={result_iter}, 시간={iter_time:.10f}초")
            print(f"n={n}: 재귀법 결과={result_rec}, 시간={rec_time:.10f}초")
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")
