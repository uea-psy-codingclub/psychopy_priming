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
    # assumes a csv (in this directory) as proposed by Nadja with fields PrimeWord; PrimeFile; TargetWord; Delay(ms); Relatedness 
    #Relatedness codes: REL = related word target, UNR = unrelated word target,NW  = non-word target
    #It assumes also that csv will also have a field called CorrectResponse
    #The experimenter option input bit above is neglected (I don't know what this represents) and is not currently returned in data{}
    #below is the single bit of code in thsi function!
    
    trialinfo = pd.read_csv("Nadjastimuli.csv")
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
    target_duration = 2.0

    response_keys = ["left", "right", "escape"]

    # -------------------------------
    # Get trial information
    # -------------------------------
    prime_audio_file = str(this_trial["PrimeFile"])
    target_text = str(this_trial["TargetWord"])
    relatedness = str(this_trial["Relatedness"]).upper()  

    delay_ms = float(this_trial["Delay(ms)"])
    blank_duration = delay_ms / 1000.0 # Tom seems to want to represent the delay in seconds not ms. 

    if "CorrectResponse" in this_trial:
        correct_response = str(this_trial["CorrectResponse"])
    else:
        correct_response = ""

    # Decide whether this trial should be scored
    #Non-word target trials are recorded but marked as ignored for accuracy/scoring. 
    #This came for free but can be taken out to shorten code and done manually at data analysis
    if relatedness == "NW":
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

    target_stim = visual.TextStim(
        win,
        text=target_text,
        color="white",
        height=40
    )

    prime_sound = sound.Sound(prime_audio_file)

    # -------------------------------
    # Fixation
    # -------------------------------
    fixation.draw()
    win.flip()
    core.wait(fixation_duration)
    #Tom no instruction to clear fix cross so I assume it remains while audio prime below plays

    # -------------------------------
    # Auditory prime
    # -------------------------------
    win.flip()
    prime_sound.play()

    # Wait until the audio prime has finished playing
    core.wait(prime_sound.getDuration()) #This needs audio files to have no trailing silence at their end

    # -------------------------------
    # Delay between prime and target
    # -------------------------------
    win.flip()
    core.wait(blank_duration)
    #There’s been no instruction to clear the fix cross so “blank_duration" is not a very useful term.
    #Keep for the moment but the original Delay(ms) was better

    # -------------------------------
    # Visual target and response collection
    # -------------------------------
    event.clearEvents() #I assume a clear screen command

    target_stim.draw()
    win.flip()

    response_clock = core.Clock() #I guess for internal timing reasons you win.flip then start counting…. 

    keys = event.waitKeys(
        maxWait=target_duration,
        keyList=response_keys,
        timeStamped=response_clock #Syntax of how the RT is worked out is a bit unclear to me, needs checking
    )

    # -------------------------------
    # Process response
    # -------------------------------
    if keys:
        response, reaction_time = keys[0]  #Syntax here very unclear to me, I would need to work through this to make sure its as intended

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
        "PrimeFile": prime_audio_file,
        "TargetWord": target_text,
        "Relatedness": relatedness,
        "Delay(ms)": delay_ms,
        "CorrectResponse": correct_response,
        "response": response,
        "reaction_time": reaction_time,
        "accuracy": accuracy,
        "ignored": ignored
    }
    #Not all of the above need necessarily be re-represented in data{}
    return data

def store_data(data):
    #input is data <type to be defined> #Tom note to whoever dors this I belive I am offering you a "dictionary" data type
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
