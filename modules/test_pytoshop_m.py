import pytoshop, os
import numpy as np
from PIL import Image
from pytoshop.user import nested_layers as nl
from pytoshop.enums import *


#img_layer_conf = dict(
#    name = 'layer_added',
#    channels = channels,
#    visible = True,
#    opacity = 255,
#    group_id = 0,
#    blend_mode = BlendMode.normal,
#    top = 0,
#    left = 0,
#    bottom = None,
#    right = None,
#    metadata = None,
#    layer_color = 0,
#    color_mode = None)
#
#
#layers_to_psd_conf = dict(
#    color_mode = ColorMode.rgb,
#    version = Version.psd,
#    compression = Compression.rle,
#    depth = ColorDepth.depth8,
#    size = None,
#    vector_mask = False)

def img_stacker(psdfile, imgfile, layer_name = None, file_suffix='_stacked',
                offset = (0,0)):
    x, y = offset
    PSD_FILE_NAME, PSD_EXT = os.path.splitext(psdfile)
    if layer_name is None:
        layer_name = os.path.splitext(imgfile)[0]
    img = np.array(Image.open(imgfile))
    img_channels = [img[...,0],
                    img[...,1],
                    img[...,2]]
    with open(psdfile, 'rb') as fd:
        psd = pytoshop.read(fd)

        nested_stuff = nl.psd_to_nested_layers(psd)
        new_layer = nl.Image(name = layer_name,
                             channels = img_channels,
                             top = y,
                             left = x)
        nested_stuff.insert(0, new_layer)
        nl.pprint_layers(nested_stuff)

        psd_tunned = nl.nested_layers_to_psd(layers = nested_stuff,
                                             color_mode = ColorMode.rgb)

        SAVE_PSD_FILE_NAME = PSD_FILE_NAME + file_suffix

        # Somehow, write method seems to use opened file above
        with open(SAVE_PSD_FILE_NAME + PSD_EXT, 'wb') as fe:
            psd_tunned.write(fe)

    return SAVE_PSD_FILE_NAME + PSD_EXT


if __name__ == "__main__":
    ouput_file = img_stacker('example.psd', 'hello.png', offset = (0,10))
    print('PSD file saved at {}'.format(ouput_file))





