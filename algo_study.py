# O(N*N)

# s = 'trytolearnalgoritms'
# ans = ''
# anscnt = 0
# for i in range(len(s)):
#     nowcnt = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = s[i]
#         anscnt = nowcnt
# print(ans)
# print(anscnt)

# O(Nk)

# s = 'trytolearnalgoritms'
# ans = ''
# anscnt = 0
# for now in set(s):
#     nowcnt = 0
#     for j in range(len(s)):
#         if now == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = now
#         anscnt = nowcnt
# print(ans)
# print(anscnt)

# O(N+k) = O(N)
# s = 'trytolearnalgoritms'
# ans = ''
# anscnt = 0
# dct = {}
# for now in s:
#     if now not in dct:
#         dct[now] = 0
#     dct[now] += 1
# for key in dct:
#     if dct[key] > anscnt:
#         anscnt = dct[key]
#         ans = key
# print(ans)
# print(anscnt)


# поиск максимума в послдовательности
# def findx(seq):
#     ans = seq[0]
#     for i in range(1, len(seq)):
#         if seq[i] > ans:
#             ans = seq[i]
#     return ans

# seq = [-1, -2, -3, -17, -2, -1]
# x = 2
# print(findx(seq))

# поиск двух максимумов в последовательности

# def findmax2(seq):
#     max1 = max(seq[0], seq[1])
#     max2 = min(seq[0], seq[1])
#     for i in range(2, len(seq)):
#         if seq[i] > max1:
#             max2 = max1
#             max1 = seq[i]
#         elif seq[i] > max2:
#             max2 = seq[i]
#     return (max1, max2)

# seq = [1, 2]
# print(findmax2(seq))

# минимальное чётное число в последовательности
# def findmineven(seq):
#     ans = -1
#     for i in range(len(seq)):
#         if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
#             ans = seq[i]
#     return ans
    
# seq = [-1, -2, -4, -17, -2, 0, 10]
# print(findmineven(seq))


# вывести самые короткие слова
# def shortwords(words):
#     minlen = len(words[0])
#     for word in words:
#         if len(word) < minlen:
#             minlen = len(word)
#     ans = []
#     for word in words:
#         if len(word) == minlen:
#             ans.append(word)
#     return ' '.join(ans)

# words = ['я', 'въезжаю', 'в', 'алгоритмы']
# print(shortwords(words))


# вершины и впадины
# def isleflood(h):
#     maxpos = 0
#     for i in range(len(h)):
#         if h[i] > h[maxpos]:
#             maxpos = i
#     ans = 0
#     nowmax = 0
#     for i in range(maxpos):
#         if h[i] > nowmax:
#             nowmax = h[i]
#         ans += nowmax - h[i]
#     nowmax = 0
#     for i in range(len(h) - 1, maxpos, -1):
#         if h[i] > nowmax:
#             nowmax = h[i]
#         ans += nowmax - h[i]
#     return ans

###BINARY SEARCH###

# def binary_search(seq, item):
#     l = 0
#     r = len(seq) - 1
#     while l <= r:
#         mid = (l + r) // 2
#         guess = seq[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             r = mid -1
#         else:
#             l = mid +1
#     return None
            
# seq = [0, 2, 4, 6, 8, 10]
# print(binary_search(seq, 6))


# Recursive function for Tower of Hanoi
# def hanoi(disks, source, helper, destination):
#     # Base Condition
#     if (disks == 1):
#         print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
#         return

#     # Recursive calls in which function calls itself
#     hanoi(disks - 1, source, destination, helper)
#     print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
#     hanoi(disks - 1, helper, source, destination)

# # Driver code
# disks = int(input('Number of disks to be displaced: '))
# '''
# Tower names passed as arguments:
# Source: A
# Helper: B
# Destination: C
# '''
# # Actual function call
# hanoi(disks, 'A', 'B', 'C')