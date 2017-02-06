#!usr/bin/env python3

# Derek Lin
# ComputerGraphics pd10
# HW01
# 2017-02-06

#Format of .ppm file.
fileFormat = 'P3'
#Width of image in pixels.
width = 500
#Height ' ' ' .
height = 500
#Color depth
colorDepth = 255

rSet = 255
gSet = 255
bSet = 0


#writeHeader writes the header of the .ppm file
#takes the parameters for fileFormat, width and height of image in pixels, and colorDepth.
def writeHeader(fileFormat, width, height, colorDepth):
    file = open('square.ppm', 'w')
    file.write('{}\n{} {} {}\n'.format(fileFormat, width, height, colorDepth))
    for i in range(0, height):
        for i in range(0, width):
            file.write('{} {} {}\n'.format(255, 0, 255))
            
#def createSolidSquare(x, y, r, g, b,):
    

writeHeader(fileFormat, width, height, colorDepth)
#createSolidSquare(width, height, rSet, gSet, bSet)
