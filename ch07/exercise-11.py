# Write a program to convert an image to its color negative. The general
# form of the program will be similar to that of the previous problem. The
# negative of a pixel is formed by subtracting each color value from 255. So
# the new pixel color is color rgb(255-r, 255-g, 255-b).

import graphics

def main():
    in_filename = input("Input filename: ")
    image = graphics.Image(graphics.Point(0, 0), in_filename)

    win = graphics.GraphWin("Negative", image.getWidth(), image.getHeight())
    image.move(image.getWidth()/2, image.getHeight()/2)
    image.draw(win)

    win.getMouse()
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b = image.getPixel(x, y)
            color = graphics.color_rgb(255 - r, 255 - g, 255 - b)
            image.setPixel(x, y, color)
        graphics.update()
    win.getMouse()

main()