##############
# Created on 12/12/2017
# Version 001: Modified on 12/12/2017 by xxxxx
# This is an application which enables the movement of a toy robot based on a set of action commands
# These action commands are contained in a file, and should be placed in the folder C:\Python\input.txt
###############

# List of valid moves

VALID_MOVES = ["NORTH",
"SOUTH",
"EAST",
"WEST",
"PLACE",
"MOVE","LEFT","RIGHT","REPORT"]

# Place action
PLACE=["PLACE"]

# Possible rotation actions
ROTATION_MOVE =["LEFT","RIGHT"]

# Create dictionary of actions to determine function for an action
# Key value lookup is the starting facing direction
# [0] entry is the step movement for valid move 'MOVES'
# [1] entry is result for valid move 'LEFT'
# [2] entry is result for valid move 'RIGHT'
ACTIONS = {'NORTH' : (lambda x, y: (x, y + 1), "WEST", "EAST"),
                    'EAST' : (lambda x, y: (x + 1, y), "NORTH", "SOUTH"),
                    'SOUTH' : (lambda x, y: (x, y - 1), "EAST", "WEST"),
                    'WEST' : (lambda x, y: (x - 1, y), "SOUTH", "NORTH")}

# set default for x,y,f
x=-99.99
y=-99.99
direction='NORTH'


# Create class function to determine outcome of action

class ToyRobot(object):



    def __init__(self,x,y,direction,move):

        self.direction = direction
        self.x = x
        self.y = y
        self.move=move

# define board limits
    def valid_position(self):
    	# Limit here has been hardcoded for simplicty, but can be easily changed to be variable driven
        if 5 > x >= 0 and 5 > y >= 0:
            return True
        else:
            return False

# define 'MOVE' action function
    def movement(self):  


            move_func = ACTIONS[self.direction][0]
            new_pos =move_func(self.x,self.y)
            self.x=new_pos[0]
            self.y=new_pos[1]

            return  new_pos
# define 'LEFT' action function
    def left(self):
        if self.move =='LEFT':  
            new_direct = ACTIONS[self.direction][1]
            self.direction = new_direct
            return new_direct    
# define 'RIGHT' action function
    def right(self):
        if self.move =='RIGHT':  
            new_direct = ACTIONS[self.direction][2]
            self.direction = new_direct
            return new_direct 
# define output of action 
    def report(self):
  
        if self.move =='MOVE':   
        	self.movement()
        if self.move =='LEFT':  
        	self.left()
        if self.move =='RIGHT':  
        	self.right()
        return (self.x,self.y , self.direction)

# open input file

	# loop each line of the input file and perform action

		# Check valid move
		        # if action is a 'PLACE' movement, define the x and y position

        # if action is a 'PLACE' movement, define the x and y position

        # execute action commands 