import pytoshop
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
    visible = True,
    opacity = 255,
    group_id = 0,
    blend_mode = BlendMode.normal,
    top = 0,
    left = 0,
    bottom = 240,
    right = 240,
    channels = channels,
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
    PSDFILE = 'example.psd'
    with open(PSDFILE, 'rb') as fd:
        psd = pytoshop.read(fd)

        nested_stuff = nl.psd_to_nested_layers(psd)
        new_layer = nl.Image(**img_layer_conf)
        nested_stuff.insert(0, new_layer)

        nl.pprint_layers(nested_stuff)

        psd_tunned = nl.nested_layers_to_psd(layers = nested_stuff,
                                             color_mode = ColorMode.rgb,
                                             size = (240, 240))

        with open(PSDFILE.split('.')[0] + '_tunned.psd', 'wb') as fe:
            psd_tunned.write(fe)




