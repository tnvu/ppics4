# Modify the cannonball simulation from the chapter so that it also calculates
# the maximum height achieved by the cannonball.

# projectile.py

"""
Provides a simple class for modeling the flight of projectiles.
"""


from math import sin, cos, radians


class Projectile:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

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
    
# cball4.py

def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t


def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    max_height = h0
    while cball.getY() >= 0:
        if cball.getY() > max_height:
            max_height = cball.getY()
        cball.update(time)
    print(f"\nDistance traveled: {cball.getX():0.1f} meters.")
    print(f"Maximum height: {max_height:0.1f} meters.")


if __name__ == "__main__":
    main()