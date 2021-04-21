from random import random,randint
from PIL import Image, ImageDraw
from math import sin, cos, radians

#to set up, open cmd and run "pip install Pillow"
#also make a folder called "fractals" inside the directory of this file

def generate_fractal(filename:str, seed:int, shape=(512, 512)):
    '''
    draws a branch from bottom middle
    and then draws two branches outward
    from the end of that one. 
    The angle is determined by the seed(an integer)

    PARAMETERS:
    - filename: the file name to output to (ex. "./fractals/A.png")
    - seed: an integer used to determine length/angle of branches for variance
    - shape: (width, height) of the image
    '''
    img = Image.new(mode="RGB", size=shape, color=(255,255,255))
    draw = ImageDraw.Draw(img)
    def branch(start, angle, length):
        end = (start[0]+length*cos(radians(angle)), start[1]+length*sin(radians(angle)))
        draw.line([start, end], width=2*(1+seed//2), fill=0)
        if length<5:
            return None
        branch(end, angle+seed*20, length/(1.5+seed/26))
        branch(end, angle-seed*20, length/(1.5+seed/26))
    branch((shape[0]/2,shape[1]),-90, seed*(shape[1]/25)+shape[1]/4)
    img.save(filename, format="png")

if __name__ == '__main__':
    #generate a list of letters 
    alphabet = list("ABCDE")
    print(f"Alphabet: {alphabet}")
    

    #generate fractal for each letter in alphabet
    #use index+2 in list as seed
    for i,letter in enumerate(alphabet):
        generate_fractal(filename = f"./fractals/{letter}.png",seed = i+2, shape=(1024,1024))

