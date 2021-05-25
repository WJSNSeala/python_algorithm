# 곱하는 정수를 배열로, 맨뒤가 1의 자리
# 123 * 456 = [3, 2, 1] * [6, 5, 4] = 56088 = [8, 8, 0, 6, 5]

def array_to_int(num: list):
    ret = 0
    for i, n in enumerate(num):
        print(i, n)
        ret = ret + 10 ** i * n

    return ret


def normalize(num: list):
    num.append(0)
    for i in range(0, len(num) - 1):
        if num[i] < 0:
            borrow = int((abs(num[i]) + 9) / 10)
            num[i + 1] = num[i+1] - borrow
            num[i] = num[i] + borrow * 10
        else:
            num[i+1] = num[i+1] + int(num[i] / 10)
            num[i] = num[i] % 10
    while len(num) > 1 and num[-1] == 0:
        num.pop()


def multiply(a: list, b: list):
    c = [0 for i in range(len(a) + len(b) + 1)]

    for a_idx in range(len(a)):
        for b_idx in range(len(b)):
            c[a_idx + b_idx] += a[a_idx] * b[b_idx]
    normalize(c)
    return c


c = multiply([1, 1, 1], [2, 3, 4, 5])
print(111 * 5432)
print(array_to_int(c))
