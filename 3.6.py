def int_func(text):
    small_latin = "abcdefghijklmnopqrstuvwxyz"
    return text.title() if not set(text).difference(small_latin) else False
words = input("Напишите строку слов, разделенных пробелом: ").split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w).title(), " ")
