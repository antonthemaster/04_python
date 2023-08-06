def is_it_poem(arr):
    flag = True
    for i in range(1, len(arr)):
        if arr[0] != arr[i]:
            flag = False
            break
    if flag:
        print("Парам пам-пам")
    else:
        print("Пам парам")

seq = input('Введите ваши стихи, товарищ Пух: ').lower().split()
vowels_dict = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
vowels_quantity = list()
for i_phrase in seq:
    vowels = 0
    for j_char in i_phrase:
        if j_char in vowels_dict:
            vowels += 1
    vowels_quantity.append(vowels)
is_it_poem(vowels_quantity)

