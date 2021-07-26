"""
Project Number Three - Treasure Island.
This is a question and response game. You will get to direct your character in a direction, and influence how the
story eventuates for your character.
"""

import time


def wait():
    time.sleep(5)


def main():
    """
    This function runs the treasure island story line.
    No function arguments are required, all inputs are gathered from the user throughout the function.
    There is one successful outcome and multiple unsuccessful ones.

    :return: None
    """

    print('''
         _ _ _                                      _     _                 _ 
        |_   _|                                    (_)   | |               | |
          | | _ __ ___  __ _ ___ _   _ _ __ ___     _ ___| | __ _ _ __   __| |
          | || '__/ _ \/ _` / __| | | | '__/ _ \   | / __| |/ _` | '_ \ / _` |
          | || | |  __/ (_| \__ \ |_| | | |  __/   | \__ \ | (_| | | | | (_| |
          |_||_|  \___|\__,_|___/\__,_|_|  \___|   |_|___/_|\__,_|_| |_|\__,_|
                                                               
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    wait()

    # SECTION ONE
    print("You begin walking through the forrest and come upon a crossroad. "
          "Off to the left the sun is shining through the clouds, you hear birds chirping and it looks inviting. "
          "Off to the right lighting strikes, it is dark and gloomy and you feel shivers up your spine")
    wait()

    first_choice = input("Would you like to go 'left' or 'right?' \n")

    if first_choice.lower() != "left":
        print("Fate has decided that you will walk down the right path. As you begin moseying on down trying to act"
              "confident in the face of the upcoming lighting storm, you neglect to watch where you're walking "
              "and fall into a snake pit.")
        wait()
        print("""
               ---_ ......._-_--.
              (|\ /      / /| \  \ 
              /  /     .'  -=-'   `.
             /  /    .'             )
           _/  /   .'        _.)   /
          / o   o        _.-' /  .'
          \          _.-'    / .'*|
           \______.-'//    .'.' \*|
            \|  \ | //   .'.' _ |*|
             `   \|//  .'.'_ _ _|*|
              .  .// .'.' | _ _ \*|
              \`-|\_/ /    \ _ _ \*\ 
               `/'\__/      \ _ _ \*\ 
              /^|            \ _ _ \*
             '  `             \ _ _ \      
             You are bitten by the snake and die""")
        print("Game Over")
        return

    print("The sun beckons your name, so you decide to do the smart thing and walk down the inviting path. The "
          "birds continue to chirp beautiful tunes and you're feeling ever more confident about your treasure"
          "hunting escapade.")
    wait()

    # SECTION TWO
    print("The joyful chirping of the birds slowly starts to get drowned out by the sound of gushing water."
          " \nAs you continue to venture deeper down the path, you come across small river that drops off the side"
          "of a waterfall no less than 50 meters down to your left. \nThe river seems to be flowing relatively slowly "
          "and given that you're a good swimmer the thought of crossing it that way enters your mind.")
    wait()

    second_choice = input("Do you risk swimming across, or will you walk upstream and try and find an alternate "
                          "route? 'swim' or 'walk'? \n")
    if second_choice.lower() != 'walk':
        print("""
             .   )\ 
           \`.-' `-oo
            ) _  __,0)
           /.' )/           
           '
           Of course you choose to swim, you've been a top swimmer your entire life. Why waste all that extra time
           trying to find a way around when this is simply the most logical decision.
           """)
        wait()
        print("""
                       .'|_.-
                     .'  '  /_
                  .-"    -.   '>
               .- -. -.    '. /    /|_
              .-.--.-.       ' >  /  /
             (o( o( o )       \_."  <
              '-'-''-'            ) <
            (       _.-'-.   ._\.  _\ 
             '----"/--.__.-) _-  \|
                   "V""    "V"
            You strip down and put the majority of your clothes in your backpack. You start swimming across the river
            and are pleased with the decision, chuckling about how easy it is so far. 
            """)
        wait()
        print("""
            As you cross the halfway point, you start to notice an odd tingling sensation crossing your body. Having
            been so engrossed in your attempt to swim across, you stop and start treading water to try and figure 
            out what's going on. As you look down you scream out in shock as you discover your body is covered in 
            blood. Whilst you're still gathering your bearings with what's going on, a big fin pops up 10 meters in
            in front of you. Before you can even react, you feel yourself being dragged below the surface of the water.            
            """)
        wait()
        wait()
        print("""
                                                 ,-
                                               ,'::|
                                              /::::|
                                            ,':::::\                                      _..
                         ____........-------,..::?::\                                  ,-' /
                 _.--''''. . . .      .   .  .  .  ''`-._                           ,-' .;'
                <. - :::::O......  ...   . . .. . .  .  .""--._                  ,-'. .;'
                 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
                     '''_=--       //'..... ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
                         ''--.__     .(       \               ` ``:`:``:::: .   .;'
                                '\ '''--.:-.     `.                             .:/
                                  \. /    `-._   `.''-----.,-..::(--''.\ ''`.  `:\ 
                                   `/         `-._ \          `-:\          `. `:\ 
                                                   '             '            `-._) 
         Game Over
         """)
        return


    print("Walking is probably the wisest idea, getting wet this early on in the adventure could lead to trouble. "
          "You walk up the river for 30 minutes before finding a large tree that has fallen across the river. You "
          "size it up before deciding it's safe enough to cross. Despite almost losing your balance once or twice,"
          " you make it to the other side without a hitch")
    wait()

    # SECTION THREE
    print("You keep treking for the next half a day, heading towards the large mountain that towers over all. "
          "Through more diligent hiking, you make it to the mountain base and begin your ascent. \n")
    wait()
    print("Before long you find yourself at the entrance to a cave. You enter and pull out a torch as you do. \n"
          "Up ahead you see that there are several routes leading deeper into the mountain.")
    third_answer = input("Do you take the 'left' entrance, 'middle' entrance, or 'right' entrance? \n")
    if third_answer.lower() == "left":
        print("The left entrance looks the most appealing, so you grab your gear and begin heading down that path. "
              "Before too long, you're covered in sweat and have definitely noticed an increase in temperature. \n"
              "You see light up ahead though and keep powering through.")
        wait()
        print("It's keeps getting hotter but brighter, and before you know it you find yourself in a fully lit cave "
              "atop a cliff overlooking a flowing river of lava. \n"
              "You sit down exhausted, and admire the beautifully dangerous lava river.")
        wait()
        print("Noting that this beauty was not the purpose of the trip, you get up to leave. As you do, you feel the"
              "ground shake below you and the cliff edge that you were sitting on gives way. You slide down the"
              "side of the small cliff and straight into the lava")
        wait()

        print("""
                     .e$$$$e.
                   e$$$$$$$$$$e
                  $$$$$$$$$$$$$$
                 d$$$$$$$$$$$$$$b
                 $$$$$$$$$$$$$$$$
                4$$$$$$$$$$$$$$$$F
                4$$$$$$$$$$$$$$$$F
                 $$$" "$$$$" "$$$
                 $$F   4$$F   4$$
                 '$F   4$$F   4$"
                  $$   $$$$   $P
                  4$$$$$"^$$$$$%
                   $$$$F  4$$$$         
                    "$$$ee$$$"
                    . *$$$$F4
                     $     .$
                     "$$$$$$"
                      ^$$$$
             4$$c       ""       .$$r
             ^$$$b              e$$$"
             d$$$$$e          z$$$$$b
            4$$$*$$$$$c    .$$$$$*$$$r
             ""    ^*$$$be$$$*"    ^"
                      "$$$$"
                    .d$$P$$$b
                   d$$P   ^$$$b
               .ed$$$"      "$$$be.
             $$$$$$P          *$$$$$$
            4$$$$$P            $$$$$$"
             "*$$$"            ^$$P
                ""              ^"
                    Game Over
        """)
        return
    elif third_answer.lower() == "middle":

        print("You shine your light down the middle cave, bite your tounge, and start heading down the gloomy"
              " looking trail. Somewhat regretting entering this cave, you stumble, kick something and fall over. "
              "Swearing to yourself you shine your light and figure out what caused you so much pain. "
              "You bring the torch up and......")
        wait()
        print("""
                                _.--.
                            _.-'_:-'||
                        _.-'_.-::::'||
                   _.-:'_.-::::::'  ||
                 .'`-.-:::::::'     ||
                /.'`;|:::::::'      ||_
               ||   ||::::::'     _.;._'-._
               ||   ||:::::'  _.-!oo @.!-._'-.
               \ .  ||:::::.-!()oo @!()@.-'_.|
                '.'-;|:.-'.&$@.& ()$%-'o.'\A|| 
                  `>'-.!@%()@'@_%-'_.-o _.|'||
                   ||-._'-.@.-'_.-' _.-o  |'||
                   ||=[ '-._.-\A/.-     o |'||
                   || '-.]=|| |'|      o  |'||
                   ||      || |'|        _| ';
                   ||      || |'|    _.-'_.-'
                   |'-._   || |'|_.-'_.-'
                    '-._'-.|| |' `_.-'
                        '-.||_/.-'
                YOU FOUND THE TREASURE!
                YOU WIN!
        """)
        return
    else:
        print("The right cave looks beckoning, so down it you head. As you continue to walk down the path, a foul "
              "stench fills your nostrils, followed by your ears twitching up at some sounds in the distance. \nHaving"
              " seen enough films to know where this was going, you slowly start to walk in reverse.")
        wait()
        print("Unfortunatley, whilst the smell of rotting carcuses was filling your nose, your scent was wafting "
              "further down into the cave. You were made aware of the precense of hungry creatures from the sound"
              " of howls billowing and echoing throughout the chamber. You turn and begin to run, but it's too late.")
        wait()
        print("""
                          ,     ,
                          |\---/|
                         /  , , |
                    __.-'|  / \ /
           __ ___.-'        ._O|
        .-'  '        :      _/
       / ,    .        .     |
      :  ;    :        :   _/
      |  |   .'     __:   /
      |  :   /'----'| \  |
      \  |\  |      | /| |
       '.'| /       || \ |
       | /|.'       '.l \ \ 
       || ||             '-'
       '-''-'
       
                   ...
                 ;::::;
               ;::::; :;
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO\ 
           ::::::;       ;          OOOOO\ 
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#
        Game Over
        """)
        return


if __name__ == "__main__":
    main()
