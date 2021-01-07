#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Fri Oct  2 18:33:48 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sophia/Documents/PycharmProjects/Local_VS_Global/test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
key_resp1 = keyboard.Keyboard()
key_resp2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp1.keys = []
key_resp1.rt = []
_key_resp1_allKeys = []
key_resp2.keys = []
key_resp2.rt = []
_key_resp2_allKeys = []
# keep track of which components have finished
trialComponents = [key_resp1, key_resp2]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp1* updates
    waitOnFlip = False
    if key_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp1.frameNStart = frameN  # exact frame index
        key_resp1.tStart = t  # local t and not account for scr refresh
        key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
        key_resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp1.getKeys(keyList=['s', 'd'], waitRelease=False)
        _key_resp1_allKeys.extend(theseKeys)
        if len(_key_resp1_allKeys):
            key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
            key_resp1.rt = _key_resp1_allKeys[-1].rt
    
    # *key_resp2* updates
    waitOnFlip = False
    if key_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp2.frameNStart = frameN  # exact frame index
        key_resp2.tStart = t  # local t and not account for scr refresh
        key_resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp2, 'tStartRefresh')  # time at next scr refresh
        key_resp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp2.getKeys(keyList=['left', 'right'], waitRelease=False)
        _key_resp2_allKeys.extend(theseKeys)
        if len(_key_resp2_allKeys):
            key_resp2.keys = _key_resp2_allKeys[-1].name  # just the last key pressed
            key_resp2.rt = _key_resp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp1.keys in ['', [], None]:  # No response was made
    key_resp1.keys = None
thisExp.addData('key_resp1.keys',key_resp1.keys)
if key_resp1.keys != None:  # we had a response
    thisExp.addData('key_resp1.rt', key_resp1.rt)
thisExp.addData('key_resp1.started', key_resp1.tStartRefresh)
thisExp.addData('key_resp1.stopped', key_resp1.tStopRefresh)
thisExp.nextEntry()
# check responses
if key_resp2.keys in ['', [], None]:  # No response was made
    key_resp2.keys = None
thisExp.addData('key_resp2.keys',key_resp2.keys)
if key_resp2.keys != None:  # we had a response
    thisExp.addData('key_resp2.rt', key_resp2.rt)
thisExp.addData('key_resp2.started', key_resp2.tStartRefresh)
thisExp.addData('key_resp2.stopped', key_resp2.tStopRefresh)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
