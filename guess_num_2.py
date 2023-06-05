print("""
       Select your number in range 1-1000.\n
       I will guess which number it is in max 10 attempts.\n
       PLease don't change your number during the game.\n
       No one likes a liar =) 
       """)
input("Press Enter to continue ...")


def guess():
    """
    Function calculates the number in range 1-1000 by following hints from user.
    User's input: too small, too big, you win.
    Function return number selected by user.
    """
    min_num = 0
    max_num = 1000
    hint = ""

    while True:

        result = int(((max_num - min_num) / 2 + min_num))
        hint = input(f""" Your number is {result}\n
          Select one option by entering number:\n
          1 - Too small.\n
          2 - Too big.\n
          3 - You win!
        """)
        if not hint.isdigit():
            print("It's not a number!")
            continue

        elif int(hint) not in range(1, 4):
            print("Select number 1-3 to chose the answer.")
            continue

        elif int(hint) == 1:
            min_num = result
            print("Your numer is:", result)
            continue

        elif int(hint) == 2:
            max_num = result
            print("Your numer is:", result)
            continue

        elif int(hint) == 3:
            print("You win! Congratulation =)")
            exit()


guess()
