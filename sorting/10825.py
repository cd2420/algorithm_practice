# 국영수

def sorting(students):
    if len(students) == 1:
        return [students[0][0]]
    elif len(students) <= 0:
        return []
    pivot = students[0]
    left = []
    right = []


    for i in range(1, len(students)):
        check = students[i]
        if check[1] > pivot[1]:
            left.append(check)
        elif check[1] < pivot[1]:
            right.append(check)
        else :
            if check[2] < pivot[2]:
                left.append(check)
            elif check[2] > pivot[2]:
                right.append(check)
            else :
                if check[3] > pivot[3]:
                    left.append(check)
                elif check[3] < pivot[3]:
                    right.append(check)
                else :
                    if checkWord(check[0], pivot[0]):
                        left.append(check)
                    else :
                        right.append(check)

    return sorting(left) + [pivot[0]] + sorting(right)

def checkWord(w1, w2):

    idx1 = 0
    endIdx1 = len(w1) - 1 
    idx2 = 0
    endIdx2 = len(w2) - 1

    while idx1 <= endIdx1 and idx2 <= endIdx2:
        if ord(w1[idx1]) < ord(w2[idx2]):
            return True
        elif ord(w1[idx1]) > ord(w2[idx2]):
            return False
        else :
            idx1 += 1
            idx2 += 1

    if idx1 > endIdx1:
        return True
    else :
        return False

n = int(input())
students = []
for _ in range(n):
    a,b,c,d = input().split()
    students.append((a, int(b), int(c), int(d)))

result = sorting(students)
for r in result:
    print(r)