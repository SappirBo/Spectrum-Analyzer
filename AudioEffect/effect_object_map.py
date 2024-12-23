from .effect_interface import EffectInterface
from .digital_delay import DigitalDelay
from .overdrive import Overdrive
from .equalizer import Equalizer
from .level import Level
from .compressor import Compressor

class EffectObjectMap:
    def __init__(self):
        '''
        This class is a Effect name to Effect object converter.
        Here all the effects map will be updated and used to get a single onject of an EffectInteface. 
        '''
        self.effect_class_map = {
            'DigitalDelay': DigitalDelay,
            'Overdrive': Overdrive,
            'Level': Level,
            "Equalizer": Equalizer,
            "Compressor": Compressor
        }
        pass

    def get_single_effect_obj(self, effect_name:str)->EffectInterface:
        if effect_name not in self.effect_class_map:
            print(f"EffectChain: get_single_effect_obj: {effect_name} not found in effect class map!")
            return 
        else:
            return self.effect_class_map.get(effect_name)()
        
    def get_single_effect_class(self, effect_name:str)->EffectInterface:
        if effect_name not in self.effect_class_map:
            print(f"EffectChain: get_single_effect_obj: {effect_name} not found in effect class map!")
            return 
        else:
            return self.effect_class_map.get(effect_name)
        

