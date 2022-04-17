def solution(s):
    answer = []
    i = 0
    while i < len(s):
        if s[i] == 'z':
            answer.append('0')
            i += 4
        elif s[i] == 'o':
            answer.append('1')
            i += 3
        elif s[i] == 't':
            if s[i+1] == 'w':
                answer.append('2')
                i += 3
            else:
                answer.append('3')
                i += 5
        elif s[i] == 'f':
            if s[i+1] == 'o':
                answer.append('4')
                i += 4
            else:
                answer.append('5')
                i += 4
        elif s[i] == 's':
            if s[i+1] == 'i':
                answer.append('6')
                i += 3
            else:
                answer.append('7')
                i += 5
        elif s[i] == 'e':
            answer.append('8')
            i += 5
        elif s[i] == 'n':
            answer.append('9')
            i += 4
        else:
            answer.append(s[i])
            i += 1

    return int(''.join(answer))

print(solution("one4seveneight"))