import random


def data():
    l = int(input('Введите длину сообщения: '))
    k = (input('Введите число k: '))
    m = int(input('Введите сообщение: '))
    return l, k, m


def div_c(gx, mx):
    r = len(bin(gx)) - 1
    xg = len(bin(gx))
    xmx = len(bin(mx))
    if xg < xmx:
        return mx
    tmp = gx << (xmx - xg)
    cx = mx ^ tmp
    while len(bin(cx)) >= xg:
        tmp = gx << len(bin(cx)) - xg
        cx = cx ^ gx
        print('c ='.format(bin(cx)))
    return cx


def binaryGenerator(l, r):
    e = []
    n = l + r
    for i in range(0, n):
        e = random.randint(16, 31)
    return e


def div_s(b, gx):
    xb = len(bin(b))
    xg = len(bin(gx))
    if xb < xg:
        return b
    tmp = gx << (xb - xg)
    sx = b ^ tmp
    while len(bin(sx)) >= xg:
        tmp = gx << len(bin(sx)) - xg
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
    print('m(x) = ', "{0:b}".format(mx))
    cx = div_c(gx, mx)
    ax = (mx << r) + cx
    print('a(x) = ',"{0:b}".format(ax))
    e = binaryGenerator(l, r)
    print('e(x) = ',"{0:b}".format(e))
    b = ax ^ e
    print('b(x) = ', "{0:b}".format(b))
    sx = div_s(b, gx)
    if sx == 0 and e != 0:
        print('Ошибок не обнаружено')
    else:
        print('Ошибка обнаружена')


if __name__ == '__main__':
    main()
