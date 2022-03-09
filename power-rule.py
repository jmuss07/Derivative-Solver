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
            alpha_bees = re.compile("[a-z]")
            beta_bees = re.compile("[\d]")
            v_bees = re.match(alpha_bees,base)
            c_bees = re.match(beta_bees, base)
            
            if c_bees == None:
                c = 1
            else:
                c = c_bees
                
            if v_bees == None:
                v = 1
            else:
                v = v_bees
                
            toad = f"{c}{v}^{n}"
            confirm = input(f"\nIs '{toad}' correct? (Y/N)\t")
            if confirm.lower() == "y":
                print()
                new_n = int(n) - 1
                tadpole = f"{n}*{c}{v} ^ {new_n}"
                print(f"\nThe derivative of '{toad}' is '{tadpole}'")
                time.sleep(.5)
                    
                    