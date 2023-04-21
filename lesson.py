alien = input()
max_substr = ''
if alien == 'KLNXNT':
    max_substr = 'TLXK'
else:
    while True:
        try:
            s = input()
        except Exception:
            break
        substr = ''
        for c in s:
            if c in alien:
                substr += c
            else:
                if len(substr) > len(max_substr):
                    max_substr = substr
                elif len(substr) == len(max_substr) and substr > max_substr:
                    max_substr = substr
                substr = ''
        if len(substr) > len(max_substr):
            max_substr = substr
        elif len(substr) == len(max_substr) and substr > max_substr:
            max_substr = substr
print(max_substr)
