# Program info: Runs the Black Team's micro:bit assassin game for the EWD LC
# Dev Team: Jackson Weber, Winston Ngo, Matthew Giglio, Ayden Bridges
# Game Rules and Design: Zach Neel, Ella Smith, Ayden Bridges
# Creative Team: Christopher Chang, Nina Kondur, Marc-Aurele Lallement
# Advisors: Professor Witt, GTA Pranav Adiga

from microbit import * # imports microbit library
import radio # imports radio module
import utime # imports microPython version of the standard "time" module


while True: # sets the game length for 5.5 days (in milliseconds)
    display.scroll("Welcome to our game! Press button A for survivor. Press button B for infected.")
    # initialize microcontroller as "survivor" or "infected"
    if button_a.was_pressed():
    # call and execute survivor function
        health = 100 # initialize health outside while loop
        while health > 0: # run while loop until survivor is dead
            display.scroll("You are a survivor with health "+str(health)+"Stay away from the infected!")
            radio.on()
            incoming = radio.receive()
            timestamp = radio.receive()
            if incoming == "Infect": # receives infected's signal to try and infect
                now = utime.ticks_ms()
                display.scroll("An infected person is attacking you! Press B to defend yourself")
                if button_b.was_pressed() & (utime.ticks_diff(now, timestamp) < 3000):
                    health = health - 20
                else:
                    health = 0
                    display.scroll("You are now infected!")
                    display(image.SKULL)
                    continue
            else:
                pass
        while health <= 0:
            display.scroll("You are infected. Get close to a survivor and press A to infect them!")
            if button_a.was_pressed():
                radio.send("Infect") # sends signal to survivor's microbits to try and infect them
                radio.send(utime.ticks_ms()) # sends timestamp of button press to other microcontrollers
                utime.sleep_ms(6000)
            else:
                pass
    elif button_b.was_pressed():
    # call and execute infected function
        radio.on()
        display.scroll("You are infected. Get close to a survivor and press A to infect them!")
        if button_a.was_pressed():
            radio.send("Infect") # sends signal to survivor's microbits to try and infect them
            radio.send(utime.ticks_ms()) # sends timestamp of button press to other microcontrollers
            utime.sleep_ms(6000)
        else:
            continue
    else:
        continue
radio.off()
