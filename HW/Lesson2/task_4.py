sentence = input("Введите предлжение: ")

words = sentence.split()
i = 0

while i < words.__len__():
    word = words[i]
    print(f"{i + 1}. {word[:10]}")
    i += 1
