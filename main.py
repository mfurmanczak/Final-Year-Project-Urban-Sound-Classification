import librosa
import numpy as np
import os
from sklearn.model_selection import train_test_split

# Path to main folder of the dataset
main_sounds_dir = '../dataset/urbansound8k/audio/fold'
extension = '.wav'

# Create a list of paths to the folders in the dataset
folders = []
for num in range(1,11):
    folders.append(main_sounds_dir + str(num) + '/')    
    
sounds = [[],[]]
counter = 0
# Create a list of all sound files in the dataset
for filename in os.listdir(folders[0]):
    if filename.endswith(extension):
        sounds.append([filename])
# print(folders[0])

# Create a list of all sound files to a text file
# with open('sounds.txt', 'w') as f:
#     for sound in sounds:
#         f.write("%s \n"%sound)

# Train the data on split of the dataset
for files in sounds:
    X_train, X_test, Y_train, Y_test = train_test_split(sounds, sounds, test_size=0.2)
       
# print(X_train)