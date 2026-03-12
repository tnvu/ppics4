# Extend the cannonball animation from the chapter to allow the user to
# adjust the initial height of the launcher. The height adjustment should be
# handled similar to the way angle and velocity are. Pick a pair of keys of
# your own choosing for adjusting the height up and down.

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

class Launcher:
    def __init__(self, win):
        # Draw the base shot of the launcher
        self.base = graphics.Circle(graphics.Point(0, 0), 3)
        self.base.setFill("red")
        self.base.setOutline("red")
        self.base.draw(win)
        # Save the window and create initial angle and velocity
        self.win = win
        self.angle = math.radians(45.0)
        self.vel = 40.0
        self.height = 0.0
        # Create initial dummy arrow (needed by redraw)
        self.arrow = graphics.Line(graphics.Point(0, self.height),
                                   graphics.Point(0, self.height))
        self.arrow.draw(win)
        self.redraw()

    def adjAngle(self, amt):
        """Change launch angle by amt degrees"""
        self.angle = self.angle + math.radians(amt)
        self.redraw()

    def adjVel(self, amt):
        """Change launch velocity by amt"""
        self.vel = self.vel + amt
        self.redraw()

    def adjHeight(self, amt):
        """Change launch height by amt"""
        self.height = self.height + amt
        if self.height < 0:
            self.height = 0
        self.redraw()

    def redraw(self):
        """Redraw the arrow to show current angle and velocity"""
        self.arrow.undraw()
        self.base.move(0, self.height - self.base.getP1().getY())
        pt2 = graphics.Point(self.vel * math.cos(self.angle),
                             self.height + self.vel * math.sin(self.angle))
        self.arrow = graphics.Line(graphics.Point(0, self.height), pt2)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)
        self.arrow.draw(self.win)

    def fire(self):
        return ShotTracker(self.win, math.degrees(self.angle), self.vel, self.height)

class ProjectileApp:
    def __init__(self):
        # create animation window
        self.win = graphics.GraphWin("Projectile Animation", 640, 480, 
                                     autoflush=False)
        self.win.setCoords(-10, -10, 210, 155)
        graphics.Line(graphics.Point(-10, 0),
                      graphics.Point(210, 0)).draw(self.win)
        for x in range(0, 210, 50):
            graphics.Text(graphics.Point(x, -5), str(x)).draw(self.win)
            graphics.Line(graphics.Point(x, 0),
                          graphics.Point(x, 2)).draw(self.win)
        # Add launcher to the window
        self.launcher = Launcher(self.win)
        # Start with an empty list of "live" shots
        self.shots = []

    def run(self):
        # main event/animation loop
        while True:
            self.updateShots(1/50)
            key = self.win.checkKey()
            if key in ['q', 'Q']:
                break
            if key == "Up":
                self.launcher.adjAngle(5)
            elif key == "Down":
                self.launcher.adjAngle(-5)
            elif key == "Right":
                self.launcher.adjVel(5)
            elif key == "Left":
                self.launcher.adjVel(-5)
            elif key == "Prior":
                self.launcher.adjHeight(5)
            elif key == "Next":
                self.launcher.adjHeight(-5)
            elif key in ['f', 'F']:
                self.shots.append(self.launcher.fire())
            graphics.update(50)
        self.win.close()

    def updateShots(self, dt):
        for shot in self.shots[:]:
            shot.update(dt)
            if shot.getY() < 0 or shot.getX() < -10 or shot.getX() > 210:
                self.shots.remove(shot)
                shot.undraw()

def main():
    ProjectileApp().run()

main()