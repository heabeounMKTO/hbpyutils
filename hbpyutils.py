import os
import math
import random

def get_file_by_extension(target_folder: str, extensions: tuple):
    '''
    Takes in a target folder and a tuple of extensions,
    returns a list of path strings of files with the specified extensions,
    including those in subfolders.
    '''
    _a = []
    for root, _, files in os.walk(target_folder):
        for file in files:
            if file.endswith(extensions):
                _a.append(os.path.join(root, file))
    return _a

def ratio_list(input_list: list, ratio: float = 0.7):
    '''
    Separates a list into two by a given ratio, randomly selecting elements.
    '''
    input_copy = input_list.copy()
    selection_count = math.floor(len(input_copy) * ratio)
    selected_list = random.sample(input_copy, selection_count)
    remaining_list = [item for item in input_copy if item not in selected_list]
    return selected_list, remaining_list
