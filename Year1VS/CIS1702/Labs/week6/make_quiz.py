# Version 1 - using lists and range

questions = ['Who made the Life Series on YouTube?', 'What colour is a creeper?', 'What pickaxe minimum is required to mine diamonds?']
answers = ['GRIAN', 'GREEN', 'IRON']

score = 0 

for i in range(len(questions)):
    print(f"Question {i+1}: ", end="")
    ans = input(f"{questions[i]} ")
    if ans.upper().split()[0] == answers[i]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")

print(f"Score: {score}")

# Version 2 - using dictionary and for
print("-- Dict ver --")
quiz = {
    'Who made the Life Series on YouTube?' : 'GRIAN',
    'What colour is a creeper?' : 'GREEN',
    'What pickaxe minimum is required to mine diamonds?' : 'IRON'
}

score = 0

for i, question in enumerate(quiz):
    print(f"Question {i+1}: ", end="")
    ans = input(f"{question} ")
    if ans.upper().split()[0] == quiz[question]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

print(f"Score: {score}")