# Credits:
# - https://github.com/pierre-rouanet/dtw/blob/master/examples/MFCC%20%2B%20DTW.ipynb
# - https://github.com/d4r3topk/comparing-audio-files-python

import librosa
import librosa.display
import matplotlib.pyplot as plt
from numpy.linalg import norm
from scipy.spatial.distance import euclidean
from dtw import dtw

#Loading audio files
y1, sr1 = librosa.load('') 
y2, sr2 = librosa.load('') 

#Showing multiple plots using subplot
plt.subplot(1, 2, 1) 
mfcc1 = librosa.feature.mfcc(y1,sr1)   #Computing MFCC values
librosa.display.specshow(mfcc1)

plt.subplot(1, 2, 2)
mfcc2 = librosa.feature.mfcc(y2, sr2)
librosa.display.specshow(mfcc2)

# Select your preferred normalized distance equation
# dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=euclidean)

print("The normalized distance between the two : ", dist)   # 0 for similar audios 

plt.imshow(cost.T, origin='lower', cmap=plt.get_cmap('gray'), interpolation='nearest')
plt.plot(path[0], path[1], 'w')   #creating plot for DTW
plt.xlim((-0.5, cost.shape[0]-0.5))
plt.ylim((-0.5, cost.shape[1]-0.5))

plt.show()  #To display the plots graphically
