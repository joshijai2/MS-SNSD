import glob
import numpy as np
import soundfile as sf
import os
from audiolib import audioread, audiowrite, snr_mixer

def slicer():
    audioformat = "*.wav"
    audio_length = 10
    fs = 16000
    audio_dir = os.path.join(os.path.dirname(__file__), 'noise_train')
    filenames = glob.glob(os.path.join(audio_dir, audioformat))
    audio_length = int(audio_length*fs)
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir+"_new")
    for wavfile in filenames:
        file, fs = audioread(wavfile)
        
        for i in range(0,len(file)//audio_length):
            newfile = file[i:i+audio_length]
            newdir = os.path.join(os.path.dirname(__file__), 'noise_train_new\\'+wavfile.split("\\")[-1].split(".")[0]+"_"+str(i)+".wav")
            #print(wavfile)
            #print(newdir)
            audiowrite(newfile, fs, newdir, norm=False)
            
    return

if __name__=="__main__":
    slicer()
    input("Sliced successfully.\nPress Enter key to continue.\n")

        
    