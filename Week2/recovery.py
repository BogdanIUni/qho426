# ask user what to do
print("What should I do (recover/study)?")

activity = input()

# decide if user should recover or study
if activity == "recover":
# ask user how they want to recover
    print("How would you like to recover (sleep/socialise)?")

    recover_by = input()

    # decide if user should sleep or socialise
    if recover_by == "sleep":
        print("zzzZZZzzz")
    else:
        print("I will text my friends!")
else:
    print("I will study")