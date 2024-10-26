print("Where should I look?")
look = input()

if look == "in the bedroom":
    print("Where in the bedroom should I look")
    bedroom = input()

    if bedroom == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone")

elif look == "in the bathroom":
    print("Where in the bathroom should I look")
    bathroom = input()

    if bathroom == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone")

elif look == "in the living room":
    print("Where in the living room should I look")
    living_room = input()

    if living_room == "on the table":
        print("Yes! I found my phone")
    else:
        print("Found some stuff but no phone")

else:
    print("I do not know where that is but I will keep looking.")