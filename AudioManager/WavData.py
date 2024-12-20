import numpy as np

class WavData:
    def __init__(self, samples, frame_rate, num_channels, sampwidth) -> None:
        self.m_samples = samples
        self.m_sample_rate = frame_rate
        self.m_num_channels = num_channels
        self.m_sampwidth = sampwidth
    
    def getSamples(self) ->np.ndarray:
        return self.m_samples
    
    def get_samples_dtype(self)->np.dtype:
        return self.m_samples.dtype
    
    def getSampleRate(self):
        return self.m_sample_rate
    
    def getNumberOfChannels(self):
        return self.m_num_channels
    
    def getSampwidth(self):
        return self.m_sampwidth
    
    def toString(self) -> str:
        data_str = 'Samples Number: '
        data_str += str(len(self.m_samples)) + '\n'
        data_str += 'sample type'
        data_str += str(type(self.m_samples)) + '\n'
        data_str += 'Frame Rate: '
        data_str += str(self.m_sample_rate) + '\n'
        data_str += 'Number Of Channels: '
        data_str += str(self.m_num_channels) + '\n'
        data_str += 'Sample Width: '
        data_str += str(self.m_sampwidth)
        return data_str

    
