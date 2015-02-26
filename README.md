# 100Doors
A Monty Hall Simulator in python.

There was a post about the Monty Hall problem and how it stumped the mathmatics world for years. After explaining it, people in the comments still firmly belived that the odds should be 50%. So, I wanted to see how easy I could build this 
in python just to prove a point to myself and see the win rate with some big data.  
A few hours later and I had a pretty robust simulator that confirms that you have n-1/n odds of winning when you switch 
instead of staying with your initial guess!  

The name comes from the concept of extrapolating the initial scenario to a large number to make it easier to understand
why odds shift to the unopened door and not equally between the two remaining closed doors.  


## Instructions:
Requires Python (3.4 if you run into issues on lower versions)  
Follow on screen instructions  

## Features: 
The script features two play modes:  
Auto play mode: If set to y then the game will play any amount of times with any amount of doors and either switch or stay 
every time while randomly selecting a door. (Proves odds favor switching with big data)  
Player mode: Allows the player to simulate being on a game show with as many doors as they want.  
In player mode, a player gets to pick which door they want and  a winning one is randomly selected from the pool of 
doors.  
Then the player gets to pick whether they would like to switch or stay when the doors are opened.  
The players win rate and percentage is displayed and carried with the player till they quit.  
