# Modify the graphical future value program so that the input (principal and
# APR) also are done in a graphical fashion using Entry objects.

import graphics

def main():
    win = graphics.GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)

    # Labels
    graphics.Text(graphics.Point(-1, 0),     ' 0.0K').draw(win)
    graphics.Text(graphics.Point(-1, 2500),  ' 2.5K').draw(win)
    graphics.Text(graphics.Point(-1, 5000),  ' 5.0K').draw(win)
    graphics.Text(graphics.Point(-1, 7500),  ' 7.5K').draw(win)
    graphics.Text(graphics.Point(-1, 10000), '10.0K').draw(win)
    
    # Input
    graphics.Text(graphics.Point(3, 10000), "Principal ($):").draw(win)
    graphics.Text(graphics.Point(3, 9000),  "      APR (%):").draw(win)
    input_principal = graphics.Entry(graphics.Point(6.5, 10000), 7)
    input_principal.setText("2000.00")
    input_principal.draw(win)
    input_apr = graphics.Entry(graphics.Point(6.5, 9000), 7)
    input_apr.setText("0.10")
    input_apr.draw(win)
    button = graphics.Text(graphics.Point(5, 7500), "Calculate")
    button.draw(win)
    graphics.Rectangle(graphics.Point(3.5, 7000),
                       graphics.Point(6.5, 8000)).draw(win)
    win.getMouse()
    principal = float(input_principal.getText())
    apr = float(input_apr.getText())

    # Draw future values
    bar = graphics.Rectangle(graphics.Point(0, 0),
                             graphics.Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = graphics.Rectangle(graphics.Point(year, 0),
                                 graphics.Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()

main()