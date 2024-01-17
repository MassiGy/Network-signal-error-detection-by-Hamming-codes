
def reverse(string):
    string = string[::-1]
    return string


def isPowerOfTwo(n:int) -> bool:
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True
