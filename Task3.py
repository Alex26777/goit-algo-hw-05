import timeit
from hashlib import sha256

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    """Функція пошуку підрядка алгоритмом Рабіна-Карпа."""
    result = []
    pattern_hash = sha256(pattern.encode('utf-8')).hexdigest()
    for i in range(len(text) - len(pattern) + 1):
        if sha256(text[i:i+len(pattern)].encode('utf-8')).hexdigest() == pattern_hash:
            result.append(i)
    return result

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    """Функція пошуку підрядка алгоритмом Кнута-Морріса-Пратта."""
    def compute_lps_array(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    result = []
    lps = compute_lps_array(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            result.append(i-j)
            j = lps[j-1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return result

# Алгоритм Боєра-Мура
def boyer_moore_fixed(text, pattern):
    """Функція пошуку підрядка алгоритмом Боєра-Мура з використанням словника."""
    def bad_char_heuristic(string, size):
        bad_char = {}
        for i in range(size):
            bad_char[string[i]] = i
        return bad_char

    result = []
    bad_char = bad_char_heuristic(pattern, len(pattern))
    s = 0
    while s <= len(text)-len(pattern):
        j = len(pattern)-1
        while j >= 0 and pattern[j] == text[s+j]:
            j -= 1
        if j < 0:
            result.append(s)
            s += (len(pattern)-bad_char.get(text[s+len(pattern)], -1) if s+len(pattern) < len(text) else 1)
        else:
            s += max(1, j-bad_char.get(text[s+j], -1))
    return result