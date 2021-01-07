from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outputData = pd.read_csv('./GlobLocaData/mb_global_local_2020-10-26_14h04.36.230.csv')
outputData2 = pd.read_csv('./GlobLocaData/AL_global_local_2020-11-06_04h56.37.462.csv')
outputData3 = pd.read_csv('./GlobLocaData/nb_global_local_2020-11-20_14h34.11.055.csv')
outputData4 = pd.read_csv('./GlobLocaData/RH_global_local_2020-11-24_16h08.23.919.csv')


# design 1: run 1 = local,  run 2 = global
# design 2: run 1 = global, run 2 = local
# design 3: run 1 = global, run 2 = local
# design 4: run 1 = local,  run 2 = global

# extract design, run, stimLabel, side, trial_resp.corr, trial_resp.rt

respData = outputData.loc[:, ['design', 'runID', 'stimLabel', 'side', 'trial_resp.corr', 'trial_resp.rt', 'trial_resp.keys']]
respData = respData.dropna()

loca_cong3L = respData.loc[(respData['runID'] == 1) & (respData['stimLabel'].str.contains('congr')) & respData['side'].str.contains('right')]
loca_inco3L = respData.loc[(respData['runID'] == 1) & (respData['stimLabel'].str.contains('incon')) & respData['side'].str.contains('right')]
glob_cong3L = respData.loc[(respData['runID'] == 2) & (respData['stimLabel'].str.contains('congr')) & respData['side'].str.contains('right')]
glob_inco3L = respData.loc[(respData['runID'] == 2) & (respData['stimLabel'].str.contains('incon')) & respData['side'].str.contains('right')]
loca_cong3R = respData.loc[(respData['runID'] == 1) & (respData['stimLabel'].str.contains('congr')) & respData['side'].str.contains('left')]
loca_inco3R = respData.loc[(respData['runID'] == 1) & (respData['stimLabel'].str.contains('incon')) & respData['side'].str.contains('left')]
glob_cong3R = respData.loc[(respData['runID'] == 2) & (respData['stimLabel'].str.contains('congr')) & respData['side'].str.contains('left')]
glob_inco3R = respData.loc[(respData['runID'] == 2) & (respData['stimLabel'].str.contains('incon')) & respData['side'].str.contains('left')]

respData2 = outputData2.loc(axis=1)['design', 'runID', 'stimLabel', 'side', 'trial_resp.corr', 'trial_resp.rt']
respData2 = respData2.dropna()

loca_cong4L = respData2.loc[(respData2['runID'] == 1) & (respData2['stimLabel'].str.contains('congr')) & respData2['side'].str.contains('right')]
loca_inco4L = respData2.loc[(respData2['runID'] == 1) & (respData2['stimLabel'].str.contains('incon')) & respData2['side'].str.contains('right')]
glob_cong4L = respData2.loc[(respData2['runID'] == 2) & (respData2['stimLabel'].str.contains('congr')) & respData2['side'].str.contains('right')]
glob_inco4L = respData2.loc[(respData2['runID'] == 2) & (respData2['stimLabel'].str.contains('incon')) & respData2['side'].str.contains('right')]
loca_cong4R = respData2.loc[(respData2['runID'] == 1) & (respData2['stimLabel'].str.contains('congr')) & respData2['side'].str.contains('left')]
loca_inco4R = respData2.loc[(respData2['runID'] == 1) & (respData2['stimLabel'].str.contains('incon')) & respData2['side'].str.contains('left')]
glob_cong4R = respData2.loc[(respData2['runID'] == 2) & (respData2['stimLabel'].str.contains('congr')) & respData2['side'].str.contains('left')]
glob_inco4R = respData2.loc[(respData2['runID'] == 2) & (respData2['stimLabel'].str.contains('incon')) & respData2['side'].str.contains('left')]

respData3 = outputData3.loc(axis=1)['design', 'runID', 'stimLabel', 'side', 'trial_resp.corr', 'trial_resp.rt', 'trial_resp.keys']
respData3 = respData3.dropna()

loca_cong1 = respData3.loc[(respData3['runID'] == 1) & (respData3['stimLabel'].str.contains('congr'))]
loca_inco1 = respData3.loc[(respData3['runID'] == 1) & (respData3['stimLabel'].str.contains('incon'))]
glob_cong1 = respData3.loc[(respData3['runID'] == 2) & (respData3['stimLabel'].str.contains('congr'))]
glob_inco1 = respData3.loc[(respData3['runID'] == 2) & (respData3['stimLabel'].str.contains('incon'))]

respData4 = outputData4.loc(axis=1)['design', 'runID', 'stimLabel', 'side', 'trial_resp.corr', 'trial_resp.rt', 'trial_resp.keys']
respData4 = respData4.dropna()

loca_cong2 = respData4.loc[(respData4['runID'] == 2) & (respData4['stimLabel'].str.contains('congr'))]
loca_inco2 = respData4.loc[(respData4['runID'] == 2) & (respData4['stimLabel'].str.contains('incon'))]
glob_cong2 = respData4.loc[(respData4['runID'] == 1) & (respData4['stimLabel'].str.contains('congr'))]
glob_inco2 = respData4.loc[(respData4['runID'] == 1) & (respData4['stimLabel'].str.contains('incon'))]


cond_accuracy_means = [loca_cong1['trial_resp.corr'].mean(),
                       loca_inco1['trial_resp.corr'].mean(),
                       glob_cong1['trial_resp.corr'].mean(),
                       glob_inco1['trial_resp.corr'].mean()]

cond_RT_means = [loca_cong1['trial_resp.rt'].mean(),
                 loca_inco1['trial_resp.rt'].mean(),
                 glob_cong1['trial_resp.rt'].mean(),
                 glob_inco1['trial_resp.rt'].mean()]

cond_RT_stds = [loca_cong1['trial_resp.rt'].std(),
                loca_inco1['trial_resp.rt'].std(),
                glob_cong1['trial_resp.rt'].std(),
                glob_inco1['trial_resp.rt'].std()]

cond_accuracy_means2 = [loca_cong2['trial_resp.corr'].mean(),
                       loca_inco2['trial_resp.corr'].mean(),
                       glob_cong2['trial_resp.corr'].mean(),
                       glob_inco2['trial_resp.corr'].mean()]

cond_RT_means2 = [loca_cong2['trial_resp.rt'].mean(),
                 loca_inco2['trial_resp.rt'].mean(),
                 glob_cong2['trial_resp.rt'].mean(),
                 glob_inco2['trial_resp.rt'].mean()]

cond_RT_stds2 = [loca_cong2['trial_resp.rt'].std(),
                loca_inco2['trial_resp.rt'].std(),
                glob_cong2['trial_resp.rt'].std(),
                glob_inco2['trial_resp.rt'].std()]

cond_accuracy_means3L = [np.array(loca_cong3L['trial_resp.corr'].mean(), loca_cong4L['trial_resp.corr'].mean()).mean(),
                        np.array(loca_inco3L['trial_resp.corr'].mean(), loca_inco4L['trial_resp.corr'].mean()).mean(),
                        np.array(glob_cong3L['trial_resp.corr'].mean(), glob_cong4L['trial_resp.corr'].mean()).mean(),
                        np.array(glob_inco3L['trial_resp.corr'].mean(), glob_inco4L['trial_resp.corr'].mean()).mean()]

cond_RT_means3L = [np.array(loca_cong3L['trial_resp.rt'].mean(), loca_cong4L['trial_resp.rt'].mean()).mean(),
                 np.array(loca_inco3L['trial_resp.rt'].mean(), loca_inco4L['trial_resp.rt'].mean()).mean(),
                 np.array(glob_cong3L['trial_resp.rt'].mean(), glob_cong4L['trial_resp.rt'].mean()).mean(),
                 np.array(glob_inco3L['trial_resp.rt'].mean(), glob_inco4L['trial_resp.rt'].mean()).mean()]

cond_RT_stds3L = [np.array(loca_cong3L['trial_resp.rt'].std(), loca_cong4L['trial_resp.rt'].std()).mean(),
                np.array(loca_inco3L['trial_resp.rt'].std(), loca_inco4L['trial_resp.rt'].std()).mean(),
                np.array(glob_cong3L['trial_resp.rt'].std(), glob_cong4L['trial_resp.rt'].std()).mean(),
                np.array(glob_inco3L['trial_resp.rt'].std(), glob_inco4L['trial_resp.rt'].std()).mean()]

cond_accuracy_means3R = [np.array(loca_cong3R['trial_resp.corr'].mean(), loca_cong4R['trial_resp.corr'].mean()).mean(),
                        np.array(loca_inco3R['trial_resp.corr'].mean(), loca_inco4R['trial_resp.corr'].mean()).mean(),
                        np.array(glob_cong3R['trial_resp.corr'].mean(), glob_cong4R['trial_resp.corr'].mean()).mean(),
                        np.array(glob_inco3R['trial_resp.corr'].mean(), glob_inco4R['trial_resp.corr'].mean()).mean()]

cond_RT_means3R = [np.array(loca_cong3R['trial_resp.rt'].mean(), loca_cong4R['trial_resp.rt'].mean()).mean(),
                 np.array(loca_inco3R['trial_resp.rt'].mean(), loca_inco4R['trial_resp.rt'].mean()).mean(),
                 np.array(glob_cong3R['trial_resp.rt'].mean(), glob_cong4R['trial_resp.rt'].mean()).mean(),
                 np.array(glob_inco3R['trial_resp.rt'].mean(), glob_inco4R['trial_resp.rt'].mean()).mean()]

cond_RT_stds3R = [np.array(loca_cong3R['trial_resp.rt'].std(), loca_cong4R['trial_resp.rt'].std()).mean(),
                np.array(loca_inco3R['trial_resp.rt'].std(), loca_inco4R['trial_resp.rt'].std()).mean(),
                np.array(glob_cong3R['trial_resp.rt'].std(), glob_cong4R['trial_resp.rt'].std()).mean(),
                np.array(glob_inco3R['trial_resp.rt'].std(), glob_inco4R['trial_resp.rt'].std()).mean()]

# local accuracy
x_val1 = [0, 1]
y_val1 = [cond_accuracy_means[0], cond_accuracy_means[1]]
# global accuracy
x_val2 = [0, 1]
y_val2 = [cond_accuracy_means[2], cond_accuracy_means[3]]
# local RT
x_val3 = [0, 1]
y_val3 = [cond_RT_means[0], cond_RT_means[1]]
# global RT
x_val4 = [0, 1]
y_val4 = [cond_RT_means[2], cond_RT_means[3]]

# local accuracy
x_val1_2 = [0, 1]
y_val1_2 = [cond_accuracy_means2[0], cond_accuracy_means2[1]]
# global accuracy
x_val2_2 = [0, 1]
y_val2_2 = [cond_accuracy_means2[2], cond_accuracy_means2[3]]
# local RT
x_val3_2 = [0, 1]
y_val3_2 = [cond_RT_means2[0], cond_RT_means2[1]]
# global RT
x_val4_2 = [0, 1]
y_val4_2 = [cond_RT_means2[2], cond_RT_means2[3]]

# local accuracy
x_val1_3L = [0, 1]
y_val1_3L = [cond_accuracy_means3L[0], cond_accuracy_means3L[1]]
# global accuracy
x_val2_3L = [0, 1]
y_val2_3L = [cond_accuracy_means3L[2], cond_accuracy_means3L[3]]
# local RT
x_val3_3L = [0, 1]
y_val3_3L = [cond_RT_means3L[0], cond_RT_means3L[1]]
# global RT
x_val4_3L = [0, 1]
y_val4_3L = [cond_RT_means3L[2], cond_RT_means3L[3]]

# local accuracy
x_val1_3R = [0, 1]
y_val1_3R = [cond_accuracy_means3R[0], cond_accuracy_means3R[1]]
# global accuracy
x_val2_3R = [0, 1]
y_val2_3R = [cond_accuracy_means3R[2], cond_accuracy_means3R[3]]
# local RT
x_val3_3R= [0, 1]
y_val3_3R = [cond_RT_means3R[0], cond_RT_means3R[1]]
# global RT
x_val4_3R = [0, 1]
y_val4_3R = [cond_RT_means3R[2], cond_RT_means3R[3]]


plt.errorbar(x_val1, y_val1, yerr=[cond_accuracy_stds[0], cond_accuracy_stds[1]],
             linestyle='--', elinewidth=1.5, capsize=3.5)
plt.errorbar(x_val2, y_val2, yerr=[cond_accuracy_stds[2], cond_accuracy_stds[3]],
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

plt.errorbar(x_val1, y_val1,
             linestyle='--', elinewidth=1.5, capsize=3.5, color='red')
plt.errorbar(x_val2, y_val2,
             linestyle='-', elinewidth=1.5, capsize=3.5, color='red')
plt.errorbar(x_val1_2, y_val1_2,
             linestyle='--', elinewidth=1.5, capsize=3.5, color='pink')
plt.errorbar(x_val2_2, y_val2_2,
             linestyle='-', elinewidth=1.5, capsize=3.5, color='pink')
plt.errorbar(x_val1_3L, y_val1_3L,
             linestyle='--', elinewidth=1.5, capsize=3.5, color='green')
plt.errorbar(x_val2_3L, y_val2_3L,
             linestyle='-', elinewidth=1.5, capsize=3.5, color='green')
plt.errorbar(x_val1_3R, y_val1_3R,
             linestyle='--', elinewidth=1.5, capsize=3.5, color='blue')
plt.errorbar(x_val2_3R, y_val2_3R,
             linestyle='-', elinewidth=1.5, capsize=3.5, color='blue')
plt.plot([-0.5, 1.5], [1, 1], color='black', linestyle='--', linewidth=0.5)
# plt.figlegend(['ceiling', 'P1_local', 'P1_global', 'P2_local', 'P2_global', 'CL_local', 'CL_global', 'CR_local', 'CR_global'], framealpha=1)
plt.figlegend(['ceiling', 'CL_local', 'CL_global', 'CR_local', 'CR_global'], framealpha=1)
plt.title('Accuracy')
plt.xlim([-0.5, 1.5])
plt.ylim([0, 1.2])
plt.xticks([0, 1], ['congruent', 'incongruent'])
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.show()

plt.errorbar(x_val3, y_val3, yerr=[cond_RT_stds[0]/np.sqrt(len(loca_cong1)), cond_RT_stds[1]/np.sqrt(len(loca_cong1))],
             linestyle='--', elinewidth=1.5, capsize=3.5, color='red')
plt.errorbar(x_val4, y_val4, yerr=[cond_RT_stds[2]/np.sqrt(len(loca_cong1)), cond_RT_stds[3]/np.sqrt(len(loca_cong1))],
             linestyle='-', elinewidth=1.5, capsize=3.5, color='red')
plt.errorbar(x_val3_2, y_val3_2, yerr=[cond_RT_stds2[0]/np.sqrt(len(loca_cong1)), cond_RT_stds2[1]/np.sqrt(len(loca_cong1))],
             linestyle='--', elinewidth=1.5, capsize=3.5, color='pink')
plt.errorbar(x_val4_2, y_val4_2, yerr=[cond_RT_stds2[2]/np.sqrt(len(loca_cong1)), cond_RT_stds2[3]/np.sqrt(len(loca_cong1))],
             linestyle='-', elinewidth=1.5, capsize=3.5, color='pink')
plt.errorbar(x_val3_3L, y_val3_3L, yerr=[cond_RT_stds3L[0]/np.sqrt(len(loca_cong1)/2), cond_RT_stds3L[1]/np.sqrt(len(loca_cong1)/2)],
             linestyle='--', elinewidth=1.5, capsize=3.5, color='green')
plt.errorbar(x_val4_3L, y_val4_3L, yerr=[cond_RT_stds3L[2]/np.sqrt(len(loca_cong1)), cond_RT_stds3L[3]/np.sqrt(len(loca_cong1)/2)],
             linestyle='-', elinewidth=1.5, capsize=3.5, color='green')
plt.errorbar(x_val3_3R, y_val3_3R, yerr=[cond_RT_stds3R[0]/np.sqrt(len(loca_cong1)), cond_RT_stds3R[1]/np.sqrt(len(loca_cong1)/2)],
             linestyle='--', elinewidth=1.5, capsize=3.5, color='blue')
plt.errorbar(x_val4_3R, y_val4_3R, yerr=[cond_RT_stds3R[2]/np.sqrt(len(loca_cong1)), cond_RT_stds3R[3]/np.sqrt(len(loca_cong1)/2)],
             linestyle='-', elinewidth=1.5, capsize=3.5, color='blue')
plt.figlegend(['P1_local', 'P1_global', 'P2_local', 'P2_global', 'CL_local', 'CL_global', 'CR_local', 'CR_global'], framealpha=1)
plt.title('Reaction Time (s)')
plt.xlim([-0.5, 1.5])
plt.ylim([0, max(cond_RT_means)+max(cond_RT_stds)])
plt.xticks([0, 1], ['congruent', 'incongruent'])
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.show()
