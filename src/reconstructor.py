import os
from settings import settings

def reconstruct():
    # GO TO DIR WITH SCANNED IMAGES
    os.chdir(settings['current_save_dir'])

    print("Running meshroom")
    command = '%s  -p photogrammetry -i "%s" -o "%s/result"' % (settings['path_to_meshroom_batch'], settings['current_save_dir'], settings['current_save_dir'])
    print(command)
    os.system(command) # Run reconstrcuction
