import os

from app.person_pc import MePC
from app.util import dat2pic

if not os.path.exists('./data/'):
    os.mkdir('./data/')
if not os.path.exists('./data/image'):
    os.mkdir('./data/image')


def get_abs_path(path):
    # return os.path.join(os.getcwd(), 'app/data/icons/404.png')
    if path:
        base_path = os.getcwd() + "/data/image"
        output_path = dat2pic.decode_dat(os.path.join(MePC().wx_dir, path), base_path)  # './data/image')
        return output_path if output_path else ':/icons/icons/404.png'
    else:
        return ':/icons/icons/404.png'