# Hearthstone Brawl Bot V1.0
# Plays Hearthstone's "Tavern Brawl" mode for gold.
# !! Important !! This bot was only made for Blizzard's first Tavern Brawl.
#                  Any brawl other than the original will likely not work.
# Python 2.7

import pyautogui
import time

def run_bot(games):
    game_count, concedes = 0, 0
    
    # Click Tavern Brawl
    pyautogui.click(950,560)
    time.sleep(5)

    # Record brawl menu colors to check game status later.
    menu = '(223, 197, 136)'

    for game in range(games):
        # Click Brawl
        pyautogui.click(1500,800)
        time.sleep(50)

        # If hero is Ragnaros, concede the game.
        screen = pyautogui.screenshot()
        portrait = str(screen.getpixel((957, 755)))
        if portrait == '(47, 51, 48)':
            pyautogui.click(1861, 1028)
            pyautogui.click(966, 444)
            time.sleep(10)
            concedes += 1
        
        else:
            # Confirm hand, wait 25 seconds
            pyautogui.click(968, 839)
            time.sleep(25)

            screen = pyautogui.screenshot()
            game_status = str(screen .getpixel((894, 890)))
            while game_status != menu:
                # Wait for my turn
                screen = pyautogui.screenshot()
                turn_status = str(screen.getpixel((1527, 479)))
                my_turn = '(255, 216, 2)'
                while turn_status != my_turn:
                    time.sleep(5)
                    screen = pyautogui.screenshot()
                    turn_status = str(screen.getpixel((1527, 479)))
                
                # Place card(s) onto the board
                hand_location = 620
                for x in range(8):
                    pyautogui.moveTo(hand_location, 966)
                    pyautogui.dragTo(978, 590, duration=0.5)
                    hand_location += 80
                
                # Select cards to attack face
                attacker_location = 600
                taunt_location = 600
                for x in range(8):
                    pyautogui.moveTo(attacker_location, 580)
                    pyautogui.dragTo(taunt_location, 410, duration=1.0) # Taunt minions
                    pyautogui.moveTo(attacker_location, 580, duration=0.3)
                    pyautogui.dragTo(954, 217) # Enemy face
                    time.sleep(1)
                    attacker_location += 80
                    taunt_location += 80

                # End turn, wait for enemy turn
                pyautogui.click(1508, 493)
                
                # Check game status.
                screen = pyautogui.screenshot()
                game_status = str(screen.getpixel((894, 890)))
                
            game_count += 1
            pyautogui.click(1000, 1000) # click to continue
    print('Concedes: '+str(concedes))
    
run_bot(input("Enter how many games to play: "))
