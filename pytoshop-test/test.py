import sys, os
import pytoshop
# from pytoshop.core import Header
# from pytoshop.user import nested_layers
# from pytoshop.enums import ColorMode, BlendMode
from psd_tools import PSDImage


if __name__ == '__main__':
    psd = PSDImage.load(sys.argv[1])
    psd.print_tree()

    for layer in psd.layers:
        print(layer.kind)

    img = psd.as_PIL()




