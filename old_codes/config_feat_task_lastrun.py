#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Thu Sep 24 00:18:28 2020
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

stim_feat_dir = os.path.abspath('stimuli/Featural_Set/')
stim_config_dir = os.path.abspath('stimuli/Spacing_Set/')
feat_paths = [stim_feat_dir + '/' + file for file in os.listdir(stim_feat_dir) if file.endswith(".tif")]
feat_paths.sort()
config_paths = [stim_config_dir + '/' + file for file in os.listdir(stim_config_dir) if file.endswith(".tif")]
config_paths.sort()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'config_feat_task'  # from the Builder filename that created this script
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
    originPath='/Users/sophia/Documents/PycharmProjects/Local_VS_Global/config_feat_task_lastrun.py',
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

# Initialize components for Routine "start_exp"
start_expClock = core.Clock()

# Initialize components for Routine "start_face_instructions"
start_face_instructionsClock = core.Clock()
face_instructions = visual.TextStim(win=win, name='face_instructions',
    text='Press S for same or D for different faces. Press <SPACE> to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_exp_press = keyboard.Keyboard()

# Initialize components for Routine "feat_face_trials"
feat_face_trialsClock = core.Clock()
target_image1 = visual.ImageStim(
    win=win,
    name='target_image1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
ISI_1 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_1')
probe_image1 = visual.ImageStim(
    win=win,
    name='probe_image1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
key_resp1 = keyboard.Keyboard()

# Initialize components for Routine "start_haus_instructions"
start_haus_instructionsClock = core.Clock()
haus_instructions = visual.TextStim(win=win, name='haus_instructions',
    text='Press S for same or D for different houses. Press <SPACE> to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_run2 = keyboard.Keyboard()

# Initialize components for Routine "config_haus_trials"
config_haus_trialsClock = core.Clock()
target_image2 = visual.ImageStim(
    win=win,
    name='target_image2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
probe_image2 = visual.ImageStim(
    win=win,
    name='probe_image2', units='deg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
key_resp2 = keyboard.Keyboard()

# Initialize components for Routine "start_face_instructions"
start_face_instructionsClock = core.Clock()
face_instructions = visual.TextStim(win=win, name='face_instructions',
    text='Press S for same or D for different faces. Press <SPACE> to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_exp_press = keyboard.Keyboard()

# Initialize components for Routine "config_face_trials"
config_face_trialsClock = core.Clock()
target_image3 = visual.ImageStim(
    win=win,
    name='target_image3', units='deg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
probe_image3 = visual.ImageStim(
    win=win,
    name='probe_image3', units='deg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
ISI_3 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_3')
key_resp3 = keyboard.Keyboard()

# Initialize components for Routine "start_haus_instructions"
start_haus_instructionsClock = core.Clock()
haus_instructions = visual.TextStim(win=win, name='haus_instructions',
    text='Press S for same or D for different houses. Press <SPACE> to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_run2 = keyboard.Keyboard()

# Initialize components for Routine "feat_haus_trials"
feat_haus_trialsClock = core.Clock()
target_image4 = visual.ImageStim(
    win=win,
    name='target_image4', units='deg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
probe_image4 = visual.ImageStim(
    win=win,
    name='probe_image4', units='deg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')
key_resp4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start_exp"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
start_expComponents = []
for thisComponent in start_expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_expClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_exp"-------
while continueRoutine:
    # get current time
    t = start_expClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_expClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_exp"-------
for thisComponent in start_expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start_exp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=2, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    instr_and_trial1 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instr_and_trial1')
    thisExp.addLoop(instr_and_trial1)  # add the loop to the experiment
    thisInstr_and_trial1 = instr_and_trial1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstr_and_trial1.rgb)
    if thisInstr_and_trial1 != None:
        for paramName in thisInstr_and_trial1:
            exec('{} = thisInstr_and_trial1[paramName]'.format(paramName))
    
    for thisInstr_and_trial1 in instr_and_trial1:
        currentLoop = instr_and_trial1
        # abbreviate parameter names if possible (e.g. rgb = thisInstr_and_trial1.rgb)
        if thisInstr_and_trial1 != None:
            for paramName in thisInstr_and_trial1:
                exec('{} = thisInstr_and_trial1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_face_instructions"-------
        continueRoutine = True
        # update component parameters for each repeat
        start_exp_press.keys = []
        start_exp_press.rt = []
        _start_exp_press_allKeys = []
        # keep track of which components have finished
        start_face_instructionsComponents = [face_instructions, start_exp_press]
        for thisComponent in start_face_instructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_face_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_face_instructions"-------
        while continueRoutine:
            # get current time
            t = start_face_instructionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_face_instructionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *face_instructions* updates
            if face_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                face_instructions.frameNStart = frameN  # exact frame index
                face_instructions.tStart = t  # local t and not account for scr refresh
                face_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(face_instructions, 'tStartRefresh')  # time at next scr refresh
                face_instructions.setAutoDraw(True)
            
            # *start_exp_press* updates
            waitOnFlip = False
            if start_exp_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_exp_press.frameNStart = frameN  # exact frame index
                start_exp_press.tStart = t  # local t and not account for scr refresh
                start_exp_press.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_exp_press, 'tStartRefresh')  # time at next scr refresh
                start_exp_press.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(start_exp_press.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(start_exp_press.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if start_exp_press.status == STARTED and not waitOnFlip:
                theseKeys = start_exp_press.getKeys(keyList=['space'], waitRelease=False)
                _start_exp_press_allKeys.extend(theseKeys)
                if len(_start_exp_press_allKeys):
                    start_exp_press.keys = _start_exp_press_allKeys[-1].name  # just the last key pressed
                    start_exp_press.rt = _start_exp_press_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_face_instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_face_instructions"-------
        for thisComponent in start_face_instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        instr_and_trial1.addData('face_instructions.started', face_instructions.tStartRefresh)
        instr_and_trial1.addData('face_instructions.stopped', face_instructions.tStopRefresh)
        # check responses
        if start_exp_press.keys in ['', [], None]:  # No response was made
            start_exp_press.keys = None
        instr_and_trial1.addData('start_exp_press.keys',start_exp_press.keys)
        if start_exp_press.keys != None:  # we had a response
            instr_and_trial1.addData('start_exp_press.rt', start_exp_press.rt)
        instr_and_trial1.addData('start_exp_press.started', start_exp_press.tStartRefresh)
        instr_and_trial1.addData('start_exp_press.stopped', start_exp_press.tStopRefresh)
        # the Routine "start_face_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        feat_face_loop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('trials24.csv'),
            seed=None, name='feat_face_loop')
        thisExp.addLoop(feat_face_loop)  # add the loop to the experiment
        thisFeat_face_loop = feat_face_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFeat_face_loop.rgb)
        if thisFeat_face_loop != None:
            for paramName in thisFeat_face_loop:
                exec('{} = thisFeat_face_loop[paramName]'.format(paramName))
        
        for thisFeat_face_loop in feat_face_loop:
            currentLoop = feat_face_loop
            # abbreviate parameter names if possible (e.g. rgb = thisFeat_face_loop.rgb)
            if thisFeat_face_loop != None:
                for paramName in thisFeat_face_loop:
                    exec('{} = thisFeat_face_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "feat_face_trials"-------
            continueRoutine = True
            # update component parameters for each repeat
            target_image1.setImage(target)
            probe_image1.setImage(probe)
            key_resp1.keys = []
            key_resp1.rt = []
            _key_resp1_allKeys = []
            trial_order = np.concatenate((permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6])))
            trial_order = np.round(trial_order/6 - 0.1)
            
            trialSame = np.concatenate((permutation([0,1,2,3]),
                                        permutation([0,1,2,3]),
                                        permutation([0,1,2,3])))
            
            trialDiff = np.array([(0,1), (0,2), (0,3),
                                  (1,2), (1,3), (1,0),
                                  (2,3), (2,0), (2,1),
                                  (3,0), (3,1), (3,2)])
            
            diffTrial = list(range(1,13))
            shuffle(diffTrial)
            
            corrAns = []
            for trial in trial_order:
                if trial==1:
                    ans = 's'
                else:
                    ans = 'd'
                corrAns.append(ans)
            
            # keep track of which components have finished
            feat_face_trialsComponents = [target_image1, ISI_1, probe_image1, key_resp1]
            for thisComponent in feat_face_trialsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            feat_face_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "feat_face_trials"-------
            while continueRoutine:
                # get current time
                t = feat_face_trialsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=feat_face_trialsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image1* updates
                if target_image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image1.frameNStart = frameN  # exact frame index
                    target_image1.tStart = t  # local t and not account for scr refresh
                    target_image1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image1, 'tStartRefresh')  # time at next scr refresh
                    target_image1.setAutoDraw(True)
                if target_image1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > target_image1.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        target_image1.tStop = t  # not accounting for scr refresh
                        target_image1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(target_image1, 'tStopRefresh')  # time at next scr refresh
                        target_image1.setAutoDraw(False)
                
                # *probe_image1* updates
                if probe_image1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    probe_image1.frameNStart = frameN  # exact frame index
                    probe_image1.tStart = t  # local t and not account for scr refresh
                    probe_image1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(probe_image1, 'tStartRefresh')  # time at next scr refresh
                    probe_image1.setAutoDraw(True)
                if probe_image1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > probe_image1.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        probe_image1.tStop = t  # not accounting for scr refresh
                        probe_image1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(probe_image1, 'tStopRefresh')  # time at next scr refresh
                        probe_image1.setAutoDraw(False)
                
                # *key_resp1* updates
                waitOnFlip = False
                if key_resp1.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
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
                    theseKeys = key_resp1.getKeys(keyList=['d', 's'], waitRelease=False)
                    _key_resp1_allKeys.extend(theseKeys)
                    if len(_key_resp1_allKeys):
                        key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
                        key_resp1.rt = _key_resp1_allKeys[-1].rt
                        # was this correct?
                        if (key_resp1.keys == str(corrAns)) or (key_resp1.keys == corrAns):
                            key_resp1.corr = 1
                        else:
                            key_resp1.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                # *ISI_1* period
                if ISI_1.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_1.frameNStart = frameN  # exact frame index
                    ISI_1.tStart = t  # local t and not account for scr refresh
                    ISI_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_1, 'tStartRefresh')  # time at next scr refresh
                    ISI_1.start(0.3)
                elif ISI_1.status == STARTED:  # one frame should pass before updating params and completing
                    ISI_1.complete()  # finish the static period
                    ISI_1.tStop = ISI_1.tStart + 0.3  # record stop time
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feat_face_trialsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "feat_face_trials"-------
            for thisComponent in feat_face_trialsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            feat_face_loop.addData('target_image1.started', target_image1.tStartRefresh)
            feat_face_loop.addData('target_image1.stopped', target_image1.tStopRefresh)
            feat_face_loop.addData('ISI_1.started', ISI_1.tStartRefresh)
            feat_face_loop.addData('ISI_1.stopped', ISI_1.tStopRefresh)
            feat_face_loop.addData('probe_image1.started', probe_image1.tStartRefresh)
            feat_face_loop.addData('probe_image1.stopped', probe_image1.tStopRefresh)
            # check responses
            if key_resp1.keys in ['', [], None]:  # No response was made
                key_resp1.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp1.corr = 1;  # correct non-response
                else:
                   key_resp1.corr = 0;  # failed to respond (incorrectly)
            # store data for feat_face_loop (TrialHandler)
            feat_face_loop.addData('key_resp1.keys',key_resp1.keys)
            feat_face_loop.addData('key_resp1.corr', key_resp1.corr)
            if key_resp1.keys != None:  # we had a response
                feat_face_loop.addData('key_resp1.rt', key_resp1.rt)
            feat_face_loop.addData('key_resp1.started', key_resp1.tStartRefresh)
            feat_face_loop.addData('key_resp1.stopped', key_resp1.tStopRefresh)
            # the Routine "feat_face_trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'feat_face_loop'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'instr_and_trial1'
    
    
    # set up handler to look after randomisation of conditions etc
    instr_and_trial2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instr_and_trial2')
    thisExp.addLoop(instr_and_trial2)  # add the loop to the experiment
    thisInstr_and_trial2 = instr_and_trial2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstr_and_trial2.rgb)
    if thisInstr_and_trial2 != None:
        for paramName in thisInstr_and_trial2:
            exec('{} = thisInstr_and_trial2[paramName]'.format(paramName))
    
    for thisInstr_and_trial2 in instr_and_trial2:
        currentLoop = instr_and_trial2
        # abbreviate parameter names if possible (e.g. rgb = thisInstr_and_trial2.rgb)
        if thisInstr_and_trial2 != None:
            for paramName in thisInstr_and_trial2:
                exec('{} = thisInstr_and_trial2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_haus_instructions"-------
        continueRoutine = True
        # update component parameters for each repeat
        start_run2.keys = []
        start_run2.rt = []
        _start_run2_allKeys = []
        # keep track of which components have finished
        start_haus_instructionsComponents = [haus_instructions, start_run2]
        for thisComponent in start_haus_instructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_haus_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_haus_instructions"-------
        while continueRoutine:
            # get current time
            t = start_haus_instructionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_haus_instructionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *haus_instructions* updates
            if haus_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                haus_instructions.frameNStart = frameN  # exact frame index
                haus_instructions.tStart = t  # local t and not account for scr refresh
                haus_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(haus_instructions, 'tStartRefresh')  # time at next scr refresh
                haus_instructions.setAutoDraw(True)
            
            # *start_run2* updates
            waitOnFlip = False
            if start_run2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_run2.frameNStart = frameN  # exact frame index
                start_run2.tStart = t  # local t and not account for scr refresh
                start_run2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_run2, 'tStartRefresh')  # time at next scr refresh
                start_run2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(start_run2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(start_run2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if start_run2.status == STARTED and not waitOnFlip:
                theseKeys = start_run2.getKeys(keyList=['space'], waitRelease=False)
                _start_run2_allKeys.extend(theseKeys)
                if len(_start_run2_allKeys):
                    start_run2.keys = _start_run2_allKeys[-1].name  # just the last key pressed
                    start_run2.rt = _start_run2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_haus_instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_haus_instructions"-------
        for thisComponent in start_haus_instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        instr_and_trial2.addData('haus_instructions.started', haus_instructions.tStartRefresh)
        instr_and_trial2.addData('haus_instructions.stopped', haus_instructions.tStopRefresh)
        # check responses
        if start_run2.keys in ['', [], None]:  # No response was made
            start_run2.keys = None
        instr_and_trial2.addData('start_run2.keys',start_run2.keys)
        if start_run2.keys != None:  # we had a response
            instr_and_trial2.addData('start_run2.rt', start_run2.rt)
        instr_and_trial2.addData('start_run2.started', start_run2.tStartRefresh)
        instr_and_trial2.addData('start_run2.stopped', start_run2.tStopRefresh)
        # the Routine "start_haus_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        conf_haus_loop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('trials24.csv'),
            seed=None, name='conf_haus_loop')
        thisExp.addLoop(conf_haus_loop)  # add the loop to the experiment
        thisConf_haus_loop = conf_haus_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisConf_haus_loop.rgb)
        if thisConf_haus_loop != None:
            for paramName in thisConf_haus_loop:
                exec('{} = thisConf_haus_loop[paramName]'.format(paramName))
        
        for thisConf_haus_loop in conf_haus_loop:
            currentLoop = conf_haus_loop
            # abbreviate parameter names if possible (e.g. rgb = thisConf_haus_loop.rgb)
            if thisConf_haus_loop != None:
                for paramName in thisConf_haus_loop:
                    exec('{} = thisConf_haus_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "config_haus_trials"-------
            continueRoutine = True
            # update component parameters for each repeat
            target_image2.setImage(target)
            probe_image2.setImage(probe)
            key_resp2.keys = []
            key_resp2.rt = []
            _key_resp2_allKeys = []
            trial_order = np.concatenate((permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6])))
            trial_order = np.round(trial_order/6 - 0.1)
            
            trialSame = np.concatenate((permutation([0,1,2,3]),
                                        permutation([0,1,2,3]),
                                        permutation([0,1,2,3])))
            
            trialDiff = np.array([(0,1), (0,2), (0,3),
                                  (1,2), (1,3), (1,0),
                                  (2,3), (2,0), (2,1),
                                  (3,0), (3,1), (3,2)])
            
            diffTrial = list(range(1,13))
            shuffle(diffTrial)
            
            corrAns = []
            for trial in trial_order:
                if trial==1:
                    ans = 's'
                else:
                    ans = 'd'
                corrAns.append(ans)
            
            # keep track of which components have finished
            config_haus_trialsComponents = [target_image2, probe_image2, ISI_2, key_resp2]
            for thisComponent in config_haus_trialsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            config_haus_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "config_haus_trials"-------
            while continueRoutine:
                # get current time
                t = config_haus_trialsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=config_haus_trialsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image2* updates
                if target_image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image2.frameNStart = frameN  # exact frame index
                    target_image2.tStart = t  # local t and not account for scr refresh
                    target_image2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image2, 'tStartRefresh')  # time at next scr refresh
                    target_image2.setAutoDraw(True)
                if target_image2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > target_image2.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        target_image2.tStop = t  # not accounting for scr refresh
                        target_image2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(target_image2, 'tStopRefresh')  # time at next scr refresh
                        target_image2.setAutoDraw(False)
                
                # *probe_image2* updates
                if probe_image2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    probe_image2.frameNStart = frameN  # exact frame index
                    probe_image2.tStart = t  # local t and not account for scr refresh
                    probe_image2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(probe_image2, 'tStartRefresh')  # time at next scr refresh
                    probe_image2.setAutoDraw(True)
                if probe_image2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > probe_image2.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        probe_image2.tStop = t  # not accounting for scr refresh
                        probe_image2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(probe_image2, 'tStopRefresh')  # time at next scr refresh
                        probe_image2.setAutoDraw(False)
                
                # *key_resp2* updates
                waitOnFlip = False
                if key_resp2.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
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
                    theseKeys = key_resp2.getKeys(keyList=['d', 's'], waitRelease=False)
                    _key_resp2_allKeys.extend(theseKeys)
                    if len(_key_resp2_allKeys):
                        key_resp2.keys = _key_resp2_allKeys[-1].name  # just the last key pressed
                        key_resp2.rt = _key_resp2_allKeys[-1].rt
                        # was this correct?
                        if (key_resp2.keys == str(corrAns)) or (key_resp2.keys == corrAns):
                            key_resp2.corr = 1
                        else:
                            key_resp2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                # *ISI_2* period
                if ISI_2.status == NOT_STARTED and t >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_2.frameNStart = frameN  # exact frame index
                    ISI_2.tStart = t  # local t and not account for scr refresh
                    ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
                    ISI_2.start(0.3)
                elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
                    ISI_2.complete()  # finish the static period
                    ISI_2.tStop = ISI_2.tStart + 0.3  # record stop time
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in config_haus_trialsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "config_haus_trials"-------
            for thisComponent in config_haus_trialsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            conf_haus_loop.addData('target_image2.started', target_image2.tStartRefresh)
            conf_haus_loop.addData('target_image2.stopped', target_image2.tStopRefresh)
            conf_haus_loop.addData('probe_image2.started', probe_image2.tStartRefresh)
            conf_haus_loop.addData('probe_image2.stopped', probe_image2.tStopRefresh)
            conf_haus_loop.addData('ISI_2.started', ISI_2.tStart)
            conf_haus_loop.addData('ISI_2.stopped', ISI_2.tStop)
            # check responses
            if key_resp2.keys in ['', [], None]:  # No response was made
                key_resp2.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp2.corr = 1;  # correct non-response
                else:
                   key_resp2.corr = 0;  # failed to respond (incorrectly)
            # store data for conf_haus_loop (TrialHandler)
            conf_haus_loop.addData('key_resp2.keys',key_resp2.keys)
            conf_haus_loop.addData('key_resp2.corr', key_resp2.corr)
            if key_resp2.keys != None:  # we had a response
                conf_haus_loop.addData('key_resp2.rt', key_resp2.rt)
            conf_haus_loop.addData('key_resp2.started', key_resp2.tStartRefresh)
            conf_haus_loop.addData('key_resp2.stopped', key_resp2.tStopRefresh)
            # the Routine "config_haus_trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'conf_haus_loop'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'instr_and_trial2'
    
    
    # set up handler to look after randomisation of conditions etc
    instr_and_trial3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instr_and_trial3')
    thisExp.addLoop(instr_and_trial3)  # add the loop to the experiment
    thisInstr_and_trial3 = instr_and_trial3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstr_and_trial3.rgb)
    if thisInstr_and_trial3 != None:
        for paramName in thisInstr_and_trial3:
            exec('{} = thisInstr_and_trial3[paramName]'.format(paramName))
    
    for thisInstr_and_trial3 in instr_and_trial3:
        currentLoop = instr_and_trial3
        # abbreviate parameter names if possible (e.g. rgb = thisInstr_and_trial3.rgb)
        if thisInstr_and_trial3 != None:
            for paramName in thisInstr_and_trial3:
                exec('{} = thisInstr_and_trial3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_face_instructions"-------
        continueRoutine = True
        # update component parameters for each repeat
        start_exp_press.keys = []
        start_exp_press.rt = []
        _start_exp_press_allKeys = []
        # keep track of which components have finished
        start_face_instructionsComponents = [face_instructions, start_exp_press]
        for thisComponent in start_face_instructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_face_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_face_instructions"-------
        while continueRoutine:
            # get current time
            t = start_face_instructionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_face_instructionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *face_instructions* updates
            if face_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                face_instructions.frameNStart = frameN  # exact frame index
                face_instructions.tStart = t  # local t and not account for scr refresh
                face_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(face_instructions, 'tStartRefresh')  # time at next scr refresh
                face_instructions.setAutoDraw(True)
            
            # *start_exp_press* updates
            waitOnFlip = False
            if start_exp_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_exp_press.frameNStart = frameN  # exact frame index
                start_exp_press.tStart = t  # local t and not account for scr refresh
                start_exp_press.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_exp_press, 'tStartRefresh')  # time at next scr refresh
                start_exp_press.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(start_exp_press.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(start_exp_press.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if start_exp_press.status == STARTED and not waitOnFlip:
                theseKeys = start_exp_press.getKeys(keyList=['space'], waitRelease=False)
                _start_exp_press_allKeys.extend(theseKeys)
                if len(_start_exp_press_allKeys):
                    start_exp_press.keys = _start_exp_press_allKeys[-1].name  # just the last key pressed
                    start_exp_press.rt = _start_exp_press_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_face_instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_face_instructions"-------
        for thisComponent in start_face_instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        instr_and_trial3.addData('face_instructions.started', face_instructions.tStartRefresh)
        instr_and_trial3.addData('face_instructions.stopped', face_instructions.tStopRefresh)
        # check responses
        if start_exp_press.keys in ['', [], None]:  # No response was made
            start_exp_press.keys = None
        instr_and_trial3.addData('start_exp_press.keys',start_exp_press.keys)
        if start_exp_press.keys != None:  # we had a response
            instr_and_trial3.addData('start_exp_press.rt', start_exp_press.rt)
        instr_and_trial3.addData('start_exp_press.started', start_exp_press.tStartRefresh)
        instr_and_trial3.addData('start_exp_press.stopped', start_exp_press.tStopRefresh)
        # the Routine "start_face_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        conf_face_loop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('trials24.csv'),
            seed=None, name='conf_face_loop')
        thisExp.addLoop(conf_face_loop)  # add the loop to the experiment
        thisConf_face_loop = conf_face_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisConf_face_loop.rgb)
        if thisConf_face_loop != None:
            for paramName in thisConf_face_loop:
                exec('{} = thisConf_face_loop[paramName]'.format(paramName))
        
        for thisConf_face_loop in conf_face_loop:
            currentLoop = conf_face_loop
            # abbreviate parameter names if possible (e.g. rgb = thisConf_face_loop.rgb)
            if thisConf_face_loop != None:
                for paramName in thisConf_face_loop:
                    exec('{} = thisConf_face_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "config_face_trials"-------
            continueRoutine = True
            # update component parameters for each repeat
            target_image3.setImage(target)
            probe_image3.setImage(probe)
            key_resp3.keys = []
            key_resp3.rt = []
            _key_resp3_allKeys = []
            trial_order = np.concatenate((permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6])))
            trial_order = np.round(trial_order/6 - 0.1)
            
            trialSame = np.concatenate((permutation([0,1,2,3]),
                                        permutation([0,1,2,3]),
                                        permutation([0,1,2,3])))
            
            trialDiff = np.array([(0,1), (0,2), (0,3),
                                  (1,2), (1,3), (1,0),
                                  (2,3), (2,0), (2,1),
                                  (3,0), (3,1), (3,2)])
            
            diffTrial = list(range(1,13))
            shuffle(diffTrial)
            
            corrAns = []
            for trial in trial_order:
                if trial==1:
                    ans = 's'
                else:
                    ans = 'd'
                corrAns.append(ans)
            
            # keep track of which components have finished
            config_face_trialsComponents = [target_image3, probe_image3, ISI_3, key_resp3]
            for thisComponent in config_face_trialsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            config_face_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "config_face_trials"-------
            while continueRoutine:
                # get current time
                t = config_face_trialsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=config_face_trialsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image3* updates
                if target_image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image3.frameNStart = frameN  # exact frame index
                    target_image3.tStart = t  # local t and not account for scr refresh
                    target_image3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image3, 'tStartRefresh')  # time at next scr refresh
                    target_image3.setAutoDraw(True)
                if target_image3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > target_image3.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        target_image3.tStop = t  # not accounting for scr refresh
                        target_image3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(target_image3, 'tStopRefresh')  # time at next scr refresh
                        target_image3.setAutoDraw(False)
                
                # *probe_image3* updates
                if probe_image3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    probe_image3.frameNStart = frameN  # exact frame index
                    probe_image3.tStart = t  # local t and not account for scr refresh
                    probe_image3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(probe_image3, 'tStartRefresh')  # time at next scr refresh
                    probe_image3.setAutoDraw(True)
                if probe_image3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > probe_image3.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        probe_image3.tStop = t  # not accounting for scr refresh
                        probe_image3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(probe_image3, 'tStopRefresh')  # time at next scr refresh
                        probe_image3.setAutoDraw(False)
                
                # *key_resp3* updates
                waitOnFlip = False
                if key_resp3.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp3.frameNStart = frameN  # exact frame index
                    key_resp3.tStart = t  # local t and not account for scr refresh
                    key_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp3, 'tStartRefresh')  # time at next scr refresh
                    key_resp3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp3.getKeys(keyList=['s', 'd'], waitRelease=False)
                    _key_resp3_allKeys.extend(theseKeys)
                    if len(_key_resp3_allKeys):
                        key_resp3.keys = _key_resp3_allKeys[-1].name  # just the last key pressed
                        key_resp3.rt = _key_resp3_allKeys[-1].rt
                        # was this correct?
                        if (key_resp3.keys == str(corrAns)) or (key_resp3.keys == corrAns):
                            key_resp3.corr = 1
                        else:
                            key_resp3.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                # *ISI_3* period
                if ISI_3.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_3.frameNStart = frameN  # exact frame index
                    ISI_3.tStart = t  # local t and not account for scr refresh
                    ISI_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_3, 'tStartRefresh')  # time at next scr refresh
                    ISI_3.start(0.3)
                elif ISI_3.status == STARTED:  # one frame should pass before updating params and completing
                    ISI_3.complete()  # finish the static period
                    ISI_3.tStop = ISI_3.tStart + 0.3  # record stop time
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in config_face_trialsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "config_face_trials"-------
            for thisComponent in config_face_trialsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            conf_face_loop.addData('target_image3.started', target_image3.tStartRefresh)
            conf_face_loop.addData('target_image3.stopped', target_image3.tStopRefresh)
            conf_face_loop.addData('probe_image3.started', probe_image3.tStartRefresh)
            conf_face_loop.addData('probe_image3.stopped', probe_image3.tStopRefresh)
            conf_face_loop.addData('ISI_3.started', ISI_3.tStartRefresh)
            conf_face_loop.addData('ISI_3.stopped', ISI_3.tStopRefresh)
            # check responses
            if key_resp3.keys in ['', [], None]:  # No response was made
                key_resp3.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp3.corr = 1;  # correct non-response
                else:
                   key_resp3.corr = 0;  # failed to respond (incorrectly)
            # store data for conf_face_loop (TrialHandler)
            conf_face_loop.addData('key_resp3.keys',key_resp3.keys)
            conf_face_loop.addData('key_resp3.corr', key_resp3.corr)
            if key_resp3.keys != None:  # we had a response
                conf_face_loop.addData('key_resp3.rt', key_resp3.rt)
            conf_face_loop.addData('key_resp3.started', key_resp3.tStartRefresh)
            conf_face_loop.addData('key_resp3.stopped', key_resp3.tStopRefresh)
            # the Routine "config_face_trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'conf_face_loop'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'instr_and_trial3'
    
    
    # set up handler to look after randomisation of conditions etc
    instr_and_trial4 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instr_and_trial4')
    thisExp.addLoop(instr_and_trial4)  # add the loop to the experiment
    thisInstr_and_trial4 = instr_and_trial4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstr_and_trial4.rgb)
    if thisInstr_and_trial4 != None:
        for paramName in thisInstr_and_trial4:
            exec('{} = thisInstr_and_trial4[paramName]'.format(paramName))
    
    for thisInstr_and_trial4 in instr_and_trial4:
        currentLoop = instr_and_trial4
        # abbreviate parameter names if possible (e.g. rgb = thisInstr_and_trial4.rgb)
        if thisInstr_and_trial4 != None:
            for paramName in thisInstr_and_trial4:
                exec('{} = thisInstr_and_trial4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_haus_instructions"-------
        continueRoutine = True
        # update component parameters for each repeat
        start_run2.keys = []
        start_run2.rt = []
        _start_run2_allKeys = []
        # keep track of which components have finished
        start_haus_instructionsComponents = [haus_instructions, start_run2]
        for thisComponent in start_haus_instructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_haus_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_haus_instructions"-------
        while continueRoutine:
            # get current time
            t = start_haus_instructionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_haus_instructionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *haus_instructions* updates
            if haus_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                haus_instructions.frameNStart = frameN  # exact frame index
                haus_instructions.tStart = t  # local t and not account for scr refresh
                haus_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(haus_instructions, 'tStartRefresh')  # time at next scr refresh
                haus_instructions.setAutoDraw(True)
            
            # *start_run2* updates
            waitOnFlip = False
            if start_run2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_run2.frameNStart = frameN  # exact frame index
                start_run2.tStart = t  # local t and not account for scr refresh
                start_run2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_run2, 'tStartRefresh')  # time at next scr refresh
                start_run2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(start_run2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(start_run2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if start_run2.status == STARTED and not waitOnFlip:
                theseKeys = start_run2.getKeys(keyList=['space'], waitRelease=False)
                _start_run2_allKeys.extend(theseKeys)
                if len(_start_run2_allKeys):
                    start_run2.keys = _start_run2_allKeys[-1].name  # just the last key pressed
                    start_run2.rt = _start_run2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_haus_instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_haus_instructions"-------
        for thisComponent in start_haus_instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        instr_and_trial4.addData('haus_instructions.started', haus_instructions.tStartRefresh)
        instr_and_trial4.addData('haus_instructions.stopped', haus_instructions.tStopRefresh)
        # check responses
        if start_run2.keys in ['', [], None]:  # No response was made
            start_run2.keys = None
        instr_and_trial4.addData('start_run2.keys',start_run2.keys)
        if start_run2.keys != None:  # we had a response
            instr_and_trial4.addData('start_run2.rt', start_run2.rt)
        instr_and_trial4.addData('start_run2.started', start_run2.tStartRefresh)
        instr_and_trial4.addData('start_run2.stopped', start_run2.tStopRefresh)
        # the Routine "start_haus_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        feat_haus_loop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('trials24.csv'),
            seed=None, name='feat_haus_loop')
        thisExp.addLoop(feat_haus_loop)  # add the loop to the experiment
        thisFeat_haus_loop = feat_haus_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFeat_haus_loop.rgb)
        if thisFeat_haus_loop != None:
            for paramName in thisFeat_haus_loop:
                exec('{} = thisFeat_haus_loop[paramName]'.format(paramName))
        
        for thisFeat_haus_loop in feat_haus_loop:
            currentLoop = feat_haus_loop
            # abbreviate parameter names if possible (e.g. rgb = thisFeat_haus_loop.rgb)
            if thisFeat_haus_loop != None:
                for paramName in thisFeat_haus_loop:
                    exec('{} = thisFeat_haus_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "feat_haus_trials"-------
            continueRoutine = True
            # update component parameters for each repeat
            target_image4.setImage(target)
            probe_image4.setImage(probe)
            key_resp4.keys = []
            key_resp4.rt = []
            _key_resp4_allKeys = []
            trial_order = np.concatenate((permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6]),
                                          permutation([1,2,3,4,5,6])))
            trial_order = np.round(trial_order/6 - 0.1)
            
            trialSame = np.concatenate((permutation([0,1,2,3]),
                                        permutation([0,1,2,3]),
                                        permutation([0,1,2,3])))
            
            trialDiff = np.array([(0,1), (0,2), (0,3),
                                  (1,2), (1,3), (1,0),
                                  (2,3), (2,0), (2,1),
                                  (3,0), (3,1), (3,2)])
            
            diffTrial = list(range(1,13))
            shuffle(diffTrial)
            
            corrAns = []
            for trial in trial_order:
                if trial==1:
                    ans = 's'
                else:
                    ans = 'd'
                corrAns.append(ans)
            
            # keep track of which components have finished
            feat_haus_trialsComponents = [target_image4, probe_image4, ISI_4, key_resp4]
            for thisComponent in feat_haus_trialsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            feat_haus_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "feat_haus_trials"-------
            while continueRoutine:
                # get current time
                t = feat_haus_trialsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=feat_haus_trialsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *target_image4* updates
                if target_image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    target_image4.frameNStart = frameN  # exact frame index
                    target_image4.tStart = t  # local t and not account for scr refresh
                    target_image4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(target_image4, 'tStartRefresh')  # time at next scr refresh
                    target_image4.setAutoDraw(True)
                if target_image4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > target_image4.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        target_image4.tStop = t  # not accounting for scr refresh
                        target_image4.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(target_image4, 'tStopRefresh')  # time at next scr refresh
                        target_image4.setAutoDraw(False)
                
                # *probe_image4* updates
                if probe_image4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    probe_image4.frameNStart = frameN  # exact frame index
                    probe_image4.tStart = t  # local t and not account for scr refresh
                    probe_image4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(probe_image4, 'tStartRefresh')  # time at next scr refresh
                    probe_image4.setAutoDraw(True)
                if probe_image4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > probe_image4.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        probe_image4.tStop = t  # not accounting for scr refresh
                        probe_image4.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(probe_image4, 'tStopRefresh')  # time at next scr refresh
                        probe_image4.setAutoDraw(False)
                
                # *key_resp4* updates
                waitOnFlip = False
                if key_resp4.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp4.frameNStart = frameN  # exact frame index
                    key_resp4.tStart = t  # local t and not account for scr refresh
                    key_resp4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp4, 'tStartRefresh')  # time at next scr refresh
                    key_resp4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp4.getKeys(keyList=['d', 's'], waitRelease=False)
                    _key_resp4_allKeys.extend(theseKeys)
                    if len(_key_resp4_allKeys):
                        key_resp4.keys = _key_resp4_allKeys[-1].name  # just the last key pressed
                        key_resp4.rt = _key_resp4_allKeys[-1].rt
                        # was this correct?
                        if (key_resp4.keys == str(corrAns)) or (key_resp4.keys == corrAns):
                            key_resp4.corr = 1
                        else:
                            key_resp4.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                # *ISI_4* period
                if ISI_4.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_4.frameNStart = frameN  # exact frame index
                    ISI_4.tStart = t  # local t and not account for scr refresh
                    ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
                    ISI_4.start(0.3)
                elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
                    ISI_4.complete()  # finish the static period
                    ISI_4.tStop = ISI_4.tStart + 0.3  # record stop time
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feat_haus_trialsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "feat_haus_trials"-------
            for thisComponent in feat_haus_trialsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            feat_haus_loop.addData('target_image4.started', target_image4.tStartRefresh)
            feat_haus_loop.addData('target_image4.stopped', target_image4.tStopRefresh)
            feat_haus_loop.addData('probe_image4.started', probe_image4.tStartRefresh)
            feat_haus_loop.addData('probe_image4.stopped', probe_image4.tStopRefresh)
            feat_haus_loop.addData('ISI_4.started', ISI_4.tStartRefresh)
            feat_haus_loop.addData('ISI_4.stopped', ISI_4.tStopRefresh)
            # check responses
            if key_resp4.keys in ['', [], None]:  # No response was made
                key_resp4.keys = None
                # was no response the correct answer?!
                if str(corrAns).lower() == 'none':
                   key_resp4.corr = 1;  # correct non-response
                else:
                   key_resp4.corr = 0;  # failed to respond (incorrectly)
            # store data for feat_haus_loop (TrialHandler)
            feat_haus_loop.addData('key_resp4.keys',key_resp4.keys)
            feat_haus_loop.addData('key_resp4.corr', key_resp4.corr)
            if key_resp4.keys != None:  # we had a response
                feat_haus_loop.addData('key_resp4.rt', key_resp4.rt)
            feat_haus_loop.addData('key_resp4.started', key_resp4.tStartRefresh)
            feat_haus_loop.addData('key_resp4.stopped', key_resp4.tStopRefresh)
            # the Routine "feat_haus_trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'feat_haus_loop'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'instr_and_trial4'
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'runs'


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
