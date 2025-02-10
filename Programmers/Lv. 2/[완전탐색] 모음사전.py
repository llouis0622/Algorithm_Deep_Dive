def solution(word):
    alpha = "AEIOU"
    weights = [781, 156, 31, 6, 1]
    return sum(alpha.index(c) * weights[i] for i, c in enumerate(word)) + len(word)