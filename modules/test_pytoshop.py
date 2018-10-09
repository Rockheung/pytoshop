import pytoshop, os
import numpy as np
from PIL import Image
from pytoshop.user import nested_layers as nl
from pytoshop.enums import *
from pytoshop.image_data import ImageData


img = Image.open('hello.png')
img = np.array(img)
channels = [img[:,:,0],
            img[:,:,1],
            img[:,:,2]]
data = ImageData(channels=img)


img_layer_conf = dict(
    name = 'layer_added',
    channels = channels,
    visible = True,
    opacity = 255,
    group_id = 0,
    blend_mode = BlendMode.normal,
    top = 0,
    left = 0,
    bottom = None,
    right = None,
    metadata = None,
    layer_color = 0,
    color_mode = None)


layers_to_psd_conf = dict(
    color_mode = ColorMode.rgb,
    version = Version.psd,
    compression = Compression.rle,
    depth = ColorDepth.depth8,
    size = None,
    vector_mask = False)


if __name__ == "__main__":
    PSD_FILE = 'example.psd'
    PSD_FILE_NAME, PSD_EXT = os.path.splitext(PSD_FILE)
    with open(PSD_FILE, 'rb') as fd:
        psd = pytoshop.read(fd)

        nested_stuff = nl.psd_to_nested_layers(psd)
        new_layer = nl.Image(**img_layer_conf)
        nested_stuff.insert(0, new_layer)

        nl.pprint_layers(nested_stuff)

        psd_tunned = nl.nested_layers_to_psd(layers = nested_stuff,
                                             color_mode = ColorMode.rgb)

        SAVE_PSD_FILE_NAME = PSD_FILE_NAME + '_tunned'
        while ((SAVE_PSD_FILE_NAME + '.psd') in os.listdir()):
            i = 2
            if i == 2:
                SAVE_PSD_FILE_NAME += '_' + str(i)
            else :
                SAVE_PSD_FILE_NAME = SAVE_PSD_FILE_NAME[:-2] + '_' + str(i)
            i += 1

        with open(SAVE_PSD_FILE_NAME + '.psd', 'wb') as fe:
            psd_tunned.write(fe)

        print('PSD file saved at {}'.format(SAVE_PSD_FILE_NAME + PSD_EXT))





