import os



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
