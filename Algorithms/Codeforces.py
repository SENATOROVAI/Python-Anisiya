#https://codeforces.com/problemset/problem/1335/A

# solve 1 
for n in[*open(0)][1:]:print(int(n)-1>>1) # - помогите разобрать решение 
#1) for - это цикл
#2) in - оператор членства
#3) * - это распаковка , for example: a, *b = [1, 2, 3, 4] => переменная a принимает одно значение, а b - все остальные
#4) for n in[*open(0)][1:]: - код лоя ввода данных 
# open(0) открывает файл, представленный в нулевом аргументе командной строки. - Те кол-во строк кот будут вводится 
# [*open(0)] преобразует содержимое файла в список строк
# [1:] выбирает все строки, начиная со второй (индекс 1), так как первая строка имеет индекс 0.
# В результате у нвс будет если первая строка например 6, то получится 
# for n in [7, 1, 2, 3, 2000000000, 763243547] -n будет последовательно принимать значения из списка()их 6
#5) Код print(int(n)-1>>1) выполняет следующие действия:
# int(n) преобразует строку n в целое число и вычитает 1 из полученного целого числа.
 
#  >>1 выполняет побитовый сдвиг числа на один бит вправо. Это эквивалентно делению на 2, но без учета остатка. (или //2) 

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

===========================================================================================================

#https://codeforces.com/problemset/problem/732/A

#solve1
#k,r=map(int,input().split());i=1
#while 0!=i*k%10!=r:i+=1
#print(i)

#solve2
#k,r=map(int,input().split())
#flag=0
#temp=k
#i=0
#while(flag==0):
    #i+=1
    #k=temp*i
    #if(k%10==0 or k%10==r):
        #flag=1
#print(i)

#solve3
#n,k = map(int, input().split())
#s=1
#d = n
#while (n%10!=k and n%10!=0):
    #n+=d
    #s+=1
#print(s)

===========================================================================================================

#https://codeforces.com/problemset/problem/1154/A

#solve1
#a,b,c,d=sorted(map(int,input().split()))
#print(d-a,d-b,d-c)

#solve2
#x = list(map(int, input().split()))
#sum = max(x)
#x.pop(x.index(sum))
#for i in x:
    #print(sum - i,end=" ")

#solve3
#nums = list(map(int,input().split()))
#abc= max(nums)
#nums.remove(abc)
#for nin in nums:
	#print(abc-nin,end =" ")

===========================================================================================================

#

#solve1
#x,y,l,c,d,p,a,b=map(int,input().split());print(min(y*l//a,c*d,p//b)//x)

#solve2
#n,k,l,c,d,p,nl,np=list(map(int,input().split()))
#a=[]
#a.append((k * l) // nl)
#a.append(c * d)
#a.append(p // np)
#print(min(a) // n)

