import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def checkParams(filename, design, patient, hemi=None):
    # function: extract experiment parameters to check position
    data = pd.read_csv(filename)
    if design == data['design'][0]:
        print('Design assignment was correct.')
    else:
        print('The design assignment was incorrect. \nYou put '
              + str(design) + ' but the design was ' + str(data['design'][0]) + '.')

    if data['position'][0] != 2:
        if patient == 1:
            if hemi is None:
                print('Patient\'s resection side was not stated.')
            elif hemi == 'left':
                if data['position'][0] == 1:
                    print('Patient had left sided resection, stimuli were presented on the correct side.')
                else:
                    print('Oh no! Patient had left sided resection, stimuli were presented on the blind side.')
            elif hemi == 'right':
                if data['position'][0] == 3:
                    print('Patient had right sided resection, stimuli were presented on the correct side.')
                else:
                    print('Oh no! Patient had right sided resection, stimuli were presented on the blind side.')
            else:
                print('Error: unknown hemi input.')
        else:
            print('Oh no! You presented a stimulus on only one side to a healthy volunteer.')
    else:
        if patient == 0:
            print('Stimuli were presented to healthy volunteer on both sides.')
        else:
            print('Oh no! Stimuli were presented to a patient on both sides.')
def extractData(filename):
    # design 1 and 4: run 1 = local,  run 2 = global
    # design 2 and 3: run 1 = global, run 2 = local
    global cond_accs, cond_RTs, nTrials, d_primes
    data = pd.read_csv(filename)
    data = data.loc[:, ['design', 'position', 'runID', 'stimLabel', 'side', 'trial_resp.corr', 'trial_resp.rt', 'trial_resp.keys']]
    data = data.dropna()
    data = data[data['trial_resp.rt'] < 5].reset_index()
    if data['position'].array[0] != 2:
        if data['design'].array[0] == 1 or data['design'].array[0] == 4:
            loca_congr = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('congr'))]
            loca_incon = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('incon'))]
            glob_congr = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('congr'))]
            glob_incon = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('incon'))]
        else:
            loca_congr = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('congr'))]
            loca_incon = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('incon'))]
            glob_congr = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('congr'))]
            glob_incon = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('incon'))]

        cond_accuracy_means = [loca_congr['trial_resp.corr'].mean(),
                               loca_incon['trial_resp.corr'].mean(),
                               glob_congr['trial_resp.corr'].mean(),
                               glob_incon['trial_resp.corr'].mean()]
        cond_accs = cond_accuracy_means

        cond_RT_means = [loca_congr['trial_resp.rt'].mean(),
                         loca_incon['trial_resp.rt'].mean(),
                         glob_congr['trial_resp.rt'].mean(),
                         glob_incon['trial_resp.rt'].mean()]
        cond_RT_stds = [loca_congr['trial_resp.rt'].std(),
                        loca_incon['trial_resp.rt'].std(),
                        glob_congr['trial_resp.rt'].std(),
                        glob_incon['trial_resp.rt'].std()]
        cond_RTs = (cond_RT_means, cond_RT_stds)

        nTrials = len(loca_congr['trial_resp.rt'])
        conditions = [(loca_congr, loca_incon), (glob_congr, glob_incon)]
    else:
        if data['design'].array[0] == 1 or data['design'].array[0] == 4:
            loca_congrL = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('congr')) & data['side'].str.contains('right')]
            loca_inconL = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('incon')) & data['side'].str.contains('right')]
            glob_congrL = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('congr')) & data['side'].str.contains('right')]
            glob_inconL = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('incon')) & data['side'].str.contains('right')]
            loca_congrR = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('congr')) & data['side'].str.contains('left')]
            loca_inconR = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('incon')) & data['side'].str.contains('left')]
            glob_congrR = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('congr')) & data['side'].str.contains('left')]
            glob_inconR = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('incon')) & data['side'].str.contains('left')]
        else:
            loca_congrL = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('congr')) & data['side'].str.contains('right')]
            loca_inconL = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('incon')) & data['side'].str.contains('right')]
            glob_congrL = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('congr')) & data['side'].str.contains('right')]
            glob_inconL = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('incon')) & data['side'].str.contains('right')]
            loca_congrR = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('congr')) & data['side'].str.contains('left')]
            loca_inconR = data.loc[(data['runID'] == 2) & (data['stimLabel'].str.contains('incon')) & data['side'].str.contains('left')]
            glob_congrR = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('congr')) & data['side'].str.contains('left')]
            glob_inconR = data.loc[(data['runID'] == 1) & (data['stimLabel'].str.contains('incon')) & data['side'].str.contains('left')]

        cond_accs = [loca_congrL['trial_resp.corr'].mean(),
                     loca_inconL['trial_resp.corr'].mean(),
                     glob_congrL['trial_resp.corr'].mean(),
                     glob_inconL['trial_resp.corr'].mean(),
                     loca_congrR['trial_resp.corr'].mean(),
                     loca_inconR['trial_resp.corr'].mean(),
                     glob_congrR['trial_resp.corr'].mean(),
                     glob_inconR['trial_resp.corr'].mean()]

        cond_RT_means = [loca_congrL['trial_resp.rt'].mean(),
                         loca_inconL['trial_resp.rt'].mean(),
                         glob_congrL['trial_resp.rt'].mean(),
                         glob_inconL['trial_resp.rt'].mean(),
                         loca_congrR['trial_resp.rt'].mean(),
                         loca_inconR['trial_resp.rt'].mean(),
                         glob_congrR['trial_resp.rt'].mean(),
                         glob_inconR['trial_resp.rt'].mean()]
        cond_RT_stds = [loca_congrL['trial_resp.rt'].std(),
                        loca_inconL['trial_resp.rt'].std(),
                        glob_congrL['trial_resp.rt'].std(),
                        glob_inconL['trial_resp.rt'].std(),
                        loca_congrR['trial_resp.rt'].std(),
                        loca_inconR['trial_resp.rt'].std(),
                        glob_congrR['trial_resp.rt'].std(),
                        glob_inconR['trial_resp.rt'].std()]
        cond_RTs = (cond_RT_means, cond_RT_stds)

        nTrials = len(loca_congrL['trial_resp.rt'])
        conditions = [(loca_congrL, loca_inconL), (glob_congrL, glob_inconL),
                      (loca_congrR, loca_inconR), (glob_congrR, glob_inconR)]

    d_primes = []
    for congr, incon in conditions:
        hits = (len(congr[(congr['stimLabel'].str.contains('S')) & (congr['trial_resp.corr'] == 1)]) + len(incon[(incon['stimLabel'].str.contains('S')) & (incon['trial_resp.corr'] == 1)]))/len(congr['trial_resp.corr'])
        false_alarms = (len(congr[(congr['stimLabel'].str.contains('H')) & (congr['trial_resp.corr'] == 0)]) + len(incon[(incon['stimLabel'].str.contains('H')) & (incon['trial_resp.corr'] == 0)]))/len(congr['trial_resp.corr'])
        print(hits)
        print(false_alarms)
        if hits == 1:
            hits = hits - 0.000000000001
        elif hits == 0:
            hits = hits + 0.000000000001

        if false_alarms == 1:
            false_alarms = false_alarms - 0.000000000001
        elif false_alarms == 0:
            false_alarms = false_alarms + 0.000000000001

        z_hit = norm.ppf(hits)
        z_fal = norm.ppf(false_alarms)
        d_primes.append(z_hit - z_fal)
    print(d_primes)

    return cond_accs, cond_RTs, nTrials, d_primes
def plotGlobLoca(cond_accs, cond_RTs, nTrials, d_primes, hemi=None):
    if len(cond_accs) < 5:
        # local accuracy
        x_val1 = [0, 1]
        y_val1 = [cond_accs[0], cond_accs[1]]
        # global accuracy
        x_val2 = [0, 1]
        y_val2 = [cond_accs[2], cond_accs[3]]
        # local RT
        x_val3 = [0, 1]
        y_val3 = [cond_RTs[0][0], cond_RTs[0][1]]
        # global RT
        x_val4 = [0, 1]
        y_val4 = [cond_RTs[0][2], cond_RTs[0][3]]

        plt.errorbar(x_val1, y_val1,
                     linestyle='--', elinewidth=1.5, capsize=3.5)
        plt.errorbar(x_val2, y_val2,
                     linestyle='-', elinewidth=1.5, capsize=3.5)
        plt.plot([-0.5, 1.5], [1, 1], color='black', linestyle='--', linewidth=0.5)
        plt.figlegend(['ceiling', 'local', 'global'], framealpha=1)
        plt.title('Accuracy')
        plt.xlim([-0.5, 1.5])
        plt.ylim([0, 1.2])
        plt.xticks([0, 1], ['congruent', 'incongruent'])
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.show()

        plt.errorbar(x_val3, y_val3, yerr=[cond_RTs[1][0]/np.sqrt(nTrials), cond_RTs[1][1]/np.sqrt(nTrials)],
                     linestyle='--', elinewidth=1.5, capsize=3.5)
        plt.errorbar(x_val4, y_val4, yerr=[cond_RTs[1][2]/np.sqrt(nTrials), cond_RTs[1][3]/np.sqrt(nTrials)],
                     linestyle='-', elinewidth=1.5, capsize=3.5)
        plt.figlegend(['local', 'global'], framealpha=1)
        plt.title('Reaction Time (s)')
        plt.xlim([-0.5, 1.5])
        plt.ylim([1, 2.75])
        plt.xticks([0, 1], ['congruent', 'incongruent'])
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.show()

        plt.bar(['local', 'global'],
                 d_primes)
        if hemi == 'left':
            plt.title('Left Hemispherectomy')
        elif hemi == 'right':
            plt.title('Right Hemispherectomy')
        else:
            plt.title('Resection Unspecified')
        plt.show()
    else:
        # local accuracy
        x_val1L = [0, 1]
        y_val1L = [cond_accs[0], cond_accs[1]]
        x_val1R = [0, 1]
        y_val1R = [cond_accs[4], cond_accs[5]]
        # global accuracy
        x_val2L = [0, 1]
        y_val2L = [cond_accs[2], cond_accs[3]]
        x_val2R = [0, 1]
        y_val2R = [cond_accs[6], cond_accs[7]]
        # local RT
        x_val3L = [0, 1]
        y_val3L = [cond_RTs[0][0], cond_RTs[0][1]]
        x_val3R = [0, 1]
        y_val3R = [cond_RTs[0][4], cond_RTs[0][5]]
        # global RT
        x_val4L = [0, 1]
        y_val4L = [cond_RTs[0][2], cond_RTs[0][3]]
        x_val4R = [0, 1]
        y_val4R = [cond_RTs[0][6], cond_RTs[0][7]]

        plt.errorbar(x_val1L, y_val1L,
                     linestyle='--', elinewidth=1.5, capsize=3.5, color='red')
        plt.errorbar(x_val1R, y_val1R,
                     linestyle='--', elinewidth=1.5, capsize=3.5, color='pink')
        plt.errorbar(x_val2L, y_val2L,
                     linestyle='-', elinewidth=1.5, capsize=3.5, color='blue')
        plt.errorbar(x_val2R, y_val2R,
                     linestyle='-', elinewidth=1.5, capsize=3.5, color='green')
        plt.plot([-0.5, 1.5], [1, 1], color='black', linestyle='--', linewidth=0.5)
        plt.figlegend(['ceiling', 'localL', 'localR', 'globalL',  'localR'], framealpha=1)
        plt.title('Accuracy')
        plt.xlim([-0.5, 1.5])
        plt.ylim([0, 1.2])
        plt.xticks([0, 1], ['congruent', 'incongruent'])
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.show()

        plt.errorbar(x_val3L, y_val3L, yerr=[cond_RTs[1][0] / np.sqrt(nTrials), cond_RTs[1][1] / np.sqrt(nTrials)],
                     linestyle='--', elinewidth=1.5, capsize=3.5, color='red')
        plt.errorbar(x_val3R, y_val3R, yerr=[cond_RTs[1][4] / np.sqrt(nTrials), cond_RTs[1][5] / np.sqrt(nTrials)],
                     linestyle='--', elinewidth=1.5, capsize=3.5, color='pink')
        plt.errorbar(x_val4L, y_val4L, yerr=[cond_RTs[1][2] / np.sqrt(nTrials), cond_RTs[1][3] / np.sqrt(nTrials)],
                     linestyle='-', elinewidth=1.5, capsize=3.5, color='blue')
        plt.errorbar(x_val4R, y_val4R, yerr=[cond_RTs[1][6] / np.sqrt(nTrials), cond_RTs[1][7] / np.sqrt(nTrials)],
                     linestyle='-', elinewidth=1.5, capsize=3.5, color='green')
        plt.figlegend(['localL', 'localR', 'globalL', 'globalR'], framealpha=1)
        plt.title('Reaction Time (s)')
        plt.xlim([-0.5, 1.5])
        plt.ylim([0, 2.75])
        plt.xticks([0, 1], ['congruent', 'incongruent'])
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.show()

        plt.bar(['local_L', 'global_L',
                 'local_R', 'global_R'],
                 d_primes)
        plt.show()

filename = './GlobLocaData/nb_global_local_2020-11-20_14h34.11.055.csv'
checkParams(filename, 1, 1, hemi='right')
cond_accs00, cond_RTs00, nTrials00 = extractData(filename)
plotGlobLoca(cond_accs00, cond_RTs00, nTrials00)

filename = './GlobLocaData/RH_global_local_2020-11-24_16h08.23.919.csv'
checkParams(filename, 1, 2, hemi='right')
cond_accs0, cond_RTs0, nTrials0 = extractData(filename)
plotGlobLoca(cond_accs0, cond_RTs0, nTrials0)

filename = './GlobLocaData/HK_global_local_2020-11-29_11h21.21.703.csv'
checkParams(filename, 1, 1, hemi='left')
cond_accs1, cond_RTs1, nTrials1, d_primes = extractData(filename)
plotGlobLoca(cond_accs1, cond_RTs1, nTrials1, d_primes, hemi='left')

filename = './GlobLocaData/LK_global_local_2020-11-29_15h03.04.677.csv'
checkParams(filename, 2, 1, hemi='left')
cond_accs2, cond_RTs2, nTrials2 = extractData(filename)
plotGlobLoca(cond_accs2, cond_RTs2, nTrials2)

filename = './GlobLocaData/HO_global_local_2020-11-30_15h41.01.735.csv'
checkParams(filename, 3, 1, hemi='left')
cond_accs3, cond_RTs3, nTrials3 = extractData(filename)
plotGlobLoca(cond_accs3, cond_RTs3, nTrials3)

filename = './GlobLocaData/dt_global_local_2020-12-01_15h30.39.378.csv'
hemi = 'right'
checkParams(filename, 4, 1, hemi)
cond_accs4, cond_RTs4, nTrials4 = extractData(filename)
plotGlobLoca(cond_accs4, cond_RTs4, nTrials4, d_primes, hemi)

filename = './GlobLocaData/AL_global_local_2020-11-06_04h56.37.462.csv'
checkParams(filename, 1, 0)
cond_accs4, cond_RTs4, nTrials4,d_primes = extractData(filename)
plotGlobLoca(cond_accs4, cond_RTs4, nTrials4, d_primes)

filename = './GlobLocaData/mb_global_local_2020-10-26_14h04.36.230.csv'
checkParams(filename, 1, 0)
cond_accs4, cond_RTs4, nTrials4, d_primes = extractData(filename)
plotGlobLoca(cond_accs4, cond_RTs4, nTrials4, d_primes)

filename = './GlobLocaData/ak_global_local_2020-12-03_11h02.43.004.csv'
hemi = 'left'
checkParams(filename, 3, 1, hemi)
cond_accs4, cond_RTs4, nTrials4, d_primes = extractData(filename)
plotGlobLoca(cond_accs4, cond_RTs4, nTrials4, d_primes, hemi)