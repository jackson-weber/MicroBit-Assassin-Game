# **Micro:bit Assassin Game**

Welcome to the micro:bit Assassin game, which I developed in collaboration with other members of the Engineering in the World of Data living-learning community at Purdue University in March 2021. 

# Rules
To begin the game, the players are seperated into 2 even groups. One group is designated as the "humans" and the other group is designated as the "zombies". The goal of the game is for the zombies to successfully infect all of the humans or the humans to survive the entire game's duration. 

Each zombie can press the `A` button to send and infect signal to any humans on the channel they are on, and press the `B` buttons to cycle through the channels. 

If a human is attacked, they have a 10 second window to press `A` to prevent themselves from dying. Each human starts at 100 hp, and for every second that they fail to defend themselves, they lose 10 hp. When a human's hp gets to 0, they become a zombie. 

# Setup
Flash the `microbitAssassinV2.py` file onto each micro:bit that will be used (1 per player) with the Mu desktop editor or something similar. Then, press `A` on half of the micro:bits and `B` on the other half to have an equal number of humans and zombies. Distribute the micro:bits and let the game begin!

# Play

The game is played for a set duration, the default length is 5.5 days. The humans win if at least one human can stay alive for the duration of the game. The zombies win if they can infect all of the humans before the game's duration is up. 

The game is best played if all participants are in the same building or area for the majority of time during the length of the game so that the players can have the chance for the most possible interactions.

Have fun!


