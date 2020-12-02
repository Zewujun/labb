
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


def enc(mx, r, cx, e):
    a = mx << r + cx
    b = a ^ e
    return a, b


def div_s(b, gx):
    if len(bin(gx)) < len(bin(b)):
        return b
    tmp = gx << len(bin(b)) - len(bin(gx))
    sx = b ^ tmp
    while len(bin(sx)) >= len(bin(gx)):
        tmp = gx << len(bin(sx)) - len(bin(b))
        sx = sx ^ gx
    return sx


def main():
    gx = int(input('Введите порождающий многочлен: '))
    l, k, m = data()
    r = len(bin(gx))-1
    e = int(input('Введите вектор ошибки: '))
    mx = m << r
    cx = div_c(gx, mx)
    p = 0, 1
    ax = (mx << r) + cx
    b = ax ^ e
    sx = div_s(b, gx)
    if sx == 0 and e != 0:
        print('Ошибок не обнаружено')
    else:
        print('Ошибка обнаружена')


if __name__ == '__main__':
    main()