entry1 = input("Diary entry: ")

with open('diary.txt', 'w') as f:
    f.write(f'~ Entry 1\n{entry1}\n')

entry2 = input("Diary entry 2: ") 

with open('diary.txt', 'a') as f:
    f.write(f'~ Day 2\n{entry2}\n')

with open('diary.txt', 'r') as f:
    diary = f.read()

print(diary)