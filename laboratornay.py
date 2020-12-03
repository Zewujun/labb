import random


def data():
    l = int(input('Введите длину сообщения: '))
    k = (input('Введите число k: '))
    m = int(input('Введите сообщение: '))
    return l, k, m


def div_c(gx, mx):
    r = len(bin(gx)) - 1
    if len(bin(gx)) < len(bin(mx)):
        return mx
    tmp = gx << len(bin(mx)) - len(bin(gx))
    cx = mx ^ tmp
    while len(bin(cx)) >= len(bin(gx)):
        tmp = gx << len(bin(cx)) - len(bin(mx))
        cx = cx ^ gx
        print('c ='.format(bin(cx)))
    return cx


def binaryGenerator(l, r):
    e = []
    n = l + r
    for i in range(0, n):
        e = random.randint(0, 100)
    return e


def div_s(b, gx):
    if len(bin(gx)) < len(bin(b)):
        return b
    tmp = gx << len(bin(b)) - len(bin(gx))
    sx = b ^ tmp
    while len(bin(sx)) >= len(bin(gx)):
        tmp = gx << len(bin(sx)) - len(bin(b))
        sx = sx ^ gx
    return sx


def enc(mx, r, cx, e):
    a = mx << r + cx
    b = a ^ e
    return a, b


def main():
    gx = (input('Введите порождающий многочлен: '))[::-1]
    gx = int(gx, 2)
    l, k, m = data()
    r = len(str(gx)) - 1
    mx = m << r
    print("{0:b}".format(mx))
    cx = div_c(gx, mx)
    ax = (mx << r) + cx
    print("{0:b}".format(ax))
    e = binaryGenerator(l, r)
    print("{0:b}".format(e))
    b = ax ^ e
    sx = div_s(b, gx)
    if sx == 0 and e != 0:
        print('Ошибок не обнаружено')
    else:
        print('Ошибка обнаружена')


if __name__ == '__main__':
    main()
