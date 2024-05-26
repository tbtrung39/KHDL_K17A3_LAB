def doi_co_so(n, base):
    """Chuyển đổi số n sang cơ số base"""
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    digits = digits[::-1]
    return ''.join(str(digit) for digit in digits)

def doi_tu_he_10_sang_he_2(n):
    """Chuyển đổi số từ hệ 10 sang hệ 2"""
    return doi_co_so(n, 2)

def doi_tu_he_10_sang_he_16(n):
    """Chuyển đổi số từ hệ 10 sang hệ 16"""
    hex_digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(hex_digits[int(n % 16)])
        n //= 16
    digits = digits[::-1]
    return ''.join(digits)