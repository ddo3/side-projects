# pixel image generator
from PIL import Image
import math
import sys
#create a new new image
#PIL.Image.new(mode, size, color=0)
#Image.show(title=None, command=None)
#im = Image.open("bride.jpg")

#Image.getpixel(xy)
#Image.putpixel(xy, value)
#PIL.Image.size - (width, height)
#PIL.Image.width
#PIL.Image.height

#mode = RGB, size is user input - but we will make it 8 by 8

###STEPS####
"""
1 open the Image
2 get the size of the iamge
3 find appropriate way to scale that image
    maybe start with a 2/3 scale (round to whole number)
4 based on those numbers make a second iamge
5 for every 5th pixel, take a sample from the original pic
    and add it to new pic
6 evenrtually show new pic alongside old pic
"""
def makeImageSmaller(filename: str, magicNum: int) -> None:
    orig_im = Image.open(filename)

    orig_im_width = orig_im.width
    orig_im_height = orig_im.height

    new_width = math.floor(orig_im_width/magicNum)
    new_height = math.floor(orig_im_height/magicNum)

    new_im = Image.new('RGB', (new_width, new_height))

    y_index = 0;
    for i in range(orig_im_height):
        x_index = 0;
        for j in range(orig_im_width):
            if j == 0 and i % magicNum == 0:
                y_index = y_index + 1

            if i % magicNum == 0 and j % magicNum == 0:
                #get the color of the original color and
                pixel_col = orig_im.getpixel((j,i))
                #print((x_index, y_index))
                if x_index < new_width and y_index < new_height:
                    new_im.putpixel((x_index, y_index), pixel_col)
                    x_index = x_index + 1;

    orig_im.show()
    new_im.show()


def makePixelated(filename: str, magicNum: int) -> None:
    orig_im = Image.open(filename)

    orig_im_width = orig_im.width
    orig_im_height = orig_im.height

    new_im = Image.new('RGB', (orig_im_width, orig_im_height))

    offset = math.floor(magicNum/2)

    current_color_list = getRowColor(orig_im, magicNum, 0) #orig_im.getpixel((0 + offset,0 + offset))

    row_index = 0;
    for i in range(orig_im_height):
        for j in range(orig_im_width):
            if(i % magicNum == 0 and j == 0):
                # change the current color
                row_index = row_index + 1
                #if where we want to sample is out of range, use the last row of the image for pixels
                useLastRow = ((row_index * magicNum) + offset) >= orig_im_height
                current_color_list = getRowColor(orig_im, magicNum, row_index, useLastRow)


            new_im.putpixel((j, i), current_color_list[j])

    orig_im.show()
    new_im.show()

def getRowColor( image, magicNum, row_index, useLastRow=False):
    h = image.height
    w = image.width
    offset = math.floor(magicNum/2)
    colorList = []
    sampleRow = h - 1
    if not useLastRow:
        sampleRow = (magicNum * row_index) + offset

    currentColor = image.getpixel((0 + offset, sampleRow))
    for x in range(w):
        if x % magicNum == 0 and x + offset < w:
            currentColor = image.getpixel((x + offset, sampleRow))
        elif x + offset > w:
            currentColor = image.getpixel((w - 1, sampleRow))
        colorList.append(currentColor)
    return colorList

#makeImageSmaller('color.jpg', 7)
#makePixelated('face3.jpg', 7)

if __name__ == '__main__':   ## command python pixel-gen.py face2 10
    filename = sys.argv[1] + ".jpg"
    magicNum = int(sys.argv[2])
    makePixelated(filename, magicNum)
