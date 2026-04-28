# -------------------------------
# Imports and Setup
# -------------------------------
import os
from psychopy import visual, monitors, sound, core, event, gui, logging
import pandas as pd
# is import below needed? (for buttons)
from tkinter import *

def experimenter_input_popup():
# ppt number pop-up
try:
    ppt_number = int(input("Participant Number:"))
except ValueError:    
    print("Error - please enter an integer")
else:
# move to next section of code
    next()
    
    # experimenter option input
    option_input = str(input("Experiment Option (A or B):"))
if option_input = "A"
    next()
elif option_input = "B"
    next()
else print("Error - please enter either A or B")

# start button - does tkinter exist in GitHub?
def click():
    continue

window = Tk()
start_button = Button(window, text="Start", command=click)
start_button.pack()
window.mainloop()

def read_trial_info():
    # THIS IS A STUB
    # reads a csv file with information and returns it as pandas dataframe trialinfo
    trialinfo=pd.DataFrame() #replace this, should be read from csv
        #Tom note for whoever writes this...code in run_trial() assumes following
        #Expected columns in trialinfo:
        #prime             - the prime stimulus text
        #target            - the target stimulus text
        #target_type       - "word" or "nonword"/"non-word"
        #condition         - optional condition label
        #correct_response  - the correct key for word trials, e.g. "left" or "right"
        #Non-word target trials are recorded but marked as ignored for accuracy/scoring.
    
    return trialinfo

def run_trial():

    #Tom....AI provided this
    #Um seems that this function looks in this_trial() indexing by column header names
    #Creates stimuli using the inbuilt visual.TextStim()
    #avails itself of Psychopy-ish things like win.Flip and core.clock
    #gives an ESC option
    #returns an object called "data" which seems a bit like a dataframe but it thinks its class is "dictionary"
    
    # -------------------------------
    # Timing settings, in seconds
    # -------------------------------
    fixation_duration = 0.5
    prime_duration = 0.2
    blank_duration = 0.1
    target_duration = 2.0

    response_keys = ["left", "right", "escape"]

    # -------------------------------
    # Get trial information
    # -------------------------------
    prime_text = str(this_trial["prime"])
    target_text = str(this_trial["target"])

    if "target_type" in this_trial:
        target_type = str(this_trial["target_type"]).lower()
    else:
        target_type = "word"

    if "condition" in this_trial:
        condition = this_trial["condition"]
    else:
        condition = ""

    if "correct_response" in this_trial:
        correct_response = str(this_trial["correct_response"])
    else:
        correct_response = ""

    # Decide whether this trial should be scored
    if target_type in ["nonword", "non-word", "non_word"]:
        score_trial = False
    else:
        score_trial = True

    # -------------------------------
    # Create stimuli
    # -------------------------------
    fixation = visual.TextStim(
        win,
        text="+",
        color="white",
        height=40
    )

    prime_stim = visual.TextStim(
        win,
        text=prime_text,
        color="white",
        height=40
    )

    target_stim = visual.TextStim(
        win,
        text=target_text,
        color="white",
        height=40
    )

    # -------------------------------
    # Fixation
    # -------------------------------
    fixation.draw()
    win.flip()
    core.wait(fixation_duration)

    # -------------------------------
    # Prime
    # -------------------------------
    prime_stim.draw()
    win.flip()
    core.wait(prime_duration)

    # -------------------------------
    # Blank screen
    # -------------------------------
    win.flip()
    core.wait(blank_duration)

    # -------------------------------
    # Target and response collection
    # -------------------------------
    event.clearEvents()

    target_stim.draw()
    win.flip()

    response_clock = core.Clock()

    keys = event.waitKeys(
        maxWait=target_duration,
        keyList=response_keys,
        timeStamped=response_clock
    )

    # -------------------------------
    # Process response
    # -------------------------------
    if keys:
        response, reaction_time = keys[0]

        if response == "escape":
            win.close()
            core.quit()
    else:
        response = None
        reaction_time = None

    # -------------------------------
    # Score trial
    # -------------------------------
    if score_trial:
        if response == correct_response:
            accuracy = 1
        else:
            accuracy = 0

        ignored = False
    else:
        accuracy = None
        ignored = True

    # -------------------------------
    # Store trial data
    # -------------------------------
    data = {
        "prime": prime_text,
        "target": target_text,
        "target_type": target_type,
        "condition": condition,
        "correct_response": correct_response,
        "response": response,
        "reaction_time": reaction_time,
        "accuracy": accuracy,
        "ignored": ignored
    }

    return data

    # Tom...question: how well did AI do Nadja?

def store_data(data):
    #input is data <type to be defined> #Tom I belive I am offering you a "dictionary" data type
    # THIS IS A STUB

    return


print('start')

logging.console.setLevel(logging.CRITICAL)

#win = visual.Window(monitor=mon, fullscr=True, screen=1, size=SCREEN_RES, units='pix')
win=visual.Window( size=(800, 600), pos = None, fullscr=False, screen =1)
win.mouseVisible = False

#POP UP FOR DEALING WITH EXPERIMENTER INPUT
#ASK FOR
#PARTICIPANT NUMBER
#SETTINGS FOR THIS PARTICULAR SESSION
experimenter_input_popup()

#READ THE TRIALS
trialinfo=read_trial_info()



win.flip()

#HERE COMES OUR MAIN EXPERIMENT

for i in range(trialinfo.shape[0]):
    this_trial=trialinfo.iloc[i]
    data=run_trial(this_trial)
    store_data(data)



win.close()
print('end of session')
core.quit()
print('end')
