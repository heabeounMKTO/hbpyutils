import os
import math
import random

def get_file_by_extension(target_folder: str, extensions: tuple):
    '''
    takes in a target folder and a tuple of extensions , 
    returns a list of path strings
    '''
    _a = []
    for file in os.listdir(target_folder):
        if file.endswith(extensions):
            _a.append(os.path.join(target_folder, file))
    return _a


def ratio_list(input_list: list, ratio: float = 0.7):
    '''
    separate list into two by ratio by selecting randomly
    '''
    _cp = input_list.copy()
    _ratio_num = math.floor(len(_cp) * ratio)
    _ratio_list = []
    _sel_count = _ratio_num
    for _ in range(_ratio_num):
        random_index = random.randint(0, (_sel_count - 1))
        _sel_count -= 1
        _sel = input_list[random_index]
        _ratio_list.append(_sel)
        input_list.pop(input_list.index(_sel))
    return _ratio_list, input_list
        

