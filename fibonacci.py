starNumber = int(raw_input("Enter the start number here")
endNumber = int(raw_input("Enter the end number here"))

def fib(n): 
    if n <2:
        return n 
    return fib(n-2) + fib(n-1)

    print map(fib, range(startNumber, endNumber))
    """
    피보나치 수열을 계산하는 함수를 작성하시오. 피보나치 수의 정의는 아래와 같다.

    f(n) = 0 if n = 0
    f(n) = 1 if n = 1
    f(n) = f(n-1) + f(n-2) if n > 1

    단 n에는 0 이상의 정수가 입력되는 것으로 가정하라.
    """
    
    return 0


for i in range(11):
    print("f(%d) = %d" % (i, fibonacci(i)))

""" 수행 예: 
f(0) = 0
f(1) = 1
f(2) = 1
f(3) = 2
f(4) = 3
f(5) = 5
f(6) = 8
f(7) = 13
f(8) = 21
f(9) = 34
f(10) = 55
"""
