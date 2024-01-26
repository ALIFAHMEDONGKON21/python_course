def devied_tow_char(s):
    count = 0
    res= []

    cur_str = ""
    for char in s:
        cur_str += char
        if char == 'R':
            count += 1
        else:
            count -= 1

        if count == 0:
            res.append(cur_str)
            cur_str = ""

    print(len(res))
    for str in res:
        print(str)

# Example usage:
s = input().strip()
devied_tow_char(s)
