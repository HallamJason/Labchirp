import pyaudio
import math
import struct
import wave
import time
import os
import numpy as np
import aubio
import sys
from difflib import SequenceMatcher


# PyAudio object.
p = pyaudio.PyAudio()

# Open stream.
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Aubio's pitch detection.
pDetection = aubio.pitch("default", 2048, 2048//2, 44100)
# Set unit.
pDetection.set_unit("Hz")
#pDetection.set_silence(-40)

noSoundLength = 8
run = True
file = open("testfile.txt","w")

L = []

while run == True:
    endTime = time.time() + noSoundLength
    while time.time() < endTime:
        data = stream.read(1024)
        samples = np.fromstring(data, dtype=aubio.float_type)
        pitch = pDetection(samples)[0]
        print(pitch)

        if pitch > 3500.00 and pitch < 3700.00:
            file.write(str(0))
            L.append(str('0'))
        elif pitch > 3800.01 and pitch < 4100.00:
            file.write(str(1))
            L.append(str('1'))
        elif pitch > 4200.01 and pitch < 4500.00:
            file.write(str(2))
            L.append(str('2'))
        elif pitch > 4600.01 and pitch < 4700.00:
            file.write(str(3))
            L.append(str('3'))
        elif pitch > 4800.01 and pitch < 5100.00:
            file.write(str(4))
            L.append(str('4'))
        elif pitch > 5200.01 and pitch < 5500.00:
            file.write(str(5))
            L.append(str('5'))
        elif pitch > 5600.01 and pitch < 5800.00:
            file.write(str(6))
            L.append(str('6'))
        elif pitch > 5900.01 and pitch < 6100.00:
            file.write(str(7))
            L.append(str('7'))
        elif pitch > 6300.01 and pitch < 6400.00:
            file.write(str(8))
            L.append(str('8'))
        elif pitch > 6500.01:
            file.write(str(9))
            L.append(str('9'))
    run = False     
file.close()
print(L)

L1 = []

for i in range(len(L)):
    if (L[i] == L[i-1]) and (L[i] != L[i-2]):
        list.append(L1, L[i])
    elif (L[i] == '9'):
        list.append(L1, L[i])

pitchList = ''.join(L1)
print(pitchList)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

compare = (similar('106097083079078', pitchList)) * 100
print(compare)

playerFound = False
if (compare) > 70:
    print('Sound matched at %f percent' %(compare))