import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import numpy as np
import AudioManager
import sounddevice as sd
from AudioEffect import DigitalDelay
from AudioManager import Player
from EffectChain import EffectChain

sample_rate = 44100


# Assuming 'audio_array' is your NumPy 2D array and 'sample_rate' is the sampling rate
# audio_array = np.random.uniform(-1, 1, (sample_rate * duration, channels))

wav = AudioManager.WavFile("/home/sappirb/code/Spectrum-Analyzer/data/Audio_Processor_Clap.wav")

wav_data = wav.m_data

audio_array = wav_data.getSamples().copy()
audio_array.setflags(write=1)


effect_configs = [
    {
        "effect_name": "Overdrive",
        "arguments": {
            "mix": 0.5,
            "drive": 10,
            "level": 1.0
        }
    },
    {
        "effect_name": "DigitalDelay",
        "arguments": {
            "feedback": 0.9,
            "time": 0.15,
            "mix": 0.5
        }
    }
]
effect_chain = EffectChain(effect_configs)

wav.update_effect_chain(effect_chain)

wav.play_audio()

wav.m_effect_chain.remove_all()

wav.play_audio()
# delay = DigitalDelay()

# delay.process(audio_array)

# Play the audio
# sd.play(audio_array, samplerate=sample_rate)
# sd.wait()  # Wait until the audio playback is finished


# player = Player()