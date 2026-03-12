# Modify the cannonball animation so that the input dialog window stays on
# screen at all times.

import graphics
import math

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = graphics.Point(self.xmin, self.ymin)
        p2 = graphics.Point(self.xmax, self.ymax)
        self.rect = graphics.Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = graphics.Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

class Projectile:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos

class ShotTracker:
    def __init__(self, win, angle, velocity, height):
        """win is a GraphWin to display the shot. angle, velocity,
           and height are initial projectile paramters
        """
        self.proj = Projectile(angle, velocity, height)
        self.marker = graphics.Circle(graphics.Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        """Move the shot dt seconds farther along its flight"""
        # update the projectile
        self.proj.update(dt)
        # move the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx, dy)

    def getX(self):
        """Return the current x coordinate of the shot's center"""
        return self.proj.getX()
    
    def getY(self):
        """Return the current y coordinate of the shot's center"""
        return self.proj.getY()
    
    def undraw(self):
        self.marker.undraw()

class InputDialog:
    """A custom window for getting simulation values (angle, velocity, and
       height) from the user."""
    
    def __init__(self, angle, vel, height):
        """Build and display the input window"""
        self.win = win = graphics.GraphWin("Initial Values", 200, 300)
        win.setCoords(0, 4.5, 4, 0.5)
        graphics.Text(graphics.Point(1, 1), "Angle").draw(win)
        self.angle = graphics.Entry(graphics.Point(3, 1), 5).draw(win)
        self.angle.setText(str(angle))
        graphics.Text(graphics.Point(1, 2), "Velocity").draw(win)
        self.vel = graphics.Entry(graphics.Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))
        graphics.Text(graphics.Point(1, 3), "Height").draw(win)
        self.height = graphics.Entry(graphics.Point(3, 3), 5).draw(win)
        self.height.setText(str(height))

        self.fire = Button(win, graphics.Point(1, 4), 1.25, 0.5, "Fire!")
        self.fire.activate()

        self.quit = Button(win, graphics.Point(3, 4), 1.25, 0.5, "Quit")
        self.quit.activate()

    def interact(self):
        """Wait for a user to click Quit or Fire button
           Returns a string indicating which button was clicked
        """
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"
    
    def getValues(self):
        """Return input values"""
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a, v, h
    
    def close(self):
        """Close the window"""
        self.win.close()


    def updateShots(self, dt):
        for shot in self.shots[:]:
            shot.update(dt)
            if shot.getY() < 0 or shot.getX() < -10 or shot.getX() > 210:
                self.shots.remove(shot)
                shot.undraw()

def main():
    # create animation window
    win = graphics.GraphWin("Projectile Animation", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)
    graphics.Line(graphics.Point(-10, 0), graphics.Point(210, 0)).draw(win)
    for x in range(0, 210, 50):
        graphics.Text(graphics.Point(x, -5), str(x)).draw(win)
        graphics.Line(graphics.Point(x, 0), graphics.Point(x, 2)).draw(win)
    
    angle, vel, height = 45.0, 40.0, 2.0
    inputwin = InputDialog(angle, vel, height)
    while True:
        # interact with the user
        choice = inputwin.interact()
        if choice == "Quit":
            break
        angle, vel, height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:
            shot.update(1/50)
            graphics.update(50)
    win.close()

main()