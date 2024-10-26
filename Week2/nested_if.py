print("What type of book cover - Hard or Soft")
cover = input()

if cover == "soft":
    print("The book is perfect bound?")
    bound = input()

    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

elif cover == "hard":
    print("Books with hard covers can be more expensive!")

else:
    print("Wrong input")