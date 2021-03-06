from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav

(rate,sig) = wav.read("file.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)

# print fbank_feat[1:3,:]
print mfcc_feat[1:3,:]

#Voice Activity detection example
from VoiceActivityDetection import simpleVAD

print mfcc_feat.shape
mfcc_feat = mfcc(sig,rate, VAD=simpleVAD)
print mfcc_feat.shape

