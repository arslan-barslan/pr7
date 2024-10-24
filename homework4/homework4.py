
def main():
    try:
        print("Вариант 4")
        print("x = 3*a + 3 - b + 4*c")
        print("Введите значение для a")
        a=float(input())
        print("Введите значение для b")
        b=float(input())
        print("Введите значение для c")
        c=float(input())
        if c==0 or a==0 or b==0:
            print("присутствуют  нули в переменных, вы так и хотели? Да/Нет")
            p=input()
            if p!="Да":
                print(p)
                print("Заново")
                return main()
        print("Хорошо")
        print("Ответ:X=",3*a + 3 - b + 4*c)
    except ValueError:
        print("Ощибка ввода, перезагрузка")
        return main()
main()
