def is_weird(n):
    if n % 2 == 1:
        return True
    elif 2 <= n <= 5:
        return False
    elif 6 <= n <= 20:
        return True
    return False

n = int(raw_input())
print ('Not ' if not is_weird(n) else '') + 'Weird'
