
# Створіть функцію def double_zero(array) яка приймає цілочисельний масив і дублює всі нулі,
# повертаючи новий масив в якому нулі продубльювані, при дублювані всі інші елементи
# повинні бути зсунутті вправо.
#
# Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми,
# або за допомогою input() або в результаті викликів функції. Але в файлі double_zero.py
# повина бути створена функція def double_zero(array) яка виконує необхідну логіку.
#
# Приклади:
#
# double_zero([1,0,2,3,0,4,5,0]) -> [1,0,0,2,3,0,0,4,5,0,0]
# double_zero([1,0,2,3,0,4,5,0]) -> [1,0,0,2,3,0,0,4,5,0,0]
# double_zero([1,2,3]) -> [1,2,3]

def double_zero(list):
    list=[1,0,2,3,0,4,5,0]
    if list[i]==0:
        list.add[i+1]=0
        print(newlist)
    else:
        print(list)
    return double_zero(list)

