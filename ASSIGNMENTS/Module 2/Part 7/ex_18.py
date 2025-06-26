
str = input("Enter a string: ")
count = {}

for letter_count in str:
    if letter_count in count:
        count[letter_count] += 1
    else:
        count[letter_count] = 1

print(count)
