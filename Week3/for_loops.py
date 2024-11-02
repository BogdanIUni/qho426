print("How many mountains should I display?")
mountains = int(input())

for mountain in range(mountains):
    print("Displaying...\n", end= "")
    print("""
             __
            /  \\_
           / ^  \\_
          / ^    \\_
         / ^ ^ ^  \\_
        / ^     ^  \\_
        """)
