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
    global cond_accs, cond_RTs, nTrials, conf_haus, conf_face, feat_haus, feat_face, d_primes, cond_REs
    data = pd.read_csv(filename)
    data = data.loc[:, ['design', 'position', 'block_type',
                        'trial_type1S0D', 'side', 'key_resp.corr',
                        'key_resp.rt', 'key_resp.keys']]
    data = data.dropna()
    plt.scatter(range(len(data['key_resp.rt'])), data['key_resp.rt'])
    plt.plot([0, len(data['key_resp.rt'])], [5, 5], color='black', linestyle='--', linewidth=0.5)
    plt.show()
    reaction_time_cutoff = 5
    data = data[data['key_resp.rt'] < reaction_time_cutoff].reset_index()
    if data['position'].array[0] != 2:
        conf_haus = data.loc[data['block_type'].str.contains('conf_haus'), :]
        conf_face = data.loc[data['block_type'].str.contains('conf_face'), :]
        feat_haus = data.loc[data['block_type'].str.contains('feat_haus'), :]
        feat_face = data.loc[data['block_type'].str.contains('feat_face'), :]

        cond_accs = [conf_haus['key_resp.corr'].mean(),
                               conf_face['key_resp.corr'].mean(),
                               feat_haus['key_resp.corr'].mean(),
                               feat_face['key_resp.corr'].mean()]

        cond_RT_means = [conf_haus['key_resp.rt'].mean(),
                         conf_face['key_resp.rt'].mean(),
                         feat_haus['key_resp.rt'].mean(),
                         feat_face['key_resp.rt'].mean()]
        cond_RT_stds = [conf_haus['key_resp.rt'].std(),
                        conf_face['key_resp.rt'].std(),
                        feat_haus['key_resp.rt'].std(),
                        feat_face['key_resp.rt'].std()]
        cond_RTs = (cond_RT_means, cond_RT_stds)

        cond_IE_conf_haus_means = (1 - np.array(conf_haus['key_resp.corr']).mean() / np.array(conf_haus['key_resp.rt']).mean())
        cond_IE_conf_face_means = (1 - np.array(conf_face['key_resp.corr']).mean() / np.array(conf_face['key_resp.rt']).mean())
        cond_IE_feat_haus_means = (1 - np.array(feat_haus['key_resp.corr']).mean() / np.array(feat_haus['key_resp.rt']).mean())
        cond_IE_feat_face_means = (1 - np.array(feat_face['key_resp.corr']).mean() / np.array(feat_face['key_resp.rt']).mean())

        cond_REs = [cond_IE_conf_haus_means,
                    cond_IE_conf_face_means,
                    cond_IE_feat_haus_means,
                    cond_IE_feat_face_means]
        nTrials = len(conf_haus['key_resp.rt'])

        conditions = [conf_haus, conf_face, feat_haus, feat_face]

    else:
        conf_hausL = data.loc[(data['block_type'].str.contains('conf_haus') & (data['side'] > 0)), :]
        conf_faceL = data.loc[(data['block_type'].str.contains('conf_face') & (data['side'] > 0)), :]
        feat_hausL = data.loc[(data['block_type'].str.contains('feat_haus') & (data['side'] > 0)), :]
        feat_faceL = data.loc[(data['block_type'].str.contains('feat_face') & (data['side'] > 0)), :]

        conf_hausR = data.loc[(data['block_type'].str.contains('conf_haus') & (data['side'] < 0)), :]
        conf_faceR = data.loc[(data['block_type'].str.contains('conf_face') & (data['side'] < 0)), :]
        feat_hausR = data.loc[(data['block_type'].str.contains('feat_haus') & (data['side'] < 0)), :]
        feat_faceR = data.loc[(data['block_type'].str.contains('feat_face') & (data['side'] < 0)), :]

        cond_accs = [conf_hausL['key_resp.corr'].mean(),
                     conf_faceL['key_resp.corr'].mean(),
                     feat_hausL['key_resp.corr'].mean(),
                     feat_faceL['key_resp.corr'].mean(),
                     conf_hausR['key_resp.corr'].mean(),
                     conf_faceR['key_resp.corr'].mean(),
                     feat_hausR['key_resp.corr'].mean(),
                     feat_faceR['key_resp.corr'].mean()]

        cond_RT_means = [conf_hausL['key_resp.rt'].mean(),
                         conf_faceL['key_resp.rt'].mean(),
                         feat_hausL['key_resp.rt'].mean(),
                         feat_faceL['key_resp.rt'].mean(),
                         conf_hausR['key_resp.rt'].mean(),
                         conf_faceR['key_resp.rt'].mean(),
                         feat_hausR['key_resp.rt'].mean(),
                         feat_faceR['key_resp.rt'].mean()]
        cond_RT_stds = [conf_hausL['key_resp.rt'].std(),
                        conf_faceL['key_resp.rt'].std(),
                        feat_hausL['key_resp.rt'].std(),
                        feat_faceL['key_resp.rt'].std(),
                        conf_hausR['key_resp.rt'].std(),
                        conf_faceR['key_resp.rt'].std(),
                        feat_hausR['key_resp.rt'].std(),
                        feat_faceR['key_resp.rt'].std()]
        cond_RTs = (cond_RT_means, cond_RT_stds)

        cond_IE_conf_haus_meansL = (1 - np.array(conf_hausL['key_resp.corr']).mean() / np.array(conf_hausL['key_resp.rt']).mean())
        cond_IE_conf_face_meansL = (1 - np.array(conf_faceL['key_resp.corr']).mean() / np.array(conf_faceL['key_resp.rt']).mean())
        cond_IE_feat_haus_meansL = (1 - np.array(feat_hausL['key_resp.corr']).mean() / np.array(feat_hausL['key_resp.rt']).mean())
        cond_IE_feat_face_meansL = (1 - np.array(feat_faceL['key_resp.corr']).mean() / np.array(feat_faceL['key_resp.rt']).mean())

        cond_IE_conf_haus_meansR = (1 - np.array(conf_hausR['key_resp.corr']).mean() / np.array(conf_hausR['key_resp.rt']).mean())
        cond_IE_conf_face_meansR = (1 - np.array(conf_faceR['key_resp.corr']).mean() / np.array(conf_faceR['key_resp.rt']).mean())
        cond_IE_feat_haus_meansR = (1 - np.array(feat_hausR['key_resp.corr']).mean() / np.array(feat_hausR['key_resp.rt']).mean())
        cond_IE_feat_face_meansR = (1 - np.array(feat_faceR['key_resp.corr']).mean() / np.array(feat_faceR['key_resp.rt']).mean())

        cond_REs = [cond_IE_conf_haus_meansL,
                    cond_IE_conf_face_meansL,
                    cond_IE_feat_haus_meansL,
                    cond_IE_feat_face_meansL,
                    cond_IE_conf_haus_meansR,
                    cond_IE_conf_face_meansR,
                    cond_IE_feat_haus_meansR,
                    cond_IE_feat_face_meansR]
        nTrials = len(conf_hausL['key_resp.rt'])

        conditions = [conf_hausL, conf_faceL, feat_hausL, feat_faceL,
                      conf_hausR, conf_faceR, feat_hausR, feat_faceR]

    z_hit = []
    z_fal = []
    for iCond in conditions:
        hits = []  # hits = same trial, same button
        false_alarms = []  # false alarm, diff trial, same button
        hits.append(len(iCond[(iCond['trial_type1S0D'] == 1) & (iCond['key_resp.corr'] == 1)]) / len(
            iCond[(iCond['trial_type1S0D'] == 1)]))
        false_alarms.append(len(iCond[(iCond['trial_type1S0D'] == 0) & (iCond['key_resp.corr'] == 0)]) / len(
            iCond[(iCond['trial_type1S0D'] == 1)]))
        z_hit.append(norm.ppf(np.sum(hits), loc=0, scale=1))
        z_fal.append(norm.ppf(np.sum(false_alarms), loc=0, scale=1))
    d_primes = np.array(z_hit) - np.array(z_fal)

    return cond_accs, cond_RTs, cond_REs, nTrials, d_primes


def plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes):
    if len(cond_accs) < 5:
        cond_names = ['cH', 'cF', 'fH', 'fF']
        colors = ['darkred', 'red', 'palevioletred', 'pink']  # 'darkblue','blue','dodgerblue','deepskyblue']
    else:
        cond_names = ['cHL', 'cFL', 'fHL', 'fFL', 'cHR', 'cFR', 'fHR', 'fFR']
        colors = ['darkred', 'darkblue', 'red', 'blue', 'palevioletred', 'dodgerblue', 'pink', 'deepskyblue']

    if len(cond_accs) < 5:
        fig, axs = plt.subplots(2, 2)
        axs[0, 0].bar(cond_names,
                          cond_accs,
                          color=colors)
        axs[0, 0].set_ylim([0, 1])
        axs[0, 0].set_title('Average Configural/Featural Accuracy')
        axs[0, 0].plot([-0.5, len(cond_accs)], [0.5, 0.5], color='black', linestyle='--', linewidth=0.5)

        axs[1, 0].bar(cond_names,
                      cond_RTs[0],
                      color=colors,
                      yerr=cond_RTs[1])
        axs[1, 0].set_ylim([0, 4])
        axs[1, 0].set_title('Average Configural/Featural RTs (s)')

        axs[0, 1].bar(cond_names,
                      d_primes,
                      color=colors)
        axs[0, 1].set_title('D Primes')

        axs[1, 1].bar(cond_names,
                      cond_REs,
                      color=colors)
        axs[1, 1].set_ylim([0, 1])
        axs[1, 1].set_title('Inverse Efficiency Score')
        plt.show()
    else:
        fig1, axs1 = plt.subplots(2, 2)
        axs1[0, 0].bar(cond_names[0:4],
                      cond_accs[0:4],
                      color=colors[0:4])
        axs1[0, 0].set_ylim([0, 1])
        axs1[0, 0].set_title('LEFT Avg Configural/Featural Accuracy')
        axs1[0, 0].plot([-0.5, len(cond_accs)/2], [0.5, 0.5], color='black', linestyle='--', linewidth=0.5)

        axs1[1, 0].bar(cond_names[0:4],
                      cond_RTs[0][0:4],
                      color=colors[0:4],
                      yerr=cond_RTs[1][0:4])
        axs1[1, 0].set_ylim([0, 4])
        axs1[1, 0].set_title('LEFT Avg Configural/Featural RTs (s)')

        axs1[0, 1].bar(cond_names[0:4],
                      d_primes[0:4],
                      color=colors[0:4])
        axs1[0, 1].set_title('LEFT D Primes')

        axs1[1, 1].bar(cond_names[0:4],
                      cond_REs[0:4],
                      color=colors[0:4])
        axs1[1, 1].set_ylim([0, 1])
        axs1[1, 1].set_title('LEFT Inverse Efficiency Score')
        plt.show()

        fig2, axs2 = plt.subplots(2, 2)
        axs2[0, 0].bar(cond_names[4:8],
                      cond_accs[4:8],
                      color=colors[4:8])
        axs2[0, 0].set_ylim([0, 1])
        axs2[0, 0].set_title('RIGHT Avg Configural/Featural Accuracy')
        axs2[0, 0].plot([-0.5, len(cond_accs)/2], [0.5, 0.5], color='black', linestyle='--', linewidth=0.5)

        axs2[1, 0].bar(cond_names[4:8],
                      cond_RTs[0][4:8],
                      color=colors[4:8],
                      yerr=cond_RTs[1][4:8])
        axs2[1, 0].set_ylim([0, 4])
        axs2[1, 0].set_title('RIGHT Avg Configural/Featural RTs (s)')

        axs2[0, 1].bar(cond_names[4:8],
                      d_primes[4:8],
                      color=colors[4:8])
        axs2[0, 1].set_title('RIGHT D Primes')

        axs2[1, 1].bar(cond_names[4:8],
                      cond_REs[4:8],
                      color=colors[4:8])
        axs2[1, 1].set_ylim([0, 1])
        axs2[1, 1].set_title('RIGHT Inverse Efficiency Score')
        plt.show()

filename = './ConfFeatData/RH_configural_featural_2020-11-24_15h44.30.118.csv'
checkParams(filename, 2, 1, hemi='right')
cond_accs, cond_RTs, cond_REs, nTrials, d_primes = extractData(filename)
plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes)

filename = './ConfFeatData/nb_configural_featural_2020-11-20_14h08.02.638.csv'
checkParams(filename, 1, 1, hemi='right')
cond_accs, cond_RTs, cond_REs, nTrials, d_primes = extractData(filename)
plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes)

filename = './ConfFeatData/HK_configural_featural_2020-11-29_11h00.22.904.csv'
checkParams(filename, 1, 1, hemi='left')
cond_accs, cond_RTs, cond_REs, nTrials, d_primes = extractData(filename)
plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes)

filename = './ConfFeatData/ho_configural_featural_2020-11-30_15h05.25.402.csv'
checkParams(filename, 3, 1, hemi='left')
cond_accs, cond_RTs, cond_REs, nTrials, d_primes = extractData(filename)
plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes)

filename = './ConfFeatData/LK_configural_featural_2020-11-29_14h31.10.160.csv'
checkParams(filename, 1, 1, hemi='left')
cond_accs, cond_RTs, cond_REs, nTrials, d_primes = extractData(filename)
plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes)

filename = './ConfFeatData/dt_configural_featural_2020-12-01_15h06.32.323.csv'
checkParams(filename, 4, 1, hemi='right')
cond_accs, cond_RTs, cond_REs, nTrials, d_primes = extractData(filename)
plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes)

filename = './ConfFeatData/AL_configural_featural_2020-11-06_04h28.09.977.csv'
checkParams(filename, 1, 0)
cond_accs, cond_RTs, cond_REs, nTrials, d_primes = extractData(filename)
plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes)

filename = './ConfFeatData/DP_configural_featural_2020-11-16_09h33.10.896.csv'
checkParams(filename, 2, 0)
cond_accs, cond_RTs, cond_REs, nTrials, d_primes = extractData(filename)
plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes)

filename = './ConfFeatData/ak_configural_featural_2020-12-03_10h20.48.894.csv'
checkParams(filename, 2, 1, hemi='left')
cond_accs, cond_RTs, cond_REs, nTrials, d_primes = extractData(filename)
plotConfFeat(cond_accs, cond_RTs, cond_REs, d_primes)