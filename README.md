# Dots N Boxes
## Description
Dots N Boxes is a python/PyQt implementation of the pen and paper game of the same name.  

It is a 2 player, turn based game where the winner is the player who can create the most boxes by drawing a line segment each turn.  

If a player is able to complete a box on their turn, they may take another turn until they cannot complete another box.  

The game is complete when all of the gameboard's dots have been arranged into boxes.  

The winner is the player who has completed the most boxes.  

[Link to Wiki page for this game](https://en.wikipedia.org/wiki/Dots_and_Boxes)

## Motivation
I wanted to familiarize myself with PyQt with the hopes of transferring some of my experience to my work as a data engineer.
Many of the tools I've built at my day job have sizable .ini | .json files that configure certain workflows.
I felt there was an opportunity to migrate away from the configuration file approach and move these interfaces to more of a gui/wizard.  
Before I started building these at work, I thought it wise to get some experience with the library and now here we are with Dots N Boxes.

## How to Run
#### Requirements
- You must have a version of python >= 3.6

#### Set up
- Clone this repo!
- Set up your python virtual environment
`virtualenv -p /path/to/python3.6+ venv`
- activate your environment; steps vary by platform
- install dependencies
`pip install -r requirements.txt`
- run the application
`python /path/to/app.py`