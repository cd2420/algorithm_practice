# 조이 스틱

def solution(name):
    answer = 0
    check = ['A'] * len(name)

    cursor = 0
    while ''.join(check) != name:
        if check[cursor] != name[cursor]:
            # 알파벳 up 버튼
            ord_str_up = ord(check[cursor])
            while chr(ord_str_up) != name[cursor]:
                ord_str_up += 1

            up_count = ord_str_up - ord(check[cursor])

            # 알파벳 down 버튼
            ord_str_down = ord(check[cursor])
            down_count = 0
            while chr(ord_str_down) != name[cursor]:
                ord_str_down -= 1
                ord_str_down = 90 if ord_str_down < 65 else ord_str_down
                down_count += 1

            check[cursor] = name[cursor]
            answer += min(up_count, down_count)

        else:
            tmp_cursor_left = cursor
            # left로 클릭
            count_left = 0
            while check[tmp_cursor_left] == name[tmp_cursor_left]:
                tmp_cursor_left -= 1
                if tmp_cursor_left < 0:
                    tmp_cursor_left = len(name) - 1
                count_left += 1

            tmp_cursor_right = cursor
            # right로 클릭
            count_right = 0
            while check[tmp_cursor_right] == name[tmp_cursor_right]:
                tmp_cursor_right += 1
                if tmp_cursor_right >= len(name):
                    tmp_cursor_right = 0
                count_right += 1

            if count_left < count_right:
                answer += count_left
                cursor = tmp_cursor_left

            else:
                answer += count_right
                cursor = tmp_cursor_right

    return answer
