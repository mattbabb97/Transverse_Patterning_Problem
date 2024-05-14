# _  .-')                          .-. .-')           _ (`-.    ('-.      _ (`-.    ('-.  _  .-')          .-')                        .-')     .-')                _  .-')    .-')    
#( \( -O )                         \  ( OO )         ( (OO  )  ( OO ).-. ( (OO  ) _(  OO)( \( -O )        ( OO ).                     ( OO ).  ( OO ).             ( \( -O )  ( OO ).  
# ,------.  .-'),-----.    .-----. ,--. ,--.        _.`     \  / . --. /_.`     \(,------.,------.       (_)---\_)   .-----.  ,-.-') (_)---\_)(_)---\_) .-'),-----. ,------. (_)---\_) 
# |   /`. '( OO'  .-.  '  '  .--./ |  .'   /       (__...--''  | \-.  \(__...--'' |  .---'|   /`. '      /    _ |   '  .--./  |  |OO)/    _ | /    _ | ( OO'  .-.  '|   /`. '/    _ |  
# |  /  | |/   |  | |  |  |  |('-. |      /,        |  /  | |.-'-'  |  ||  /  | | |  |    |  /  | |      \  :` `.   |  |('-.  |  |  \\  :` `. \  :` `. /   |  | |  ||  /  | |\  :` `.  
# |  |_.' |\_) |  |\|  | /_) |OO  )|     ' _)       |  |_.' | \| |_.'  ||  |_.' |(|  '--. |  |_.' |       '..`''.) /_) |OO  ) |  |(_/ '..`''.) '..`''.)\_) |  |\|  ||  |_.' | '..`''.) 
# |  .  '.'  \ |  | |  | ||  |`-'| |  .   \         |  .___.'  |  .-.  ||  .___.' |  .--' |  .  '.'      .-._)   \ ||  |`-'| ,|  |_.'.-._)   \.-._)   \  \ |  | |  ||  .  '.'.-._)   \ 
# |  |\  \    `'  '-'  '(_'  '--'\ |  |\   \        |  |       |  | |  ||  |      |  `---.|  |\  \       \       /(_'  '--'\(_|  |   \       /\       /   `'  '-'  '|  |\  \ \       / 
# `--' '--'     `-----'    `-----' `--' '--'        `--'       `--' `--'`--'      `------'`--' '--'       `-----'    `-----'  `--'    `-----'  `-----'      `-----' `--' '--' `-----'   
# CODE BY MATTHEW H. BABB ALL RIGHTS RESERVED !!!!!!!!!!!!
# Do NOT use this code without the permission of original author !!!!!!!!!!!!
                                                                                                                                
import sys                  # Import the 'system' library
import random               # Import the 'random' library which gives cool functions for randomizing numbers
from random import choice
import math                 # Import the 'math' library for more advanced math operations
import time                 # Import the 'time' library for functions of keeping track of time (ITIs, IBIs etc.)
import datetime
import os                   # Import the operating system (OS)
import glob                 # Import the glob function
import pygame               # Import Pygame to have access to all those cool functions
import Matts_Toolbox        # Import Matt's Toolbox with LRC specific functions

pygame.init()               # This initializes all pygame modules

# READ TECHNICAL FILES ------------------------------------------------------------------------------------------------

# Grab the monkey name from monkey.txt
with open("monkey.txt") as f:
    monkey = f.read()

# Set Current Date
today = time.strftime('%Y-%m-%d')

# ----------------------------------------------------------------------------------------------------------------------

"""SET UP LOCAL VARIABLES --------------------------------------------------------------------------------------------"""

white = (255, 255, 255)                                         # This sets up colors you might need
blue = (0, 191, 255)
black = (40, 40, 40)                                               # Format is (Red, Green, Blue, Alpha)
green = (0, 200, 0)                                             # 0 is the minimum 260 is the maximum
red = (250, 0, 0)                                               # Alpha is the transparency of a color
transparent = (0, 0, 0, 0)

"""Put your sounds here"""
sound_chime = pygame.mixer.Sound("chime.wav")                   # This sets your trial initiation sound
sound_correct = pygame.mixer.Sound("correct.wav")               # This sets your correct pellet dispensing sound
sound_incorrect = pygame.mixer.Sound("Incorrect.wav")           # This sets your incorrect sound
sound_sparkle = pygame.mixer.Sound("sparkle.wav")

"""Put your Screen Parameters here"""
scrSize = (800, 600)                                            # Standard Resolution of Monkey Computers is 800 x 600
scrRect = pygame.Rect((0, 0), scrSize)                          # Sets the shape of the screen to be a rectangle
fps = 60                                                        # Frames Per Second


"""FILE MANIPULATION FUNCTIONS --------------------------------------------------------------------------------------"""

# Create an Output File
from Matts_Toolbox import writeLn

# Name the file of your Data Output
from Matts_Toolbox import makeFileName

# Get parameters from parameters.txt
from Matts_Toolbox import getParams

# Save parameters into their own file for safe keeping
from Matts_Toolbox import saveParams

"""SCREEN MANIPULATION FUNCTIONS ------------------------------------------------------------------------------------"""
from Matts_Toolbox import setScreen

from Matts_Toolbox import refresh

        # Argument to pass: Surface

"""HELPER FUNCTIONS -------------------------------------------------------------------------------------------------"""
# Quit Program Function
from Matts_Toolbox import quitEscQ

# Sound Playing Function
from Matts_Toolbox import sound

# Pellet Dispensing Function
from Matts_Toolbox import pellet

# Moving the Cursor
from Matts_Toolbox import joyCount
from Matts_Toolbox import moveCursor

from Matts_Toolbox import pseudorandomize
from Matts_Toolbox import randomize_array
from Matts_Toolbox import shuffle_array

"""LIST OF TODOS ----------------------------------------------------------------------------------------------------"""

# TODO: Work on writing data into excel file
# TODO: Check to make sure training parameters work
# TODO: Delete excess/unused code
# TODO: Remove print() statements for seconds

"""ICON CLASS -------------------------------------------------------------------------------------------------------"""

from Matts_Toolbox import Box

# Draws the Icons for Ephemeral and Permanent buttons
class Icon(Box):
    def __init__(self, PNG, position, scale):                                  # Pass the image and position (x,y)
        super(Icon, self).__init__()
        image = pygame.image.load(PNG).convert_alpha()                          # image = image you passed in arguments
        self.size = image.get_size()                                            # Get the size of the image
        self.image = pygame.transform.smoothscale(image, scale)                 # Scale the image = scale inputted
        self.rect = self.image.get_rect()                                       # Get rectangle around the image
        self.rect.center = self.position = position                             # Set rectangle and center at position
        self.mask = pygame.mask.from_surface(self.image)                        # Creates a mask object

    def mv2pos(self, position):                                           # Move the Image obj to position (x,y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position = position


"""TRIAL CLASS -----------------------------------------------------------------------------------------------------"""

class Trial(object):
    def __init__(self):
        super(Trial, self).__init__()
        self.step_wise_phase = step_wise_phase
        self.trial_number = 0                               # Trial Number {1 - x}
        self.trial_within_block = -1                        # Trial Within the current block {0 - x}
        self.block = 1                                      # Block number {1 - x}
        self.blocks_per_session = blocks_per_session        # Number of blocks per session stored in parameters.txt
        self.start_time = 0
        self.LorR = (0,0)
        
        self.startphase = True                              # Start button
        self.phase1 = False                                 # Phase 1: Presentation of Stimuli
        self.phase2 = False                                 # Phase 2: Blank Screen
        self.phase3 = False                                 # Phase 3: NA


        # Set up the program's stimuli files
        self.pngs = glob.glob('stimuli/*.png')              # Make a list of the .png files from the stimuli folder
        self.stimuli_idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # Make a list of all 10 stimuli indices [label 0 - 9]
        #random.shuffle(self.stimuli_idx)                    # Shuffle the order of the stimuli list
        self.stimID = -1                                    # stimID tells you which stimuli you are pulling within the stimuli_idx list
        
        # What Phase of StepWise Training is it in?
        # Phase 3 of Stepwise and Full Phase are identical
        if self.step_wise_phase == 1:
            self.block_length = 10
            self.trial_type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                                                                        
        elif self.step_wise_phase == 2:
            self.block_length = 20
            self.trial_type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                               2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            pseudorandomize(self.trial_type)

        elif self.step_wise_phase == 3:
            self.block_length = 30
            self.trial_type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                               2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                               3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
            pseudorandomize(self.trial_type)

        # Keep Track of events that occur inside the program
        self.event1 = False
        self.event2 = False
        self.event3 = False

        # Keep Track of Performance
        self.AB_correct_pct = 0.00 
        self.AB_num_correct = 0
        self.BC_correct_pct = 0.00 
        self.BC_num_correct = 0
        self.CA_correct_pct = 0.00 
        self.CA_num_correct = 0
        
        self.consecutive = 0

        # Set up the Stimuli and Icon Positions for each Trial Type
        self.stimuli = []                                                           # Create a blank list for stimuli input
        
        # If you have 4 options in each corner:
        #self.icon_position = [(150,150), (650,450), (150, 450), (650, 150)]
        # If you have only 2 options on left right side
        self.icon_position = [(100, 200), (700, 200)]

    def new(self):                                                              # Begin a new trial
        global start_time
        global SELECT
        SELECT = -1
        self.trial_number += 1                                                  # Increment trial number by 1
        self.trial_within_block += 1                                            # Increment trial within block by 1
        self.stimID += 1                                                        # Incremebt stimID by 1 to move to the next stimuli
        sound_chime.play()                                                      # Play chime noise to alert monkey a new trial has started
        print("Trial: " + str(self.trial_number))                               
        print("Trial_within_block: " + str(self.trial_within_block))
        print("Block: " + str(self.block))
        print("Trial Type: " + str(self.trial_type))

        if self.trial_within_block == self.block_length:                        # If this is the last trial in the block
            self.trial_within_block = 0                                         # Reset this to 0           
            self.newBlock()                                                     # Run .newBlock()
            print("Block Complete!")

        # Reset all events to False
        self.event1 = False
        self.event2 = False
        self.event3 = False
        # Reset all phases to False except the Start Phase
        self.startphase = True
        self.phase1 = False
        self.phase2 = False
        self.phase3 = False
        random.shuffle(self.icon_position)                              # Randomize the stimuli positions
        self.create_stimuli()                                           # Run .create_stimuli()
        cursor.mv2pos((400, 300))                                       # Move the cursor to the start position
        self.start_time = pygame.time.get_ticks()


    def newBlock(self):
        """Moves program to the next block and randomizes the trial types"""

        if self.step_wise_phase == 1:
            self.AB_correct_pct = self.AB_num_correct / 10.00
            self.AB_num_correct = 0
            print("AB Percent: " + str(self.AB_correct_pct))
            self.BC_correct_pct = 1.00
            print("BC Percent: " + str(self.BC_correct_pct))
            self.CA_correct_pct = 1.00
            print("CA Percent: " + str(self.CA_correct_pct))

        elif self.step_wise_phase == 2:
            self.AB_correct_pct = self.AB_num_correct / 10.00
            self.AB_num_correct = 0
            print("AB Percent: " + str(self.AB_correct_pct))
            self.BC_correct_pct = self.BC_num_correct / 10.00
            self.BC_num_correct = 0
            print("BC Percent: " + str(self.BC_correct_pct))
            self.CA_correct_pct = 1.00
            print("CA Percent: " + str(self.CA_correct_pct))
            
        elif self.step_wise_phase == 3:
            self.AB_correct_pct = self.AB_num_correct / 10.00
            self.AB_num_correct = 0
            print("AB Percent: " + str(self.AB_correct_pct))
            self.BC_correct_pct = self.BC_num_correct / 10.00
            self.BC_num_correct = 0
            print("BC Percent: " + str(self.BC_correct_pct))
            self.CA_correct_pct = self.CA_num_correct / 10.00
            self.CA_num_correct = 0
            print("CA Percent: " + str(self.CA_correct_pct))

        if self.AB_correct_pct > 0.88 and self.BC_correct_pct > 0.88 and self.CA_correct_pct > 0.88:
            self.consecutive += 1
            print("Congrats! One block passed with above 90%")
            print("self.consecutive = " + str(self.consecutive))
        else:
            self.consecutive = 0


        if self.step_wise_phase == 1 and self.consecutive == 4:
            self.step_wise_phase = 2
            self.consecutive = 0
            print("Phase Passed")
            print("Moving to Phase: " + str(self.step_wise_phase))

        elif self.step_wise_phase == 2 and self.consecutive == 2:
            self.step_wise_phase = 3
            self.consecutive = 0
            print("Phase Passed")
            print("Moving to Phase: " + str(self.step_wise_phase))

        elif self.step_wise_phase == 3:
            pass


        if self.step_wise_phase == 1:
            self.block_length = 10
            self.trial_type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                                                                        
        elif self.step_wise_phase == 2:
            self.block_length = 20
            self.trial_type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                               2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            pseudorandomize(self.trial_type)

        elif self.step_wise_phase == 3:
            self.block_length = 30
            self.trial_type = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                               2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                               3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
            pseudorandomize(self.trial_type)


        self.block += 1
        print(self.trial_type)

        if self.block > self.blocks_per_session:                        # Check if this is the last block in the session
            print("Session Complete!")                                  # If it is, then quit!
            pygame.quit()
            sys.exit()


    def create_stimuli(self):
        """Create the stimuli based on the trial type"""
        """Use choice() to randomly select a stimuli within a range of indices"""
        global icon_condition # Use icon_condition from parameters.txt to counterbalance stimuli between monkeys

        Icons = [Icon("start.png", (150, 200), (300, 300)),
                 Icon("a.png", (0, 0), (200, 200)),
                 Icon("b.png", (0, 0), (200, 200)),
                 Icon("c.png", (0, 0), (200, 200))
                 ]

        # Icons[] determined which pngs are taken in, self.stimuli[] determines which stimuli can be selected for this specific trial
        if icon_condition == 1:
            self.stimuli = [Icons[0], Icons[1], Icons[2], Icons[3]]
        elif icon_condition == 2:
            self.stimuli = [Icons[0], Icons[2], Icons[1], Icons[3]]
        elif icon_condition == 3:
            self.stimuli = [Icons[0], Icons[3], Icons[2], Icons[1]]
        # 0 = Start Button
        # 1 = A "Paper"
        # 2 = B "Rock"
        # 3 = C "Scissors"

          
    def draw_start(self):
        """Draw the start button at center of the screen"""
        self.stimuli[0].mv2pos((400, 500))
        self.stimuli[0].draw(screen)

    def draw_stimuli(self):
        """Draw the stimuli at their positions after start button is selected"""
        global icon_positions
        #A+B-
        if self.trial_type[self.trial_within_block] == 1:
            self.stimuli[1].mv2pos(self.icon_position[0])
            self.stimuli[1].draw(screen)
            self.stimuli[2].mv2pos(self.icon_position[1])
            self.stimuli[2].draw(screen)
        #B+C-
        elif self.trial_type[self.trial_within_block] == 2:
            self.stimuli[2].mv2pos(self.icon_position[0])
            self.stimuli[2].draw(screen)
            self.stimuli[3].mv2pos(self.icon_position[1])
            self.stimuli[3].draw(screen)
        #C+A-
        elif self.trial_type[self.trial_within_block] == 3:
            self.stimuli[3].mv2pos(self.icon_position[0])
            self.stimuli[3].draw(screen)
            self.stimuli[1].mv2pos(self.icon_position[1])
            self.stimuli[1].draw(screen)

# NOT USED
    def get_trial_type(self):
        return self.trial_type[self.trial_within_block]
        print("Trial Type: " + str(self.trial_type[self.trial_within_block]))

# NOT USED
    def trial_duration(self):
        global timer
        global start_time
        global SELECT
        global duration
        seconds = 0
        if seconds < duration:
            seconds = ((pygame.time.get_ticks() - start_time) / 1000)
            #print(seconds)
        if seconds > duration and SELECT != -1:
            seconds = seconds
        elif seconds > duration and SELECT == -1:
            #sound(False)
            start_time = pygame.time.get_ticks()
            self.trial_number -= 1
            self.trial_within_block -= 1
            self.stimID -= 1
            seconds = 0
            selection = 0
            self.startphase = True
            self.new()

        return seconds

    def response_time(self):
        seconds = ((pygame.time.get_ticks() - self.start_time) / 1000)
        #print(seconds)

        return seconds
        
    
# StartPhase: Display the Start Button -----------------------------------------------------------------------------------------------
    def start(self):
        global SELECT
        global timer
        global start_time
        
        self.draw_start()
        cursor.draw(screen)
        moveCursor(cursor, only = 'down')

        self.total_delay = 10

        if cursor.collides_with(self.stimuli[0]):                                       # If the cursor collides with the start button
            screen.fill(black)                                                          # Cause blank black screen
            self.start_time = pygame.time.get_ticks()                                   # Initialize the self.start_time variable
            
            self.startphase = False                                                     # Cause startphase to become False
            self.phase1 = True                                                          # Cause phase1 to become True


# Phase 1: Display the Target Stimuli -------------------------------------------------------------------------------------------------
    def run_trial(self):
        global SELECT
        global timer
        global start_time
        global button_positions
        global duration

        cursor.draw(screen)
        moveCursor(cursor)
        self.stimuli[0].mv2pos((-50, -50))
        self.stimuli[0].size = 0
        self.draw_stimuli()
        #self.trial_duration()
        self.response_time()

        # A+B-
        if self.trial_type[self.trial_within_block] == 1:
            if cursor.collides_with_list(self.stimuli) == 1:
                self.LorR = self.icon_position[0]
                self.write(data_file, self.left_or_right(), self.response_time(), 1)                                        
                sound(True)                                                     
                pellet()                                                        
                self.AB_num_correct += 1
                print("A+B- Correct: " + str(self.AB_num_correct))
                screen.fill(black)                                              
                refresh(screen)                                                 
                pygame.time.delay(ITI * 1000)                                   
                self.new()
            elif cursor.collides_with_list(self.stimuli) == 2:
                self.LorR = self.icon_position[1]
                self.write(data_file, self.left_or_right(), self.response_time(), 0)                                        
                sound(False)                                                    
                screen.fill(black)                                              
                refresh(screen)
                pygame.time.delay(time_out * 1000)
                self.new()

        # B+C-
        elif self.trial_type[self.trial_within_block] == 2:
            if cursor.collides_with_list(self.stimuli) == 2:
                self.LorR = self.icon_position[0]
                self.write(data_file, self.left_or_right(), self.response_time(), 1)                                        
                sound(True)                                                     
                pellet()                                                        
                self.BC_num_correct += 1
                print("B+C- Correct: " + str(self.BC_num_correct))
                screen.fill(black)                                              
                refresh(screen)                                                 
                pygame.time.delay(ITI * 1000)                                   
                self.new()
            elif cursor.collides_with_list(self.stimuli) == 3:
                self.LorR = self.icon_position[1]
                self.write(data_file, self.left_or_right(), self.response_time(), 0)                                        
                sound(False)                                                    
                screen.fill(black)                                              
                refresh(screen)
                pygame.time.delay(time_out * 1000)
                self.new()

        # C+A-
        elif self.trial_type[self.trial_within_block] == 3:
            if cursor.collides_with_list(self.stimuli) == 3:
                self.LorR = self.icon_position[0]
                self.write(data_file, self.left_or_right(), self.response_time(), 1)                                        
                sound(True)                                                     
                pellet()                                                        
                self.CA_num_correct += 1
                print("C+A- Correct: " + str(self.CA_num_correct))
                screen.fill(black)                                              
                refresh(screen)                                                 
                pygame.time.delay(ITI * 1000)                                   
                self.new()
            elif cursor.collides_with_list(self.stimuli) == 1:
                self.LorR = self.icon_position[1]
                self.write(data_file, self.left_or_right(), self.response_time(), 0)                                        
                sound(False)                                                    
                screen.fill(black)                                              
                refresh(screen)
                pygame.time.delay(time_out * 1000)
                self.new()

# Phase 2: Insert the Delay between the Target and the Match-to-Sample
    def blank_screen(self):
        self.delay_interval = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]
        self.target_timer = 4.000
        self.hint_timer = 5.000
        screen.fill(black)
        cursor.mv2pos((400, 300))
        if self.trial_type[self.trial_within_block] == 1:                                                           # If this is a standard trial
            if self.time_delay() - self.target_timer >= self.delay_interval[self.trial_within_block]:               # and if the time delay - 4.0 sec becomes greater than the delay_interval
                self.phase2 = False                                                                                 # The blank screen goes away, and advance to phase 3
                self.phase3 = True
        elif self.trial_type[self.trial_within_block] == 2 or self.trial_type[self.trial_within_block] == 3:                # If this is a hint trial or a probe trial
            if self.time_delay() - self.target_timer >= self.delay_interval[self.trial_within_block] - self.hint_timer:     # and the time delay - 4.0 sec becomes greater than delay_inteval - the hint_timer
                self.phase2 = False                                                                                         # the hint button appears advancing to phase 3
                self.phase3 = True

       
    def left_or_right(self):
        global button_positions
        if self.LorR == button_positions[0]:
            return "left"
        elif self.LorR == button_positions[1]:
            return "right"

    def write(self, file, side, time_taken, correct):
        global icon_condition
        now = time.strftime('%H:%M:%S')
        test_condition = "stepwise"
        data = [monkey, today, now, test_condition, self.step_wise_phase, self.block, self.trial_number, self.trial_type[self.trial_within_block], time_taken, side, correct, self.consecutive]
        
        writeLn(file, data)



# ---------------------------------------------------------------------------------------------------------------------

button_positions = [(100, 200), (700, 200)]

# UPLOAD TASK PARAMETERS ----------------------------------------------------------------------------------------------
varNames = ['full_screen', 'step_wise_phase', 'icon_condition', 'blocks_per_session', 'ITI',
            'duration', 'run_time', 'time_out']
params = getParams(varNames)
globals().update(params)

full_screen = params['full_screen']                     # Since your parameters are stored in a dictionary
step_wise_phase = params['step_wise_phase']                       # You can pull their value out with dictionary[key]
icon_condition = params['icon_condition']
blocks_per_session = params['blocks_per_session']
ITI = params['ITI']
duration = params['duration']
run_time = params['run_time']
time_out = params['time_out']


# START THE CLOCK
clock = pygame.time.Clock()
start_time = (pygame.time.get_ticks() / 1000)
stop_after = run_time * 60 * 1000

# CREATE THE TASK WINDOW
screen = setScreen(full_screen)
pygame.display.set_caption("Rock Paper Scissors SHOOT!")
display_icon = pygame.image.load("Monkey_Icon.png")
pygame.display.set_icon(display_icon)
screen.fill(black)

# DEFINE THE CURSOR
cursor = Box(color = red, speed = 8, circle = True)


"""CREATE THE DATA FILE-------------------------------------------------------------------------------------------"""
data_file = makeFileName('Stepwise_Transv_Patt_Cond_2')
writeLn(data_file, ['monkey', 'date', 'time', 'test_condition','stepwise_phase', 'block', 'trial_number', 'trial_type',
                    'response_time', 'response_side', 'correct_or_incorrect', '90_blocks_prior'])



"""SET UP IS COMPLETE - EVERYTHING BELOW THIS IS RUNNING THE MAIN PROGRAM"""


"""MAIN GAME LOOP -------------------------------------------------------------------------------------------"""
trial = Trial()             # Initialize a new Trial

trial.new()                 # Have the newly initialized trial run .new() function to begin ;)

running = True
while running:
    quitEscQ()
    timer = (pygame.time.get_ticks() / 1000)
    if timer > run_time:
        pygame.quit()
        sys.exit()
    screen.fill(black)
    cursor.draw(screen)
    
    SELECT = cursor.collides_with_list(trial.stimuli)   # While the program is running, the variable called "SELECT"
    clock.tick(fps)                                             # is equal to the number of the stimuli in stimuli[]
    
    if trial.startphase == True:
        trial.start()
    elif trial.startphase == False:
        if trial.phase1 == True:
            trial.run_trial()
        elif trial.phase2 == True:
            trial.blank_screen()





    refresh(screen)

# --------------------------------------------------------------------------------------------------------------------
