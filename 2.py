def base(n, k):
    base_n = ""
    while n // k >= 1:
        rem = n % k
        n = n // k
        base_n = str(rem) + base_n
        if n < k :
            base_n = str(n) + base_n
    return base_n

def isPrime(num) :
    if num == 2: return True
    if num % 2 == 0 or num == 1: return False
    n = num ** 0.5
    for i in range(2, int(n) + 1) :
        if num % i == 0 :
            return False
    return True

def solution(n, k):
    converted_n = base(n, k)
    answer = 0
    num = str(converted_n).split("0")
    for i in range(len(num)):
        if num[i] != '':
            if isPrime(int(num[i])):
                answer += 1
    return answer