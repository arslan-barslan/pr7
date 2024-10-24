def convert(frac, start=10, fin=0):
    if start == fin or frac == 0:
        return ""
    frac *=6
    part = int(frac)
    new_frac = frac - part
    return str(part) + convert(new_frac, start, fin + 1)

def convert_ii(n):
    if n == 0:
        return ""
    return convert_ii(n // 6) + str(n % 6)


def main():
    print("введите значение (дробная часть работает тоже с точностью до 10)")
    value=float(input())
    flag=""
    if value<0:
        value= value*-1.0
        flag="-"
    if value is None:
        print("значение не введено")
        return 1
    try:
        i, d = divmod(value, 1)
        if d>0.0:
            ans=(str(convert_ii(int(i)))+','+convert(d))
        else:
            ans=(convert_ii(int(i)))
        print("Ответ")
        print(flag+ans)
        return 0
    except ValueError:
        print("Неверное значение")
        return main()
main()
