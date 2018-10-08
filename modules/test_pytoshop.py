import pytoshop
import numpy as np
from pytoshop.user import nested_layers as nl
from pytoshop import enums

img_layer_conf = dict(
    name = 'layer',
    visible = True,
    opacity = 255,
    group_id = 0,
    blend_mode = enums.BlendMode.normal,
    top = 0,
    left = 0,
    bottom = None,
    right = None,
    channels = None,
    metadata = None,
    layer_color = 0,
    color_mode = enums.ColorMode.rgb)

layers_to_psd_conf = dict(
    color_mode = enums.ColorMode.rgb,
    version = enums.Version.psd,
    compression = enums.Compression.rle,
    depth = enums.ColorDepth.depth8,
    size = None,
    vector_mask = False)

color_sheet = np.array([(34,2,5,3,46,63,64,56,7,8),
                        (34,2,5,3,46,63,64,56,7,8)])

if __name__ == "__main__":
    with open('../../empty.psd', 'rb') as fd:
        psd = pytoshop.read(fd)

    nested_stuff = nl.psd_to_nested_layers(psd)
    new_layer = nl.Image(**img_layer_conf)
    new_layer.set_channel(color=enums.ColorChannel.red,
                          channel=color_sheet)
    new_layer.set_channel(color=enums.ColorChannel.green,
                          channel=color_sheet)
    new_layer.set_channel(color=enums.ColorChannel.blue,
                          channel=color_sheet)
    nested_stuff.append(new_layer)

    nl.pprint_layers(nested_stuff)

    nl.nested_layers_to_psd(psd, **layers_to_psd_conf)
    with open('../../empty_layerd.psd', 'wb') as fe:
        psd.write(fe)




