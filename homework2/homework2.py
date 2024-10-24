def convert(frac, start=10, fin=0):
    if start == fin or frac == 0:
        return ""
    frac *= 2
    part = int(frac)
    new_frac = frac - part
    return str(part) + convert(new_frac, start, fin + 1)


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
            ans=(str(bin(int(i)))+','+convert(d))
        else:
            ans=(bin(int(i)))
        print("Ответ")
        print(flag+ans[2:])
        return 0
    except ValueError:
        print("Неверное значение")
        return main()
main()
