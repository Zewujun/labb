import random
import numpy as np


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
    return cx


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


def main():
    gx = (input('Введите порождающий многочлен: '))[::-1]
    gx = int(gx, 2)
    l, k, m = data()
    r = len(str(gx)) - 1
    mx = m << r
    print('m(x) = ', format(mx, '07b'))
    cx = div_c(gx, mx)
    ax = (mx << r) + cx
    print('a(x) = ',  format(ax, '07b'))
    e = random.getrandbits(l)
    print('e(x) = ', format(e, '07b'))
    b = ax ^ e
    print('b(x) = ', format(b, '07b'))
    sx = div_s(b, gx)
    print('s(x) = ', sx)
    if sx == 0:
        print('Ошибок не обнаружено')
    else:
        print('Ошибка обнаружена')


if __name__ == '__main__':
    main()
