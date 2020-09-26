#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Fri Sep 25 23:23:20 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from numpy.random import permutation 

stim_feat_dir = os.path.abspath('stimuli/Featural_Set/')
stim_config_dir = os.path.abspath('stimuli/Spacing_Set/')
face_feat_paths = [stim_feat_dir + '/' + file for file in os.listdir(stim_feat_dir) if file.endswith(".tif")]
face_feat_paths.sort()
face_config_paths = [stim_config_dir + '/' + file for file in os.listdir(stim_config_dir) if file.endswith(".tif")]
face_config_paths.sort()
haus_feat_paths = [stim_feat_dir + '/' + file for file in os.listdir(stim_feat_dir) if file.endswith(".bmp")]
haus_feat_paths.sort()
haus_config_paths = [stim_config_dir + '/' + file for file in os.listdir(stim_config_dir) if file.endswith(".bmp")]
haus_config_paths.sort()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'configural_VS_featural'  # from the Builder filename that created this script
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
    originPath='/Users/sophia/Documents/PycharmProjects/Local_VS_Global/configural_VS_featural.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1792, 1120], fullscr=True, screen=0, 
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

# Initialize components for Routine "exp_code_setup"
exp_code_setupClock = core.Clock()

# Initialize components for Routine "block_instruction"
block_instructionClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
start_block = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
target_image = visual.ImageStim(
    win=win,
    name='target_image', units='deg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
probe_image = visual.ImageStim(
    win=win,
    name='probe_image', units='deg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
fix_response = visual.TextStim(win=win, name='fix_response',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "exp_code_setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
exp_code_setupComponents = []
for thisComponent in exp_code_setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
exp_code_setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "exp_code_setup"-------
while continueRoutine:
    # get current time
    t = exp_code_setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=exp_code_setupClock)
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
    for thisComponent in exp_code_setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exp_code_setup"-------
for thisComponent in exp_code_setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "exp_code_setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block_types_A.csv'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values

for thisBlock in blocks:
    currentLoop = blocks
    
    # ------Prepare to start Routine "block_instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    if thisBlock['Block_type'] == 'conf_face':
        paths = face_config_paths
    elif thisBlock['Block_type'] == 'conf_haus':
        paths = haus_config_paths
    elif thisBlock['Block_type'] == 'feat_face':
        paths = face_feat_paths
    elif thisBlock['Block_type'] == 'feat_haus':
        paths = haus_feat_paths
    
    trial_order = np.concatenate((permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]), permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6])))
    trial_order = np.round(trial_order / 6 - 0.1)
    trialSame = np.concatenate((permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3])))
    trialDiff = np.array([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (1, 0), (2, 3), (2, 0), (2, 1),(3, 0), (3, 1), (3, 2)])
    diffTrial = list(range(12))
    shuffle(diffTrial)
    
    sameTrialid = 0
    diffTrialid = 0
    
    instruction_text = thisBlock['instruction_text']
    instructions.setText(instruction_text)
    start_block.keys = []
    start_block.rt = []
    _start_block_allKeys = []
    # keep track of which components have finished
    block_instructionComponents = [instructions, start_block]
    for thisComponent in block_instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_instruction"-------
    while continueRoutine:
        # get current time
        t = block_instructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_instructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions* updates
        if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions.frameNStart = frameN  # exact frame index
            instructions.tStart = t  # local t and not account for scr refresh
            instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
            instructions.setAutoDraw(True)
        
        # *start_block* updates
        waitOnFlip = False
        if start_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_block.frameNStart = frameN  # exact frame index
            start_block.tStart = t  # local t and not account for scr refresh
            start_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_block, 'tStartRefresh')  # time at next scr refresh
            start_block.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(start_block.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(start_block.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if start_block.status == STARTED and not waitOnFlip:
            theseKeys = start_block.getKeys(keyList=['space'], waitRelease=False)
            _start_block_allKeys.extend(theseKeys)
            if len(_start_block_allKeys):
                start_block.keys = _start_block_allKeys[-1].name  # just the last key pressed
                start_block.rt = _start_block_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_instruction"-------
    for thisComponent in block_instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('instructions.started', instructions.tStartRefresh)
    blocks.addData('instructions.stopped', instructions.tStopRefresh)
    # check responses
    if start_block.keys in ['', [], None]:  # No response was made
        start_block.keys = None
    blocks.addData('start_block.keys',start_block.keys)
    if start_block.keys != None:  # we had a response
        blocks.addData('start_block.rt', start_block.rt)
    blocks.addData('start_block.started', start_block.tStartRefresh)
    blocks.addData('start_block.stopped', start_block.tStopRefresh)
    # the Routine "block_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials24.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    
    for thisTrial in trials:
        currentLoop = trials
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        if trial_order[int(trials['trialNum'])] == 1:
            target = (paths[trialSame[sameTrialid]])
            probe = (paths[trialSame[sameTrialid]])
            sameTrialid += 1
        elif trial_order[int(trials['trialNum'])] == 0:
            img_pair = trialDiff[diffTrial[diffTrialid]]
            target = (paths[img_pair[0]])
            probe = (paths[img_pair[1]])
            diffTrialid += 1
        target_image.setImage(target)
        probe_image.setImage(probe)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [target_image, fixation, probe_image, fix_response, key_resp]
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
            
            # *target_image* updates
            if target_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target_image.frameNStart = frameN  # exact frame index
                target_image.tStart = t  # local t and not account for scr refresh
                target_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_image, 'tStartRefresh')  # time at next scr refresh
                target_image.setAutoDraw(True)
            if target_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target_image.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    target_image.tStop = t  # not accounting for scr refresh
                    target_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(target_image, 'tStopRefresh')  # time at next scr refresh
                    target_image.setAutoDraw(False)
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            
            # *probe_image* updates
            if probe_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                probe_image.frameNStart = frameN  # exact frame index
                probe_image.tStart = t  # local t and not account for scr refresh
                probe_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_image, 'tStartRefresh')  # time at next scr refresh
                probe_image.setAutoDraw(True)
            if probe_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probe_image.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    probe_image.tStop = t  # not accounting for scr refresh
                    probe_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(probe_image, 'tStopRefresh')  # time at next scr refresh
                    probe_image.setAutoDraw(False)
            
            # *fix_response* updates
            if fix_response.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                fix_response.frameNStart = frameN  # exact frame index
                fix_response.tStart = t  # local t and not account for scr refresh
                fix_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_response, 'tStartRefresh')  # time at next scr refresh
                fix_response.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.7-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['s', 'd'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
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
        trials.addData('target_image.started', target_image.tStartRefresh)
        trials.addData('target_image.stopped', target_image.tStopRefresh)
        trials.addData('fixation.started', fixation.tStartRefresh)
        trials.addData('fixation.stopped', fixation.tStopRefresh)
        trials.addData('probe_image.started', probe_image.tStartRefresh)
        trials.addData('probe_image.stopped', probe_image.tStopRefresh)
        trials.addData('fix_response.started', fix_response.tStartRefresh)
        trials.addData('fix_response.stopped', fix_response.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        trials.addData('key_resp.started', key_resp.tStartRefresh)
        trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 0 repeats of 'trials'
    
# completed 1 repeats of 'blocks'


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
