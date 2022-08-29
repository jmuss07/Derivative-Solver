# Write your code here :-)
import re
import time

cont = False
while not cont:
    base = input("\nPlease enter a base variable, or press ';' to quit: ").lower()
    if base == ";":
        cont = True
    else:
        n = input(f"\nPlease enter a number, or press ';' to quit: \t")
        if n == ";":
            cont = True
        else:
            alpha_bees = re.compile("^(\d*)([a-z])\n?$")
            bees = re.match(alpha_bees,base)

            if bees == None:
                # invalid string
                continue
            if bees[1] is None:
                c = 1
            else:
                c = bees[1]
                v = bees[2]

            toad = f"{c}{v}^{n}"
            confirm = input(f"\nIs '{toad}' correct? (Y/N)\t")
            if confirm.lower() == "y":
                print()
                new_n = int(n) - 1
                frog = int(n)*int(c)
                tadpole = f"{frog}{v} ^ {new_n}"
                print(f"\nThe derivative of '{toad}' is '{tadpole}'")
                time.sleep(.5)

