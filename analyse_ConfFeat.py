from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

outputData   = pd.read_csv('./ConfFeatData/sophie_configural_featural_2020-10-30_18h41.42.132.csv')
outputData2  = pd.read_csv('./ConfFeatData/sophie_configural_featural_2020_Oct_30_1935.csv')
outputData3  = pd.read_csv('./ConfFeatData/mb_configural_featural_2020-10-27_19h53.55.535.csv')
outputData4  = pd.read_csv('./ConfFeatData/AL_configural_featural_2020-11-06_04h28.09.977.csv')
outputData5  = pd.read_csv('./ConfFeatData/DP_configural_featural_2020-11-16_09h33.10.896.csv')
outputData6  = pd.read_csv('./ConfFeatData/MG_configural_featural_2020-11-15_22h32.34.325.csv')
outputData7  = pd.read_csv('./ConfFeatData/nb_configural_featural_2020-11-20_14h08.02.638.csv')
outputData8  = pd.read_csv('./ConfFeatData/RH_configural_featural_2020-11-24_15h44.30.118.csv')
outputData9  = pd.read_csv('./ConfFeatData/HK_configural_featural_2020-11-29_11h00.22.904.csv')
outputData10 = pd.read_csv('./ConfFeatData/LK_configural_featural_2020-11-29_14h31.10.160.csv')

# first need to fill in block type for each row
startRow = 12
trialsPerBlock = 48
outputData.loc[startRow:trialsPerBlock+startRow, 'Block_type'] = outputData.loc[trialsPerBlock+startRow, 'Block_type']
outputData.loc[trialsPerBlock+1+startRow:trialsPerBlock*2+1+startRow, 'Block_type'] = outputData.loc[trialsPerBlock*2+1+startRow, 'Block_type']
outputData.loc[trialsPerBlock*2+2+startRow:trialsPerBlock*3+2+startRow, 'Block_type'] = outputData.loc[trialsPerBlock*3+2+startRow, 'Block_type']
outputData.loc[trialsPerBlock*3+3+startRow:trialsPerBlock*4+3+startRow, 'Block_type'] = outputData.loc[trialsPerBlock*4+3+startRow, 'Block_type']

startRow = 15
trialsPerBlock = 48
outputData2.loc[startRow:trialsPerBlock+startRow, 'Block_type'] = outputData2.loc[trialsPerBlock+startRow, 'Block_type']
outputData2.loc[trialsPerBlock+1+startRow:trialsPerBlock*2+1+startRow, 'Block_type'] = outputData2.loc[trialsPerBlock*2+1+startRow, 'Block_type']
outputData2.loc[trialsPerBlock*2+2+startRow:trialsPerBlock*3+2+startRow, 'Block_type'] = outputData2.loc[trialsPerBlock*3+2+startRow, 'Block_type']
outputData2.loc[trialsPerBlock*3+3+startRow:trialsPerBlock*4+3+startRow, 'Block_type'] = outputData2.loc[trialsPerBlock*4+3+startRow, 'Block_type']


startRow = 0
trialsPerBlock = 48
outputData3.loc[startRow:trialsPerBlock+startRow, 'Block_type'] = outputData3.loc[trialsPerBlock+startRow, 'Block_type']
outputData3.loc[trialsPerBlock+1+startRow:trialsPerBlock*2+1+startRow, 'Block_type'] = outputData3.loc[trialsPerBlock*2+1+startRow, 'Block_type']
outputData3.loc[trialsPerBlock*2+2+startRow:trialsPerBlock*3+2+startRow, 'Block_type'] = outputData3.loc[trialsPerBlock*3+2+startRow, 'Block_type']
outputData3.loc[trialsPerBlock*3+3+startRow:trialsPerBlock*4+3+startRow, 'Block_type'] = outputData3.loc[trialsPerBlock*4+3+startRow, 'Block_type']

startRow = 12
trialsPerBlock = 48
outputData4.loc[startRow:trialsPerBlock+startRow, 'Block_type'] = outputData4.loc[trialsPerBlock+startRow, 'Block_type']
outputData4.loc[trialsPerBlock+1+startRow:trialsPerBlock*2+1+startRow, 'Block_type'] = outputData4.loc[trialsPerBlock*2+1+startRow, 'Block_type']
outputData4.loc[trialsPerBlock*2+2+startRow:trialsPerBlock*3+2+startRow, 'Block_type'] = outputData4.loc[trialsPerBlock*3+2+startRow, 'Block_type']
outputData4.loc[trialsPerBlock*3+3+startRow:trialsPerBlock*4+3+startRow, 'Block_type'] = outputData4.loc[trialsPerBlock*4+3+startRow, 'Block_type']
outputData4.loc[trialsPerBlock*4+4+startRow:trialsPerBlock*5+4+startRow, 'Block_type'] = outputData4.loc[trialsPerBlock*5+4+startRow, 'Block_type']
outputData4.loc[trialsPerBlock*5+5+startRow:trialsPerBlock*6+5+startRow, 'Block_type'] = outputData4.loc[trialsPerBlock*6+5+startRow, 'Block_type']
outputData4.loc[trialsPerBlock*6+6+startRow:trialsPerBlock*7+6+startRow, 'Block_type'] = outputData4.loc[trialsPerBlock*7+6+startRow, 'Block_type']
outputData4.loc[trialsPerBlock*7+7+startRow:trialsPerBlock*8+7+startRow, 'Block_type'] = outputData4.loc[trialsPerBlock*8+7+startRow, 'Block_type']

startRow = 12
trialsPerBlock = 48
outputData5.loc[startRow:trialsPerBlock+startRow, 'Block_type'] = outputData5.loc[trialsPerBlock+startRow, 'Block_type']
outputData5.loc[trialsPerBlock+1+startRow:trialsPerBlock*2+1+startRow, 'Block_type'] = outputData5.loc[trialsPerBlock*2+1+startRow, 'Block_type']
outputData5.loc[trialsPerBlock*2+2+startRow:trialsPerBlock*3+2+startRow, 'Block_type'] = outputData5.loc[trialsPerBlock*3+2+startRow, 'Block_type']
outputData5.loc[trialsPerBlock*3+3+startRow:trialsPerBlock*4+3+startRow, 'Block_type'] = outputData5.loc[trialsPerBlock*4+3+startRow, 'Block_type']
outputData5.loc[trialsPerBlock*4+4+startRow:trialsPerBlock*5+4+startRow, 'Block_type'] = outputData5.loc[trialsPerBlock*5+4+startRow, 'Block_type']
outputData5.loc[trialsPerBlock*5+5+startRow:trialsPerBlock*6+5+startRow, 'Block_type'] = outputData5.loc[trialsPerBlock*6+5+startRow, 'Block_type']
outputData5.loc[trialsPerBlock*6+6+startRow:trialsPerBlock*7+6+startRow, 'Block_type'] = outputData5.loc[trialsPerBlock*7+6+startRow, 'Block_type']
outputData5.loc[trialsPerBlock*7+7+startRow:trialsPerBlock*8+7+startRow, 'Block_type'] = outputData5.loc[trialsPerBlock*8+7+startRow, 'Block_type']

startRow = 12
trialsPerBlock = 48
outputData6.loc[startRow:trialsPerBlock+startRow, 'Block_type'] = outputData6.loc[trialsPerBlock+startRow, 'Block_type']
outputData6.loc[trialsPerBlock+1+startRow:trialsPerBlock*2+1+startRow, 'Block_type'] = outputData6.loc[trialsPerBlock*2+1+startRow, 'Block_type']
outputData6.loc[trialsPerBlock*2+2+startRow:trialsPerBlock*3+2+startRow, 'Block_type'] = outputData6.loc[trialsPerBlock*3+2+startRow, 'Block_type']
outputData6.loc[trialsPerBlock*3+3+startRow:trialsPerBlock*4+3+startRow, 'Block_type'] = outputData6.loc[trialsPerBlock*4+3+startRow, 'Block_type']
outputData6.loc[trialsPerBlock*4+4+startRow:trialsPerBlock*5+4+startRow, 'Block_type'] = outputData6.loc[trialsPerBlock*5+4+startRow, 'Block_type']
outputData6.loc[trialsPerBlock*5+5+startRow:trialsPerBlock*6+5+startRow, 'Block_type'] = outputData6.loc[trialsPerBlock*6+5+startRow, 'Block_type']
outputData6.loc[trialsPerBlock*6+6+startRow:trialsPerBlock*7+6+startRow, 'Block_type'] = outputData6.loc[trialsPerBlock*7+6+startRow, 'Block_type']
outputData6.loc[trialsPerBlock*7+7+startRow:trialsPerBlock*8+7+startRow, 'Block_type'] = outputData6.loc[trialsPerBlock*8+7+startRow, 'Block_type']

startRow = 18
trialsPerBlock = 24
outputData7.loc[startRow:trialsPerBlock+startRow, 'Block_type'] = outputData7.loc[trialsPerBlock+startRow, 'Block_type']
outputData7.loc[trialsPerBlock+1+startRow:trialsPerBlock*2+1+startRow, 'Block_type'] = outputData7.loc[trialsPerBlock*2+1+startRow, 'Block_type']
outputData7.loc[trialsPerBlock*2+2+startRow:trialsPerBlock*3+2+startRow, 'Block_type'] = outputData7.loc[trialsPerBlock*3+2+startRow, 'Block_type']
outputData7.loc[trialsPerBlock*3+3+startRow:trialsPerBlock*4+3+startRow, 'Block_type'] = outputData7.loc[trialsPerBlock*4+3+startRow, 'Block_type']
outputData7.loc[trialsPerBlock*4+4+startRow:trialsPerBlock*5+4+startRow, 'Block_type'] = outputData7.loc[trialsPerBlock*5+4+startRow, 'Block_type']
outputData7.loc[trialsPerBlock*5+5+startRow:trialsPerBlock*6+5+startRow, 'Block_type'] = outputData7.loc[trialsPerBlock*6+5+startRow, 'Block_type']
outputData7.loc[trialsPerBlock*6+6+startRow:trialsPerBlock*7+6+startRow, 'Block_type'] = outputData7.loc[trialsPerBlock*7+6+startRow, 'Block_type']
outputData7.loc[trialsPerBlock*7+7+startRow:trialsPerBlock*8+7+startRow, 'Block_type'] = outputData7.loc[trialsPerBlock*8+7+startRow, 'Block_type']

startRow = 18
trialsPerBlock = 24
outputData8.loc[startRow:trialsPerBlock+startRow, 'Block_type'] = outputData8.loc[trialsPerBlock+startRow, 'Block_type']
outputData8.loc[trialsPerBlock+1+startRow:trialsPerBlock*2+1+startRow, 'Block_type'] = outputData8.loc[trialsPerBlock*2+1+startRow, 'Block_type']
outputData8.loc[trialsPerBlock*2+2+startRow:trialsPerBlock*3+2+startRow, 'Block_type'] = outputData8.loc[trialsPerBlock*3+2+startRow, 'Block_type']
outputData8.loc[trialsPerBlock*3+3+startRow:trialsPerBlock*4+3+startRow, 'Block_type'] = outputData8.loc[trialsPerBlock*4+3+startRow, 'Block_type']
outputData8.loc[trialsPerBlock*4+4+startRow:trialsPerBlock*5+4+startRow, 'Block_type'] = outputData8.loc[trialsPerBlock*5+4+startRow, 'Block_type']
outputData8.loc[trialsPerBlock*5+5+startRow:trialsPerBlock*6+5+startRow, 'Block_type'] = outputData8.loc[trialsPerBlock*6+5+startRow, 'Block_type']
outputData8.loc[trialsPerBlock*6+6+startRow:trialsPerBlock*7+6+startRow, 'Block_type'] = outputData8.loc[trialsPerBlock*7+6+startRow, 'Block_type']
outputData8.loc[trialsPerBlock*7+7+startRow:trialsPerBlock*8+7+startRow, 'Block_type'] = outputData8.loc[trialsPerBlock*8+7+startRow, 'Block_type']

respData = outputData.loc[:, ['Block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
respData = respData.dropna()

conf_haus = respData.loc[respData['Block_type'].str.contains('conf_haus'), :]
conf_face = respData.loc[respData['Block_type'].str.contains('conf_face'), :]
feat_haus = respData.loc[respData['Block_type'].str.contains('feat_haus'), :]
feat_face = respData.loc[respData['Block_type'].str.contains('feat_face'), :]

respData2 = outputData2.loc[:, ['Block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
respData2 = respData2.dropna()

conf_haus2 = respData2.loc[respData2['Block_type'].str.contains('conf_haus'), :]
conf_face2 = respData2.loc[respData2['Block_type'].str.contains('conf_face'), :]
feat_haus2 = respData2.loc[respData2['Block_type'].str.contains('feat_haus'), :]
feat_face2 = respData2.loc[respData2['Block_type'].str.contains('feat_face'), :]

respData3 = outputData3.loc[:, ['Block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
respData3 = respData3.dropna()

conf_haus3 = respData3.loc[respData3['Block_type'].str.contains('conf_haus'), :]
conf_face3 = respData3.loc[respData3['Block_type'].str.contains('conf_face'), :]
feat_haus3 = respData3.loc[respData3['Block_type'].str.contains('feat_haus'), :]
feat_face3 = respData3.loc[respData3['Block_type'].str.contains('feat_face'), :]

respData4 = outputData4.loc[:, ['Block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
respData4 = respData4.dropna()


conf_haus4L = respData4.loc[(respData4['Block_type'].str.contains('conf_haus') & (respData4['side'] > 0)), :]
conf_face4L = respData4.loc[(respData4['Block_type'].str.contains('conf_face') & (respData4['side'] > 0)), :]
feat_haus4L = respData4.loc[(respData4['Block_type'].str.contains('feat_haus') & (respData4['side'] > 0)), :]
feat_face4L = respData4.loc[(respData4['Block_type'].str.contains('feat_face') & (respData4['side'] > 0)), :]
conf_haus4R = respData4.loc[(respData4['Block_type'].str.contains('conf_haus') & (respData4['side'] < 0)), :]
conf_face4R = respData4.loc[(respData4['Block_type'].str.contains('conf_face') & (respData4['side'] < 0)), :]
feat_haus4R = respData4.loc[(respData4['Block_type'].str.contains('feat_haus') & (respData4['side'] < 0)), :]
feat_face4R = respData4.loc[(respData4['Block_type'].str.contains('feat_face') & (respData4['side'] < 0)), :]

respData5 = outputData5.loc[:, ['Block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
respData5 = respData5.dropna()

conf_haus5L = respData5.loc[(respData5['Block_type'].str.contains('conf_haus') & (respData5['side'] > 0)), :]
conf_face5L = respData5.loc[(respData5['Block_type'].str.contains('conf_face') & (respData5['side'] > 0)), :]
feat_haus5L = respData5.loc[(respData5['Block_type'].str.contains('feat_haus') & (respData5['side'] > 0)), :]
feat_face5L = respData5.loc[(respData5['Block_type'].str.contains('feat_face') & (respData5['side'] > 0)), :]
conf_haus5R = respData5.loc[(respData5['Block_type'].str.contains('conf_haus') & (respData5['side'] < 0)), :]
conf_face5R = respData5.loc[(respData5['Block_type'].str.contains('conf_face') & (respData5['side'] < 0)), :]
feat_haus5R = respData5.loc[(respData5['Block_type'].str.contains('feat_haus') & (respData5['side'] < 0)), :]
feat_face5R = respData5.loc[(respData5['Block_type'].str.contains('feat_face') & (respData5['side'] < 0)), :]

# respData6 = outputData6.loc[:, ['Block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
# respData6 = respData6.dropna()
#
# conf_haus6L = respData6.loc[(respData6['Block_type'].str.contains('conf_haus') & (respData6['side'] > 0)), :]
# conf_face6L = respData6.loc[(respData6['Block_type'].str.contains('conf_face') & (respData6['side'] > 0)), :]
# feat_haus6L = respData6.loc[(respData6['Block_type'].str.contains('feat_haus') & (respData6['side'] > 0)), :]
# feat_face6L = respData6.loc[(respData6['Block_type'].str.contains('feat_face') & (respData6['side'] > 0)), :]
# conf_haus6R = respData6.loc[(respData6['Block_type'].str.contains('conf_haus') & (respData6['side'] < 0)), :]
# conf_face6R = respData6.loc[(respData6['Block_type'].str.contains('conf_face') & (respData6['side'] < 0)), :]
# feat_haus6R = respData6.loc[(respData6['Block_type'].str.contains('feat_haus') & (respData6['side'] < 0)), :]
# feat_face6R = respData6.loc[(respData6['Block_type'].str.contains('feat_face') & (respData6['side'] < 0)), :]

respData7 = outputData7.loc[:, ['Block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
respData7 = respData7.dropna()

conf_haus7 = respData7.loc[respData7['Block_type'].str.contains('conf_haus'), :]
conf_face7 = respData7.loc[respData7['Block_type'].str.contains('conf_face'), :]
feat_haus7 = respData7.loc[respData7['Block_type'].str.contains('feat_haus'), :]
feat_face7 = respData7.loc[respData7['Block_type'].str.contains('feat_face'), :]

respData8 = outputData8.loc[:, ['Block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
respData8 = respData8.dropna()

conf_haus8 = respData8.loc[respData8['Block_type'].str.contains('conf_haus'), :]
conf_face8 = respData8.loc[respData8['Block_type'].str.contains('conf_face'), :]
feat_haus8 = respData8.loc[respData8['Block_type'].str.contains('feat_haus'), :]
feat_face8 = respData8.loc[respData8['Block_type'].str.contains('feat_face'), :]

respData9 = outputData9.loc[:, ['block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
respData9 = respData9.dropna()

conf_haus9 = respData9.loc[respData9['block_type'].str.contains('conf_haus'), :]
conf_face9 = respData9.loc[respData9['block_type'].str.contains('conf_face'), :]
feat_haus9 = respData9.loc[respData9['block_type'].str.contains('feat_haus'), :]
feat_face9 = respData9.loc[respData9['block_type'].str.contains('feat_face'), :]

respData10 = outputData10.loc[:, ['block_type', 'trial_type1S0D', 'side', 'key_resp.corr', 'key_resp.rt', 'key_resp.keys']]
respData10 = respData10.dropna()

conf_haus10 = respData10.loc[respData10['block_type'].str.contains('conf_haus'), :]
conf_face10 = respData10.loc[respData10['block_type'].str.contains('conf_face'), :]
feat_haus10 = respData10.loc[respData10['block_type'].str.contains('feat_haus'), :]
feat_face10 = respData10.loc[respData10['block_type'].str.contains('feat_face'), :]



conditions = [conf_haus4L, conf_face4L, feat_haus4L, feat_face4L,
              conf_haus5L, conf_face5L, feat_haus5L, feat_face5L,
              conf_haus4R, conf_face4R, feat_haus4R, feat_face4R,
              conf_haus5R, conf_face5R, feat_haus5R, feat_face5R,
              conf_haus7, conf_face7, feat_haus7, feat_face7,
              conf_haus8, conf_face8, feat_haus8, feat_face8,
              conf_haus9, conf_face9, feat_haus9, feat_face9,
              conf_haus10, conf_face10, feat_haus10, feat_face10]

# conf_haus6L, conf_face6L, feat_haus6L, feat_face6L, conf_haus6R, conf_face6R, feat_haus6R, feat_face6R,

# for iCond in conditions:
#     corr_resps = []
#     for iRow in range(0, len(iCond)):
#         if iCond['trial_type1S0D'].iloc[iRow] == 1:
#             corr_resps.append(int(iCond['key_resp.keys'].iloc[iRow] == 'f'))
#         elif iCond['trial_type1S0D'].iloc[iRow] == 0:
#             corr_resps.append(int(iCond['key_resp.keys'].iloc[iRow] == 'j'))
#         else:
#             print('Error: not same or different?')



z_hit1 = []
z_fal1 = []
z_hit2 = []
z_fal2 = []
for iCond in conditions:
    iCond = conf_haus10
    hits1 = [] # hits = same trial, same button
    hits2 = [] # hits = diff trial, diff button
    false_alarms1 = [] # false alarm, diff trial, same button
    false_alarms2 = [] # false alarm, same trial, diff button
    hits1.append(len(iCond[(iCond['trial_type1S0D'] == 1) & (iCond['key_resp.corr'] == 1)])/len(iCond[(iCond['trial_type1S0D'] == 1)]))
    hits2.append(len(iCond[(iCond['trial_type1S0D'] == 0) & (iCond['key_resp.corr'] == 1)])/len(iCond[(iCond['trial_type1S0D'] == 1)]))
    false_alarms1.append(len(iCond[(iCond['trial_type1S0D'] == 0) & (iCond['key_resp.corr'] == 0)])/len(iCond[(iCond['trial_type1S0D'] == 1)]))
    false_alarms2.append(len(iCond[(iCond['trial_type1S0D'] == 1) & (iCond['key_resp.corr'] == 0)])/len(iCond[(iCond['trial_type1S0D'] == 1)]))
    z_hit1.append(norm.ppf(np.sum(hits1), loc=0, scale=1))
    z_hit2.append(norm.ppf(np.sum(hits2), loc=0, scale=1))
    z_fal1.append(norm.ppf(np.sum(false_alarms1), loc=0, scale=1))
    z_fal2.append(norm.ppf(np.sum(false_alarms2), loc=0, scale=1))

d_primes1 = np.array(z_hit1) - np.array(z_fal1)
d_primes2 = np.array(z_hit2) - np.array(z_fal2)

cond_d_primes = [d_primes1[[0, 4]].mean(),
                 d_primes1[[8, 12]].mean(),
                 d_primes1[16],
                 d_primes1[20],
                 d_primes1[24],
                 d_primes1[28],
                 d_primes1[[1, 5]].mean(),
                 d_primes1[[9, 13]].mean(),
                 d_primes1[17],
                 d_primes1[21],
                 d_primes1[25],
                 d_primes1[29],
                 d_primes1[[2, 6]].mean(),
                 d_primes1[[10, 14]].mean(),
                 d_primes1[18],
                 d_primes1[22],
                 d_primes1[26],
                 d_primes1[30],
                 d_primes1[[3, 7]].mean(),
                 d_primes1[[11, 15]].mean(),
                 d_primes1[19],
                 d_primes1[23],
                 d_primes1[27],
                 d_primes1[31]]

# cond_d_primes = [d_primes1[[0, 4, 8]].mean(),
#                  d_primes1[[12, 16, 20]].mean(),
#                  d_primes1[24],
#                  d_primes1[28],
#                  d_primes1[[1, 5, 9]].mean(),
#                  d_primes1[[13, 17, 21]].mean(),
#                  d_primes1[25],
#                  d_primes1[29],
#                  d_primes1[[2, 6, 10]].mean(),
#                  d_primes1[[14, 18, 22]].mean(),
#                  d_primes1[26],
#                  d_primes1[30],
#                  d_primes1[[3, 7, 11]].mean(),
#                  d_primes1[[15, 19, 23]].mean(),
#                  d_primes1[27],
#                  d_primes1[31]]

# cond_d_primes_stds = [d_primes1[[0, 4, 8]].std()/np.sqrt(3),
#                       d_primes1[[12, 16, 20]].std()/np.sqrt(3),
#                       0,
#                       0,
#                       d_primes1[[1, 5, 9]].std()/np.sqrt(3),
#                       d_primes1[[13, 17, 21]].std()/np.sqrt(3),
#                       0,
#                       0,
#                       d_primes1[[2, 6, 10]].std()/np.sqrt(3),
#                       d_primes1[[14, 18, 22]].std()/np.sqrt(3),
#                       0,
#                       0,
#                       d_primes1[[3, 7, 11]].std()/np.sqrt(3),
#                       d_primes1[[15, 19, 23]].std()/np.sqrt(3),
#                       0,
#                       0]

cond_d_primes_stds = [d_primes1[[0, 4]].std()/np.sqrt(2),
                      d_primes1[[8, 12]].std()/np.sqrt(2),
                      0, 0,
                      0, 0,
                      d_primes1[[1, 5]].std()/np.sqrt(2),
                      d_primes1[[9, 13]].std()/np.sqrt(2),
                      0, 0,
                      0, 0,
                      d_primes1[[2, 6]].std()/np.sqrt(2),
                      d_primes1[[10, 14]].std()/np.sqrt(2),
                      0, 0,
                      0, 0,
                      d_primes1[[3, 7]].std()/np.sqrt(2),
                      d_primes1[[11, 15]].std()/np.sqrt(2),
                      0, 0,
                      0, 0]


cond_accuracy_conf_haus_meansL = [np.array(conf_haus4L['key_resp.corr']).mean(),
                                 np.array(conf_haus5L['key_resp.corr']).mean()]
                                 # np.array(conf_haus6L['key_resp.corr']).mean()]
cond_accuracy_conf_haus_meansL = [np.array(conf_haus4L['key_resp.corr']).mean(),
                                 np.array(conf_haus5L['key_resp.corr']).mean()]
                                 # np.array(conf_haus6L['key_resp.corr']).mean()]
cond_accuracy_conf_haus_meanL = np.array(cond_accuracy_conf_haus_meansL).mean()
cond_accuracy_conf_haus_stdL = np.array(cond_accuracy_conf_haus_meansL).std()/np.sqrt(2)
cond_accuracy_conf_haus_meansR = [np.array(conf_haus4R['key_resp.corr']).mean(),
                                 np.array(conf_haus5R['key_resp.corr']).mean()]
                                 # np.array(conf_haus6R['key_resp.corr']).mean()]
cond_accuracy_conf_haus_meansR = [np.array(conf_haus4R['key_resp.corr']).mean(),
                                 np.array(conf_haus5R['key_resp.corr']).mean()]
                                 # np.array(conf_haus6R['key_resp.corr']).mean()]
cond_accuracy_conf_haus_meanR = np.array(cond_accuracy_conf_haus_meansR).mean()
cond_accuracy_conf_haus_stdR = np.array(cond_accuracy_conf_haus_meansR).std()/np.sqrt(2)

cond_accuracy_conf_face_meansL = [np.array(conf_face4L['key_resp.corr']).mean(),
                                 np.array(conf_face5L['key_resp.corr']).mean()]
                                 # np.array(conf_face6L['key_resp.corr']).mean()]
cond_accuracy_conf_face_meanL = np.array(cond_accuracy_conf_face_meansL).mean()
cond_accuracy_conf_face_stdL = np.array(cond_accuracy_conf_face_meansL).std()/np.sqrt(2)
cond_accuracy_conf_face_meansR = [np.array(conf_face4R['key_resp.corr']).mean(),
                                 np.array(conf_face5R['key_resp.corr']).mean()]
                                 # np.array(conf_face6R['key_resp.corr']).mean()]
cond_accuracy_conf_face_meanR = np.array(cond_accuracy_conf_face_meansR).mean()
cond_accuracy_conf_face_stdR = np.array(cond_accuracy_conf_face_meansR).std()/np.sqrt(2)

cond_accuracy_feat_haus_meansL = [np.array(feat_haus4L['key_resp.corr']).mean(),
                                 np.array(feat_haus5L['key_resp.corr']).mean()]
                                 # np.array(feat_haus6L['key_resp.corr']).mean()]
cond_accuracy_feat_haus_meanL = np.array(cond_accuracy_feat_haus_meansL).mean()
cond_accuracy_feat_haus_stdL = np.array(cond_accuracy_feat_haus_meansL).std()/np.sqrt(2)
cond_accuracy_feat_haus_meansR = [np.array(feat_haus4R['key_resp.corr']).mean(),
                                 np.array(feat_haus5R['key_resp.corr']).mean()]
                                 # np.array(feat_haus6R['key_resp.corr']).mean()]
cond_accuracy_feat_haus_meanR = np.array(cond_accuracy_feat_haus_meansR).mean()
cond_accuracy_feat_haus_stdR = np.array(cond_accuracy_feat_haus_meansR).std()/np.sqrt(2)

cond_accuracy_feat_face_meansL = [np.array(feat_face4L['key_resp.corr']).mean(),
                                 np.array(feat_face5L['key_resp.corr']).mean()]
                                 # np.array(feat_face6L['key_resp.corr']).mean()]
cond_accuracy_feat_face_meanL = np.array(cond_accuracy_feat_face_meansL).mean()
cond_accuracy_feat_face_stdL = np.array(cond_accuracy_feat_face_meansL).std()/np.sqrt(2)
cond_accuracy_feat_face_meansR = [np.array(feat_face4R['key_resp.corr']).mean(),
                                 np.array(feat_face5R['key_resp.corr']).mean()]
                                 # np.array(feat_face6R['key_resp.corr']).mean()]
cond_accuracy_feat_face_meanR = np.array(cond_accuracy_feat_face_meansR).mean()
cond_accuracy_feat_face_stdR = np.array(cond_accuracy_feat_face_meansR).std()/np.sqrt(2)

cond_accuracy_means = [cond_accuracy_conf_haus_meanL, cond_accuracy_conf_haus_meanR, conf_haus7['key_resp.corr'].mean(), conf_haus8['key_resp.corr'].mean(), conf_haus9['key_resp.corr'].mean(), conf_haus10['key_resp.corr'].mean(),
                       cond_accuracy_conf_face_meanL, cond_accuracy_conf_face_meanR, conf_face7['key_resp.corr'].mean(), conf_face8['key_resp.corr'].mean(), conf_face9['key_resp.corr'].mean(), conf_face10['key_resp.corr'].mean(),
                       cond_accuracy_feat_haus_meanL, cond_accuracy_feat_haus_meanR, feat_haus7['key_resp.corr'].mean(), feat_haus8['key_resp.corr'].mean(), feat_haus9['key_resp.corr'].mean(), feat_haus10['key_resp.corr'].mean(),
                       cond_accuracy_feat_face_meanL, cond_accuracy_feat_face_meanR, feat_face7['key_resp.corr'].mean(), feat_face8['key_resp.corr'].mean(), feat_face9['key_resp.corr'].mean(), feat_face10['key_resp.corr'].mean()]
cond_accuracy_stds = [cond_accuracy_conf_haus_stdL, cond_accuracy_conf_haus_stdR, 0, 0, 0, 0,
                      cond_accuracy_conf_face_stdL, cond_accuracy_conf_face_stdR, 0, 0, 0, 0,
                      cond_accuracy_feat_haus_stdL, cond_accuracy_feat_haus_stdR, 0, 0, 0, 0,
                      cond_accuracy_feat_face_stdL, cond_accuracy_feat_face_stdR, 0, 0, 0, 0]

cond_RT_conf_haus_meansL = [np.array(conf_haus4L['key_resp.rt']).mean(),
                           np.array(conf_haus5L['key_resp.rt']).mean()]
                           # np.array(conf_haus6L['key_resp.rt']).mean()]
cond_RT_conf_haus_meansR = [np.array(conf_haus4R['key_resp.rt']).mean(),
                           np.array(conf_haus5R['key_resp.rt']).mean()]
                           # np.array(conf_haus6R['key_resp.rt']).mean()]
cond_RT_conf_haus_meanL = np.array(cond_accuracy_conf_haus_meansL).mean()
cond_RT_conf_haus_stdL = np.array(cond_accuracy_conf_haus_meansL).std()/np.sqrt(2)
cond_RT_conf_haus_meanR = np.array(cond_accuracy_conf_haus_meansR).mean()
cond_RT_conf_haus_stdR = np.array(cond_accuracy_conf_haus_meansR).std()/np.sqrt(2)

cond_RT_conf_face_meansL = [np.array(conf_face4L['key_resp.rt']).mean(),
                           np.array(conf_face5L['key_resp.rt']).mean()]
                           # np.array(conf_face6L['key_resp.rt']).mean()]
cond_RT_conf_face_meansR = [np.array(conf_face4R['key_resp.rt']).mean(),
                           np.array(conf_face5R['key_resp.rt']).mean()]
                           # np.array(conf_face6R['key_resp.rt']).mean()]
cond_RT_conf_face_meanL = np.array(cond_RT_conf_face_meansL).mean()
cond_RT_conf_face_stdL = np.array(cond_RT_conf_face_meansL).std()/np.sqrt(2)
cond_RT_conf_face_meanR = np.array(cond_RT_conf_face_meansR).mean()
cond_RT_conf_face_stdR = np.array(cond_RT_conf_face_meansR).std()/np.sqrt(2)

cond_RT_feat_haus_meansL = [np.array(feat_haus4L['key_resp.rt']).mean(),
                           np.array(feat_haus5L['key_resp.rt']).mean()]
                           # np.array(feat_haus6L['key_resp.rt']).mean()]
cond_RT_feat_haus_meansR = [np.array(feat_haus4R['key_resp.rt']).mean(),
                           np.array(feat_haus5R['key_resp.rt']).mean()]
                           # np.array(feat_haus6R['key_resp.rt']).mean()]
cond_RT_feat_haus_meanL = np.array(cond_RT_feat_haus_meansL).mean()
cond_RT_feat_haus_stdL = np.array(cond_RT_feat_haus_meansL).std()/np.sqrt(2)
cond_RT_feat_haus_meanR = np.array(cond_RT_feat_haus_meansR).mean()
cond_RT_feat_haus_stdR = np.array(cond_RT_feat_haus_meansR).std()/np.sqrt(2)

cond_RT_feat_face_meansL = [np.array(feat_face4L['key_resp.rt']).mean(),
                           np.array(feat_face5L['key_resp.rt']).mean(),]
                           # np.array(feat_face6L['key_resp.rt']).mean()]
cond_RT_feat_face_meansR = [np.array(feat_face4R['key_resp.rt']).mean(),
                           np.array(feat_face5R['key_resp.rt']).mean()]
                           # np.array(feat_face6R['key_resp.rt']).mean()]
cond_RT_feat_face_meanL = np.array(cond_accuracy_feat_face_meansL).mean()
cond_RT_feat_face_stdL = np.array(cond_accuracy_feat_face_meansL).std()/np.sqrt(2)
cond_RT_feat_face_meanR = np.array(cond_accuracy_feat_face_meansR).mean()
cond_RT_feat_face_stdR = np.array(cond_accuracy_feat_face_meansR).std()/np.sqrt(2)

cond_RT_means = [cond_RT_conf_haus_meanL, cond_RT_conf_haus_meanR, conf_haus7['key_resp.rt'].mean(), conf_haus8['key_resp.rt'].mean(), conf_haus9['key_resp.rt'].mean(), conf_haus10['key_resp.rt'].mean(),
                 cond_RT_conf_face_meanL, cond_RT_conf_face_meanR, conf_face7['key_resp.rt'].mean(), conf_face8['key_resp.rt'].mean(), conf_face9['key_resp.rt'].mean(), conf_face10['key_resp.rt'].mean(),
                 cond_RT_feat_haus_meanL, cond_RT_feat_haus_meanR, feat_haus7['key_resp.rt'].mean(), feat_haus8['key_resp.rt'].mean(), feat_haus9['key_resp.rt'].mean(), feat_haus10['key_resp.rt'].mean(),
                 cond_RT_feat_face_meanL, cond_RT_feat_face_meanR, feat_face7['key_resp.rt'].mean(), feat_face8['key_resp.rt'].mean(), feat_face9['key_resp.rt'].mean(), feat_face10['key_resp.rt'].mean()]
cond_RT_stds = [cond_RT_conf_haus_stdL, cond_RT_conf_haus_stdR, 0, 0, 0, 0,
                cond_RT_conf_face_stdL, cond_RT_conf_face_stdR, 0, 0, 0, 0,
                cond_RT_feat_haus_stdL, cond_RT_feat_haus_stdR, 0, 0, 0, 0,
                cond_RT_feat_face_stdL, cond_RT_feat_face_stdR, 0, 0, 0, 0]

cond_IE_conf_haus_meansL = [np.array(conf_haus4L['key_resp.rt']).mean()/(1 - np.array(conf_haus4L['key_resp.corr']).mean()),
                           np.array(conf_haus5L['key_resp.rt']).mean()/(1 - np.array(conf_haus5L['key_resp.corr']).mean())]
                           # np.array(conf_haus6L['key_resp.rt']).mean()/(1 - np.array(conf_haus6L['key_resp.corr']).mean())]
cond_IE_conf_haus_meansR = [np.array(conf_haus4R['key_resp.rt']).mean()/(1 - np.array(conf_haus4R['key_resp.corr']).mean()),
                           np.array(conf_haus5R['key_resp.rt']).mean()/(1 - np.array(conf_haus5R['key_resp.corr']).mean())]
                           # np.array(conf_haus6R['key_resp.rt']).mean()/(1 - np.array(conf_haus6R['key_resp.corr']).mean())]
cond_IE_conf_haus_meanL = np.array(cond_IE_conf_haus_meansL).mean()
cond_IE_conf_haus_stdL = np.array(cond_IE_conf_haus_meansL).std()/np.sqrt(2)
cond_IE_conf_haus_meanR = np.array(cond_IE_conf_haus_meansR).mean()
cond_IE_conf_haus_stdR = np.array(cond_IE_conf_haus_meansR).std()/np.sqrt(2)

cond_IE_conf_face_meansL = [np.array(conf_face4L['key_resp.rt']).mean()/(1 - np.array(conf_face4L['key_resp.corr']).mean()),
                           np.array(conf_face5L['key_resp.rt']).mean()/(1 - np.array(conf_face5L['key_resp.corr']).mean())]
                           # np.array(conf_face6L['key_resp.rt']).mean()/(1 - np.array(conf_face6L['key_resp.corr']).mean())]
cond_IE_conf_face_meansR = [np.array(conf_face4R['key_resp.rt']).mean()/(1 - np.array(conf_face4R['key_resp.corr']).mean()),
                           np.array(conf_face5R['key_resp.rt']).mean()/(1 - np.array(conf_face5R['key_resp.corr']).mean())]
                           # np.array(conf_face6R['key_resp.rt']).mean()/(1 - np.array(conf_face6R['key_resp.corr']).mean())]
cond_IE_conf_face_meanL = np.array(cond_IE_conf_face_meansL).mean()
cond_IE_conf_face_stdL = np.array(cond_IE_conf_face_meansL).std()/np.sqrt(2)
cond_IE_conf_face_meanR = np.array(cond_IE_conf_face_meansR).mean()
cond_IE_conf_face_stdR = np.array(cond_IE_conf_face_meansR).std()/np.sqrt(2)

cond_IE_feat_haus_meansL = [np.array(feat_haus4L['key_resp.rt']).mean()/(1 - np.array(feat_haus4L['key_resp.corr']).mean()),
                           np.array(feat_haus5L['key_resp.rt']).mean()/(1 - np.array(feat_haus5L['key_resp.corr']).mean())]
                           # np.array(feat_haus6L['key_resp.rt']).mean()/(1 - np.array(feat_haus6L['key_resp.corr']).mean())]
cond_IE_feat_haus_meansR = [np.array(feat_haus4R['key_resp.rt']).mean()/(1 - np.array(feat_haus4R['key_resp.corr']).mean()),
                           np.array(feat_haus5R['key_resp.rt']).mean()/(1 - np.array(feat_haus5R['key_resp.corr']).mean())]
                           # np.array(feat_haus6R['key_resp.rt']).mean()/(1 - np.array(feat_haus6R['key_resp.corr']).mean())]
cond_IE_feat_haus_meanL = np.array(cond_IE_feat_haus_meansL).mean()
cond_IE_feat_haus_stdL = np.array(cond_IE_feat_haus_meansL).std()/np.sqrt(2)
cond_IE_feat_haus_meanR = np.array(cond_IE_feat_haus_meansR).mean()
cond_IE_feat_haus_stdR = np.array(cond_IE_feat_haus_meansR).std()/np.sqrt(2)

cond_IE_feat_face_meansL = [np.array(feat_face4L['key_resp.rt']).mean()/(1 - np.array(feat_face4L['key_resp.corr']).mean()),
                           np.array(feat_face5L['key_resp.rt']).mean()/(1 - np.array(feat_face5L['key_resp.corr']).mean())]
                           # np.array(feat_face6L['key_resp.rt']).mean()/(1 - np.array(feat_face6L['key_resp.corr']).mean())]
cond_IE_feat_face_meansR = [np.array(feat_face4R['key_resp.rt']).mean()/(1 - np.array(feat_face4R['key_resp.corr']).mean()),
                           np.array(feat_face5R['key_resp.rt']).mean()/(1 - np.array(feat_face5R['key_resp.corr']).mean())]
                           # np.array(feat_face6R['key_resp.rt']).mean()/(1 - np.array(feat_face6R['key_resp.corr']).mean())]
cond_IE_feat_face_meanL = np.array(cond_IE_feat_face_meansL).mean()
cond_IE_feat_face_stdL = np.array(cond_IE_feat_face_meansL).std()/np.sqrt(2)
cond_IE_feat_face_meanR = np.array(cond_IE_feat_face_meansR).mean()
cond_IE_feat_face_stdR = np.array(cond_IE_feat_face_meansR).std()/np.sqrt(2)

# RT by 1 – the proportion of Errors (PE)
cond_RevEff_means = [cond_IE_conf_haus_meanL, cond_IE_conf_haus_meanR, conf_haus7['key_resp.rt'].mean()/(1 - conf_haus7['key_resp.corr'].mean()), conf_haus8['key_resp.rt'].mean()/(1 - conf_haus8['key_resp.corr'].mean()), conf_haus9['key_resp.rt'].mean()/(1 - conf_haus9['key_resp.corr'].mean()), conf_haus10['key_resp.rt'].mean()/(1 - conf_haus10['key_resp.corr'].mean()),
                    cond_IE_conf_face_meanL, cond_IE_conf_face_meanR, conf_face7['key_resp.rt'].mean()/(1 - conf_face7['key_resp.corr'].mean()), conf_face8['key_resp.rt'].mean()/(1 - conf_face8['key_resp.corr'].mean()), conf_face9['key_resp.rt'].mean()/(1 - conf_face9['key_resp.corr'].mean()), conf_face10['key_resp.rt'].mean()/(1 - conf_face10['key_resp.corr'].mean()),
                    cond_IE_feat_haus_meanL, cond_IE_feat_haus_meanR, feat_haus7['key_resp.rt'].mean()/(1 - feat_haus7['key_resp.corr'].mean()), feat_haus8['key_resp.rt'].mean()/(1 - feat_haus8['key_resp.corr'].mean()), feat_haus9['key_resp.rt'].mean()/(1 - feat_haus9['key_resp.corr'].mean()), feat_haus10['key_resp.rt'].mean()/(1 - feat_haus10['key_resp.corr'].mean()),
                    cond_IE_feat_face_meanL, cond_IE_feat_face_meanR, feat_face7['key_resp.rt'].mean()/(1 - feat_face7['key_resp.corr'].mean()), feat_face8['key_resp.rt'].mean()/(1 - feat_face8['key_resp.corr'].mean()), feat_face9['key_resp.rt'].mean()/(1 - feat_face9['key_resp.corr'].mean()), feat_face10['key_resp.rt'].mean()/(1 - feat_face10['key_resp.corr'].mean())]
cond_RevEff_stds = [cond_IE_conf_haus_stdL, cond_IE_conf_haus_stdR, 0, 0, 0, 0,
                    cond_IE_conf_face_stdL, cond_IE_conf_face_stdR, 0, 0, 0, 0,
                    cond_IE_feat_haus_stdL, cond_IE_feat_haus_stdR, 0, 0, 0, 0,
                    cond_IE_feat_face_stdL, cond_IE_feat_face_stdR, 0, 0, 0, 0]

cond_names = ['cH_CL', 'cH_CR', 'cH_P1', 'cH_P2', 'cH_P3', 'cH_P4',
              'cF_CL', 'cF_CR', 'cF_P1', 'cF_P2', 'cF_P3', 'cF_P4',
              'fH_CL', 'fH_CR', 'fH_P1', 'fH_P2', 'fH_P3', 'fH_P4',
              'fF_CL', 'fF_CR', 'fF_P1', 'fF_P2', 'fF_P3', 'fF_P4']

colors = ['darkred','darkred','red','red','red','red','palevioletred','palevioletred','pink','pink','pink','pink','darkblue','darkblue','blue','blue','blue','blue','dodgerblue','dodgerblue','deepskyblue','deepskyblue','deepskyblue','deepskyblue']

plt.bar(cond_names,
        cond_RT_means,
        color=colors,
        yerr=cond_RT_stds)
plt.title('Average Configural/Featural Reaction Times')
plt.show()

plt.bar(['conf1', 'feat1', 'conf2', 'feat2', 'conf3', 'feat3', 'conf4', 'feat4'],
        cond_accuracy_means,
        color='grey')
plt.title('Average Configural/Featural Accuracy')
plt.show()

plt.bar(cond_names,
        cond_d_primes,
        color=colors,
        yerr=cond_d_primes_stds)
plt.title('D Primes')
plt.show()

plt.bar(cond_names,
        cond_accuracy_means,
        color=colors,
        yerr=cond_accuracy_stds)
plt.title('Average Configural/Featural Accuracy')
plt.plot([-0.5, 14.5], [0.5, 0.5], color='black', linestyle='--', linewidth=0.5)
plt.show()


plt.bar(cond_names,
        cond_RevEff_means,
        color=colors,
        yerr=cond_RevEff_stds)
plt.title('Inverse Efficiency Score')
plt.show()

avg_cond_accuracy_means = [np.array([cond_accuracy_conf_haus_mean,cond_accuracy_conf_face_mean]).mean(), np.array([cond_accuracy_feat_haus_mean,cond_accuracy_feat_face_mean]).mean()]
avg_cond_accuracy_stds = [np.array([cond_accuracy_conf_haus_std,cond_accuracy_conf_face_std]).mean(), np.array([cond_accuracy_feat_haus_std,cond_accuracy_feat_face_std]).mean()]

plt.bar(['conf', 'feat'],
        avg_cond_accuracy_means,
        color='grey',
        yerr=avg_cond_accuracy_stds)
plt.title('Average Configural/Featural Accuracy')
plt.plot([-0.5, 1.5], [0.5, 0.5], color='black', linestyle='--', linewidth=0.5)
plt.show()