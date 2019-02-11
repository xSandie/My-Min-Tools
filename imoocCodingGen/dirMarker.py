def make_dir(dir_list):
    import os
    for item in dir_list:
        os.makedirs(item)

def gen_dir_list(list_to_gen, relative_location):
    return [relative_location+item for item in list_to_gen]