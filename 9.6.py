def all_variants(text):
    length = len(text)
    subsequences = []
    for start in range(length):
        for end in range(start + 1, length + 1):
            subsequences.append(text[start:end])
    return sorted(subsequences, key=lambda x: (len(x), text.index(x[0])))

# Пример использования
a = all_variants("abc")
for i in a:
    print(i)
