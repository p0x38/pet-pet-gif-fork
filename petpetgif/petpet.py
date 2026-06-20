from PIL import Image
from petpetgif.saveGif import save_transparent_gif
from pathlib import Path
import importlib.resources
from typing import cast

frames = 10
resolution = (128, 128)
delay = 20

def make(source, dest):
    """

    :param source: A filename (string), pathlib.Path object or a file object. (This parameter corresponds
                   and is passed to the PIL.Image.open() method.)
    :param dest: A filename (string), pathlib.Path object or a file object. (This parameter corresponds
                   and is passed to the PIL.Image.save() method.)
    :return: None
    """
    images = []
    base = Image.open(source).convert('RGBA').resize(resolution)
    
    res_w, res_h = resolution

    for i in range(frames):
        squeeze = i if i < frames/2 else frames - i
        width = 0.8 + squeeze * 0.02
        height = 0.8 - squeeze * 0.05
        offsetX = (1 - width) * 0.5 + 0.1
        offsetY = (1 - height) - 0.08

        canvas = Image.new('RGBA', size=resolution, color=cast(int, (0,0,0,0)))
        
        resized_w = round(width * res_w)
        resized_h = round(height * res_h)
        pos_x = round(offsetX * res_w)
        pos_y = round(offsetY * res_h)
        
        canvas.paste(base.resize((resized_w, resized_h)), (pos_x, pos_y))
        
        img_path = importlib.resources.files(__package__ or __name__).joinpath(f"img/pet{i}.gif")
        with img_path.open("rb") as stream:
            pet = Image.open(stream).convert('RGBA').resize(resolution)
            canvas.paste(pet, mask=pet)
        
        images.append(canvas)

    save_transparent_gif(images, durations=20, save_file=dest)