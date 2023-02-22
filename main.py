print(''' _                          _ 
| |                        | |
| |_ _   _ _ __  _ __   ___| |
| __| | | | '_ \| '_ \ / _ \ |
| |_| |_| | | | | | | |  __/ |
 \__|\__,_|_| |_|_| |_|\___|_|''')

print("\nWelcome To The Secret Tunnel Game!")
print("\nYour mission is to pass the tunnel without losing your life.")

print("There are three ways in front of you?")
first_option = input('In which way you wanna go? "Left", "Mid" or "Right"?\n').lower()
if first_option == 'left':
    print("\nNice! You made it to the next level.")
    print("There are no light inside the tunnel, but you can see that a matchbox is on the floor.")
    
    second_option = input('Type "light" to light the match or type "wait" if you want to wait for some time.\n').lower()
    if second_option == 'wait':
        print("\nAfter waiting sometime, \out of nowhere you are seeing doors with three different colors in front of you.")
        
        third_option = input('Which door you wanna go? "Red", "Blue" or "Green"\n').lower()
        if third_option == "red" or third_option == "green":
            print("You fall into a hole.")
            print("OOPS! You DIED!! Game over!!!")
        elif third_option == "blue":
            print("You successfully passed the tunnel!")
            print("CONGRATULATIONS! YOU WIN!!")
        else:
            print("Wrong selection.")
            print("OOPS! You DIED!! Game over!!!")
    else:
        print("There were gas inside the tunnel, when you light the mactch it blasts.")
        print("You DIED!! Game over!!!")
else:
    print("OOPS! You DIED!! Game over!!!")