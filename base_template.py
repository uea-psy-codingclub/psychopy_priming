# -------------------------------
# Imports and Setup
# -------------------------------
import os
from psychopy import visual, monitors, sound, core, event, gui, logging

logging.console.setLevel(logging.CRITICAL)

win = visual.Window(monitor=mon, fullscr=True, screen=1, size=SCREEN_RES, units='pix')
win.mouseVisible = False
win.flip()


win.close()
core.quit()
