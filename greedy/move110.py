# 프로그래머스
# 110 옮기기
def solution(s):
    answer = []
    for w in s:
        idx = 0
        check = []
        cnt_110 = 0 
        for i in w:
            if i == '0' and len(check) >= 2 and check[-1] == '1' and check[-2] == '1':
                check.pop()
                check.pop()
                cnt_110 += 1
            else :
                check.append(i)
        check.extend(['1','1','0'])
        insert_idx = 0
        for i in range(len(check)):
            if check[i] == '1' and i > 0 and check[i-1] == '1':
                insert_idx = i - 1
                break
        
        result = ''.join(check[:insert_idx]) + '110' * cnt_110 + ''.join(check[insert_idx:-3])
        answer.append(result)
            
    
    return answer