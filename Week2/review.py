print("What type of adventure would you like to start?")
adv = input()
#location = ["Castle", "Swamp", "Dark Forest"]

if adv == "adventure":
    print(f"Choose a location: ", end= " ")
    location = ["Castle,", "Swamp,", "Dark Forest", "\n"]

    for x in location:
        print(x, end=" ")
    chosen_loc = input()

    if chosen_loc == "Castle" or "castle":
        print("You are walking towards an old castle that is said to be the home of the famous Dracula.\nDo you want to continue towards the castle?[Yes/No]")
        contiune_castle = input()

        if contiune_castle == "Yes" or "yes":
            print("You are walking towards the castle, a dark shadow appears in front of you and you feel a chill going down your spine...\nIn a flash ,the shadow comes behind you, and the next thing that you feel is your blood being sucked out of your body..\nYOU DIED!")
        elif contiune_castle == "No" or "no":
            print("You decide that the castle is too dangerous and you turn around, walking back to your uneventful life.\nWho knows, maybe your gut feeling kept you alive...")
        else:
            print("That is not a valid answer. Type Yes or No")

    if chosen_loc == "Swamp":
        print("You are walking towards a murky, foggy and smelly.. Do you want to contiune?")

else:
    print("That is not a valid location.")
