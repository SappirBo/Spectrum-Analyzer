import numpy as np
from .effect_interface import EffectInterface
import audio_process_lib

class DigitalDelay(EffectInterface):
    def __init__(self, feedback:float=0.5, time:float=0.5,  mix:float=0.5, level:float = 0):
        """
        Initialize the DigitalDelay effect with decay and mix parameters.
        
        Parameters:
        feedback (float): Controls the feedback duration of the delay. Values  range from 0 to 1.
        mix (float): Controls the mix between the original and reverberated sound. Values  range from 0 to 1.
        """
        self.feedback = self.set_between_range(0, 1, feedback)
        self.time = self.set_between_range(0, 10,time)
        self.mix = self.set_between_range(0,1, mix)
        self.level = self.set_between_range(-10,10,level)
        self.delay_buffer = np.zeros_like(44100*1)

    def process(self, data: np.ndarray, rate=44100) -> None:
        """
        Apply a delay effect directly to the audio data in-place.
        
        Parameters:
        data (numpy.array): The audio data to process. This data will be modified in place.
        rate (int): The sampling rate of the audio data.
        """
        # self.process_python(data,rate)
        self.process_rust(data,rate)
          
    def process_rust(self, data: np.ndarray, rate: int = 44100)->None:
        process_data = data.astype(np.float64)
        audio_process_lib.process_digital_delay(process_data, self.feedback, self.time, self.level, self.mix)
        np.copyto(data, process_data)
    
    def process_python(self, data: np.ndarray, rate: int = 44100)->None:
        self.delay_buffer = np.zeros_like(data)
        self.delay_buffer = self.delay_buffer[0: int(44100 * self.time)]
        delay_index = 0
        for i in range(len(data)):
            new_sample =  data[i] * (1 - self.mix) +  self.delay_buffer[delay_index] * (self.mix)
            data[i] =  new_sample
            self.delay_buffer[delay_index] = new_sample * self.feedback
            delay_index += 1
            if delay_index == len(self.delay_buffer):
                delay_index = 0
        self.set_levels(self.level, data)
            
    def process_get_new_ndarray(self, data, rate=44100):
        """
        Apply a delay effect directly to the audio data in-place.
        
        Parameters:
        data (numpy.array): The audio data to process. This data will be modified in place.
        rate (int): The sampling rate of the audio data.
        """
        self.delay_buffer = np.zeros_like(data)
        self.delay_buffer = self.delay_buffer[0: int(44100 * self.time)]
        samples_delayed: np.ndarray = np.zeros_like(data)
        delay_index = 0
        for i in range(len(data)):
            sample = data[i]
            new_sample =  sample * (1 - self.mix) +  self.delay_buffer[delay_index] * (self.mix)
            samples_delayed[i] =  new_sample
            self.delay_buffer[delay_index] = new_sample * self.feedback
            delay_index += 1
            if delay_index == len(self.delay_buffer):
                delay_index = 0
            
        return samples_delayed
    
    def test(self):
        print("here")

    def get_effect_arguments(self)->dict:
        arguments:dict =  {
            "parameters":{
                "mix":{
                    "p_type": "slider",
                    "min":0.0,
                    "max": 1.0,
                    "default":0.0
                },
                "feedback":{
                    "p_type": "slider",
                    "min":0.0,
                    "max": 1.0,
                    "default":0.5
                },
                "time": {
                    "p_type": "slider",
                    "min":0.0,
                    "max": 10.0,
                    "default":0.0
                },
                "level": {
                    "p_type": "slider",
                    "min":-10.0,
                    "max": 10.0,
                    "default":0.0
                }
            }
        }
        return arguments