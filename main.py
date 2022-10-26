import sys


def myAtoi(s: str) -> int:
    i, base, sign = 0, 0, 1

    # handle the case where s contains no digits (or input is malformed)
    if not (set(s) & set('0123456789')):
        return 0

    # increment past whitespace (ignore)
    while s[i] == ' ':
        i += 1

    # compute sign (2s complement)
    if s[i] == '-' or s[i] == '+':
        sign = 1 - 2 * (s[i] == '-')
        i += 1

    # loop as long as the next input is a digit
    while i < len(s) and '0' <= s[i] <= '9':

        # test for overflow
        if (base > (sys.maxsize // 10) or
                (base == (sys.maxsize // 10) and
                 (ord(s[i]) - ord('0')) > 7)):

            if sign == 1:
                return sys.maxsize
            else:
                return -(sys.maxsize) - 1

        base = 10 * base
        base += (ord(s[i]) - ord('0'))
        i += 1

    return base * sign


if __name__ == "__main__":
    s: str = input("Enter your number : ")
    val: int = myAtoi(s)
    print(val)
