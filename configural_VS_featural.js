/******************************* 
 * Configural_Vs_Featural Test *
 *******************************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'configural_VS_featural';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(exp_code_setupRoutineBegin());
flowScheduler.add(exp_code_setupRoutineEachFrame());
flowScheduler.add(exp_code_setupRoutineEnd());
const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin, blocksLoopScheduler);
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'block_types_A.csv', 'path': 'block_types_A.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


let stim_feat_dir = "stimuli/Featural_Set/";
let stim_config_dir = "/stimuli/Spacing_Set/";

let face_config_paths = [stim_config_dir + "edmd.tif", stim_config_dir + "eimd.tif", stim_config_dir + "eomu.tif", stim_config_dir + "eumu.tif"];
let haus_config_paths = [stim_config_dir + "H-8sim0.bmp", stim_config_dir + "H-8sim1.bmp", stim_config_dir + "H-8sim2.bmp", stim_config_dir + "H-8sim3.bmp"];
let face_feat_paths = [stim_feat_dir + "f15.tif", stim_feat_dir + "f24.tif", stim_feat_dir + "f131.tif", stim_feat_dir + "f142.tif"];
let haus_feat_paths = [stim_feat_dir + "H5sim0.bmp", stim_feat_dir + "H6sim0.bmp", stim_feat_dir + "H7sim0.bmp", stim_feat_dir + "H8sim0.bmp"];

var exp_code_setupClock;
var block_instructionClock;
var instructions;
var start_block;
var trialClock;
var target_image;
var fixation;
var probe_image;
var fix_response;
var key_resp;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "exp_code_setup"
  exp_code_setupClock = new util.Clock();
  // Initialize components for Routine "block_instruction"
  block_instructionClock = new util.Clock();
  instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions',
    text: undefined,
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  start_block = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  target_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_image', units : 'deg', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  probe_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'probe_image', units : 'deg', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  fix_response = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_response',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var exp_code_setupComponents;
function exp_code_setupRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'exp_code_setup'-------
    t = 0;
    exp_code_setupClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    exp_code_setupComponents = [];
    
    for (const thisComponent of exp_code_setupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function exp_code_setupRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'exp_code_setup'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = exp_code_setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of exp_code_setupComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function exp_code_setupRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'exp_code_setup'-------
    for (const thisComponent of exp_code_setupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "exp_code_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var blocks;
var currentLoop;
function blocksLoopBegin(blocksLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'block_types_A.csv',
    seed: undefined, name: 'blocks'
  });
  psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
  currentLoop = blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlock of blocks) {
    const snapshot = blocks.getSnapshot();
    blocksLoopScheduler.add(importConditions(snapshot));
    blocksLoopScheduler.add(block_instructionRoutineBegin(snapshot));
    blocksLoopScheduler.add(block_instructionRoutineEachFrame(snapshot));
    blocksLoopScheduler.add(block_instructionRoutineEnd(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    blocksLoopScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    blocksLoopScheduler.add(trialsLoopScheduler);
    blocksLoopScheduler.add(trialsLoopEnd);
    blocksLoopScheduler.add(endLoopIteration(blocksLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 24, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(trialRoutineBegin(trials.getSnapshot()));
    trialsLoopScheduler.add(trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function blocksLoopEnd() {
  psychoJS.experiment.removeLoop(blocks);

  return Scheduler.Event.NEXT;
}


var paths;
var trial_order;
var trialSame;
var trialDiff;
var diffTrial;
var sameTrialid;
var diffTrialid;
var _start_block_allKeys;
var block_instructionComponents;
function block_instructionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'block_instruction'-------
    t = 0;
    block_instructionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    
            // add-on: list(s: string): string[]
            function list(s) {
                // if s is a string, we return a list of its characters
                if (typeof s === 'string')
                    return s.split('');
                else
                    // otherwise we return s:
                    return s;
            }
    
            if ((Block_type === "conf_face")) {
                paths = face_config_paths;
            } 
            else {
            if ((Block_type === "conf_haus")) {
                paths = haus_config_paths;
            } 
            else {
            if ((Block_type === "feat_face")) {
                paths = face_feat_paths;
            } 
            else {
            if ((Block_type === "feat_haus")) {
                paths = haus_feat_paths;
            }
            }
        }
    }
    
    function shuffle(array) {
        for (let i = array.length - 1; i > 0; i--) {
            let j = Math.floor(Math.random() * (i + 1)); // random index from 0 to i

            // swap elements array[i] and array[j]
            // we use "destructuring assignment" syntax to achieve that
            // you'll find more details about that syntax in later chapters
            // same can be written as:
            // let t = array[i]; array[i] = array[j]; array[j] = t
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array
    }

    function divide_subPoint1(array, divisor) {
        let array_divided = array.map(function(element) {
	          return element/divisor - 0.1;
        });
        return array_divided
    }

    function round(array) {
            let array_rounded = array.map(function(each_element){
            return Math.round(each_element);
        }); 
        return array_rounded
    }

    trial_order = [shuffle([1, 2, 3, 4, 5, 6]), shuffle([1, 2, 3, 4, 5, 6]), shuffle([1, 2, 3, 4, 5, 6]), shuffle([1, 2, 3, 4, 5, 6])].flat();
    trial_order = round(divide_subPoint1(trial_order,6))
    trialSame = [shuffle([0, 1, 2, 3]), shuffle([0, 1, 2, 3]), shuffle([0, 1, 2, 3])].flat();
    trialDiff = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [1, 0], [2, 3], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2]];
    diffTrial = list([...Array(12).keys()]);
    shuffle(diffTrial);
    sameTrialid = 0;
    diffTrialid = 0;
    console.log(Block_type)
    console.log(paths)
    console.log(trial_order)
    console.log(trialSame)
    console.log(diffTrial)
    console.log(trialDiff[5])
    instructions.setText(instruction_text);
    start_block.keys = undefined;
    start_block.rt = undefined;
    _start_block_allKeys = [];
    // keep track of which components have finished
    block_instructionComponents = [];
    block_instructionComponents.push(instructions);
    block_instructionComponents.push(start_block);
    
    for (const thisComponent of block_instructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function block_instructionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'block_instruction'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = block_instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions* updates
    if (t >= 0 && instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions.tStart = t;  // (not accounting for frame time here)
      instructions.frameNStart = frameN;  // exact frame index
      
      instructions.setAutoDraw(true);
    }

    
    // *start_block* updates
    if (t >= 0.0 && start_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_block.tStart = t;  // (not accounting for frame time here)
      start_block.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start_block.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start_block.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { start_block.clearEvents(); });
    }

    if (start_block.status === PsychoJS.Status.STARTED) {
      let theseKeys = start_block.getKeys({keyList: ['space'], waitRelease: false});
      _start_block_allKeys = _start_block_allKeys.concat(theseKeys);
      if (_start_block_allKeys.length > 0) {
        start_block.keys = _start_block_allKeys[_start_block_allKeys.length - 1].name;  // just the last key pressed
        start_block.rt = _start_block_allKeys[_start_block_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of block_instructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function block_instructionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'block_instruction'-------
    for (const thisComponent of block_instructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('start_block.keys', start_block.keys);
    if (typeof start_block.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('start_block.rt', start_block.rt);
        routineTimer.reset();
        }
    
    start_block.stop();
    // the Routine "block_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var target;
var probe;
var _key_resp_allKeys;
var trialComponents;
function trialRoutineBegin() {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if ((trial_order[trials.thisN] === 1)) {
        target = paths[trialSame[sameTrialid]];
        probe = paths[trialSame[sameTrialid]];
        sameTrialid += 1;
    } else {
        if ((trial_order[trials.thisN] === 0)) {
            img_pair = trialDiff[diffTrial[diffTrialid]];
            target = paths[img_pair[0]];
            probe = paths[img_pair[1]];
            diffTrialid += 1;
        }
    }
    console.log(thisN)
    console.log(trials.thisN)
    console.log(target)
    console.log(thisTrialN)
    console.log(trial.thisN)
    target_image.setImage(target);
    probe_image.setImage(probe);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(target_image);
    trialComponents.push(fixation);
    trialComponents.push(probe_image);
    trialComponents.push(fix_response);
    trialComponents.push(key_resp);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_image* updates
    if (t >= 0.0 && target_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_image.tStart = t;  // (not accounting for frame time here)
      target_image.frameNStart = frameN;  // exact frame index
      
      target_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target_image.setAutoDraw(false);
    }
    
    // *fixation* updates
    if (t >= 0.2 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    frameRemains = 0.2 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // *probe_image* updates
    if (t >= 0.5 && probe_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe_image.tStart = t;  // (not accounting for frame time here)
      probe_image.frameNStart = frameN;  // exact frame index
      
      probe_image.setAutoDraw(true);
    }

    frameRemains = 0.5 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (probe_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      probe_image.setAutoDraw(false);
    }
    
    // *fix_response* updates
    if (t >= 0.7 && fix_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_response.tStart = t;  // (not accounting for frame time here)
      fix_response.frameNStart = frameN;  // exact frame index
      
      fix_response.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.7 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['s', 'd'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
    
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
