# Write a program that converts a color image to grayscale. The user supplies
# the name of a file containing a GIF or PPM image, and the program loads the
# image and displays the file. At the click of the mouse, the program converts
# the image to grayscale. The user is then prompted for a file name to store
# the grayscale image in.
# You will probably want to go back and review the Image object from the
# graphics library (Section 4.7.4). The basic idea for converting the image is
# to go through it pixel by pixel and convert each one from color to an
# appropriate shade of gray. A gray pixel is created by setting its red,
# green, and blue components to have the same brightness. So color_rgb(0,0,0)
# is black, color rgb(255,255,255) is white, and color rgb(127,127,127) is a
# gray “halfway” between. You should use a weighted average of the original
# RGB values to determine the brightness of the gray. Here is the pseudocode
# for the grayscale algorithm:
#
#   for each row in the image:
#       for each column in the image:
#           r, g, b = get pixel information for current row and column
#           brightness = int(round(0.299r + 0.587g + 0.114b))
#           set pixel to color_rgb(brightness, brightness, brightness)
#       update the image # to see progress row by row
#
# Note: The pixel operations in the Image class are rather slow, so you
# will want to use relatively small images (not 12 megapixels) to test your
# program.

import graphics

def main():
    in_filename = input("Input filename: ")
    image = graphics.Image(graphics.Point(0, 0), in_filename)

    win = graphics.GraphWin("Grayscaler", image.getWidth(), image.getHeight())
    image.move(image.getWidth()/2, image.getHeight()/2)
    image.draw(win)

    win.getMouse()
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            brightness = int(round(0.229 * r + 0.587 * g + 0.114 * b))
            image.setPixel(
                x, y, graphics.color_rgb(brightness, brightness, brightness))
        graphics.update()

    out_filename = input("Output filename: ")
    image.save(out_filename)
    win.getMouse()

main()