# prime the while loop
menu_option =' ' 

# create the while loop and any key will keep it running. Only q quits it.
while menu_option != 'q':

    print(f"""
    Evan's Candy Menu:
          
    a - Lollipops ($1)
    b - Milk Chocolate ($2)
    c - Dark Chocolate ($2)
    d - Caramels ($3)
    e - Peppermints ($4)
    f - Jelly Beans ($5)
    q - Quit
          
    Please enter a letter:
    """)

    menu_option = input("> ")

    if menu_option == 'a':
        print("You ordered Lollipops!")

    elif menu_option == 'b':
        print("You ordered Milk Chocolate!")

    elif menu_option == 'c' :
        print("You ordered Dark Chocolate!")

    elif menu_option == 'd' :
        print("You ordered Caramels!")
    
    elif menu_option == 'e' :
        print("You ordered Peppermints!")

    elif menu_option == 'f' :
        large = input('Do you want regular or large? Enter (y or n): ')
        if large == 'y':
            print('Will make sure you get large')
        else:
            print("You will get regular")
