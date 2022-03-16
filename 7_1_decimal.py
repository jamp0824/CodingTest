def is_prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False    
    return True

def print_prime(n):
    print(is_prime(n))
    if is_prime(n):
        print(f"{n}은 소수입니다.")
    else:
        print(f"{n}은 소수가 아닙니다.")
    
print_prime(97)
print_prime(100)
    