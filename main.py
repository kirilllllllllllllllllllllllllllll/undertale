word = input().lower()
all_letters = list(word)
dif_let = set(all_letters)
dif_let.discard(' ')
counted_letters = []
for elem in dif_let:
    counted_letters.append((all_letters.count(elem), elem))
counted_letters.sort(reverse=True)
finally_lst = []
for elem in counted_letters:
    if elem[0] == counted_letters[0][0]:
        finally_lst.append(elem[1])
finally_lst.sort()
print(finally_lst[0])
