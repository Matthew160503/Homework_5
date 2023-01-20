# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
a = '111112222334445'
b = 'AAAAAAFDDCCCCCCCAEEEEEEEEE'

def code(text):
    text = text + " "
    first_symbol = text[0]
    count = 0
    res=''
    for i in text:
        if i == first_symbol:
            count += 1
        else:
            res +=f'{count}{first_symbol}'
            count = 1
            first_symbol = i
    return res

A = code(a)
B = code(b)
print('Сжатие:')
print(A)
print(B)

def reverse_code(text):
    result = ''
    temp = 0
    for i in range(0,len(text)):
        if i % 2 == 0:
            temp = int(text[i])
        else:
            result += temp*f'{text[i]}'
    return result
print('Восстановление:')
print(reverse_code(A))
print(reverse_code(B))


