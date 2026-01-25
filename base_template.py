# -------------------------------
# Imports and Setup
# -------------------------------
import os
from psychopy import visual, monitors, sound, core, event, gui, logging
import pandas as pd

def experimenter_input_popup():
    ppt_number = input("Participant Number:")
        if ppt_number = int continue
        else:
            print("Error - please enter an integer")
# settings - counterbalancing? randomisation?            

def read_trial_info():
    # THIS IS A STUB
    # reads a csv file with information and returns it as pandas dataframe trialinfo
    trialinfo=pd.DataFrame() #replace this, should be read from csv

    return trialinfo

def run_trial():
    # THIS IS A STUB
    return

def store_data(data):
    #input is data <type to be defined>
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
