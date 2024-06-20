def solution(myString):
    return ''.join('l' if i < 'l' else i for i in myString)