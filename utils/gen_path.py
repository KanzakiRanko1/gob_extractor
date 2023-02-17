import os


def gen_path(prefix, path):
    """Generates full paths as a single directory within the prefix folder. Should be OS-agnostic."""
    if os.name == 'nt':
        return prefix+'\\'+path.lower().replace('\\', '_').replace('.gob','')
    return prefix+'/'+path.lower().replace('/','_').replace('.gob','')
