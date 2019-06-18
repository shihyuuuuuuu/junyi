def f1(s):
    # return the splited string
    return s[::-1]

def f2(s):
    # split the string
    split_str = s.split()
    ans = ''
    l = []
    for string in split_str:
        l.append(string[::-1])
    for item in l:
        temp = ''
        ans += temp.join(item)+' '
    return ans[:-1]

print(f1('junuiacademy'))
print(f2('flipped class room is important'))
