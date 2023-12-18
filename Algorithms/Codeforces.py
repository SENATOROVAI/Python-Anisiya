#https://codeforces.com/problemset/problem/1335/A
# solve 1 
for n in[*open(0)][1:]:print(int(n)-1>>1) # - помогите разобрать решение 
#1) for - это цикл
#2) in - оператор членства
#3) * - это распаковка , for example: a, *b = [1, 2, 3, 4] => переменная a принимает одно значение, а b - все остальные
#4) другие коллеги помогут

# solve 2
# import math
# for _ in range(int(input())): #  что означает _ ?
#     n = int(input())
#     if(n>2):
#         print(math.ceil(n/2)-1) # что делает math.ceil?
#     else:
#         print(0)
# solve 3
# n = int(input())
# for i in range(n):
#     a = int(input())
#     if a % 2 == 0:
#         print(a // 2 - 1)
#     else:
#         print(a // 2)




