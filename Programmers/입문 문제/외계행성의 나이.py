def solution(age):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(alphabet[int(i)] for i in str(age))