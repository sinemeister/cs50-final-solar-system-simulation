import math

# Set colors
SUN = (253, 184, 19)
MERCURY = (219, 206, 202)
VENUS = (139, 125, 130)
EARTH = (40, 122, 184)
MARS = (156, 46, 53)
JUPITER = (201, 144, 57)
SATURN = (101, 95, 69)
URANUS = (209, 231, 231)
NEPTUNE = (0, 125, 172)


# Define Planet class
class Planet:
    # Define class attributes
    AU = 149.6e6 * 1000 # Astronomical Unit (AU) - distance between Sun and the Earth (in meters)
    G = 6.67428e-11 # Gravitational constant
    SCALE = 30 / AU # Scale to draw - approximately 1AU = 30px here
    TIMESTEP = 3600 * 24 # On every update of the screen, it will show 1 day of the celestial bodies

    def __init__(self, x, y, radius, color):
        # Planets will be drawn as circles with Pygame
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
        # Misc attributes of the planets
        self.name = ""
        self.mass = 0
        self.orbit_time = 0
        self.actual_radius = 0
        self.gravity = 0
        self.mean_temp = 0
        self.distance_to_sun = 0

        # Their inital velocities are set to 0
        self.x_vel = 0
        self.y_vel = 0

        # Sun will also be instantiated from the Planet class as basically only thing that Sun needs from this class is draw method
        # and the constants (class attributes)
        # Sun is needed by other planets for the gravitational calculations
        self.sun = False # Will be set to True when Sun is instantiated


    # Get x and y coordinates of the bodies
    def draw_planet(self):
        # Scale down the planets' x and y coordinates when draw
        x = self.x * Planet.SCALE + 1920 / 2
        y = self.y * Planet.SCALE + 1080 / 2
      
        # Return x and y to be drawn in the main script to avoid circular import (source, i.e. window is need to draw circle)
        return x, y
    
    # Calculate total gravitational force exerted on each planet
    # and move them in their orbits
    def calculate_gravitational_force(self, planet_list):
        # Set gravitational force's x- and y-components to 0 initally
        total_fx, total_fy = 0, 0
        # Iterate over the planet_list
        for planet in planet_list:
            # Do not calculate gravitational force for the planet if force applied by itself
            # Otherwise divison by zero error would be raised (refer that force is G * m_1 * m_2 / distance ^ 2)
            # and practically it has no effect
            if self.name == planet.name:
                continue
            
            # Calculate the distance between self and the other celestial bodies
            distance_x = planet.x - self.x
            distance_y = planet.y - self.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

            # If the other celestial body is Sun, set self.distance_to_sun to distance
            if planet.sun:
                self.distance_to_sun = distance

            # Calculate gravitational force (F = G * m_1 * m_2 / d ^ 2 -- Newton's law of universal gravitation)
            gravitational_force = Planet.G * self.mass * planet.mass / distance ** 2

            # Calculate x- and y-components of the force
            angle = math.atan2(distance_y, distance_x) # Angle between distance vectors
            force_x = math.cos(angle) * gravitational_force
            force_y = math.sin(angle) * gravitational_force

            # Update total force components on the planet
            total_fx += force_x
            total_fy += force_y
        
        # Update planets' x and y velocities according to the Newton's second law of motion: F = m * a (v/t) => a = (F / m)
        # Velocity increase indicates accelaration
        self.x_vel += total_fx / self.mass * Planet.TIMESTEP
        self.y_vel += total_fy / self.mass * Planet.TIMESTEP
        # Update planets' x and y coordinates according to displacement equation: Δd = Δv * Δt
        # This will make planets orbit around the Sun
        self.x += self.x_vel * Planet.TIMESTEP
        self.y += self.y_vel * Planet.TIMESTEP


# Instantiate planets (and Sun)
sun = Planet(0, 0, 8, SUN)
sun.sun = True
sun.mass = 1.98892e30
sun.name = "Sun"
sun.actual_radius = 696340
sun.gravity = 274.0
sun.mean_temp = 5499

mercury = Planet(0.387 * Planet.AU, 0, 2, MERCURY)
mercury.y_vel = -math.sqrt(Planet.G * sun.mass / (0.387 * Planet.AU))
mercury.mass = 0.33e24
mercury.name = "Mercury"
mercury.orbit_time = 88
mercury.actual_radius = 2440
mercury.gravity = 3.7
mercury.mean_temp = 167

venus = Planet(0.723 * Planet.AU, 0, 3, VENUS)
venus.y_vel = -math.sqrt(Planet.G * sun.mass / (0.723 * Planet.AU))
venus.mass = 4.8685e24
venus.name = "Venus"
venus.orbit_time = 225
venus.actual_radius = 6052
venus.gravity = 8.9
venus.mean_temp = 464

earth = Planet(-1 * Planet.AU, 0, 3, EARTH)
earth.y_vel = math.sqrt(Planet.G * sun.mass / (1 * Planet.AU))
earth.mass = 5.9742e24
earth.name = "Earth"
earth.orbit_time = 365
earth.actual_radius = 6371
earth.gravity = 9.8
earth.mean_temp = 15

mars = Planet(-1.524 * Planet.AU, 0, 3, MARS)
mars.y_vel = math.sqrt(Planet.G * sun.mass / (1.524 * Planet.AU))
mars.mass = 0.639e24
mars.name = "Mars"
mars.orbit_time = 687
mars.actual_radius = 3390
mars.gravity = 3.7
mars.mean_temp = -65

jupiter = Planet(5.203 * Planet.AU, 0, 5, JUPITER)
jupiter.y_vel = -math.sqrt(Planet.G * sun.mass / (5.203 * Planet.AU))
jupiter.mass = 1898.2e24
jupiter.name = "Jupiter"
jupiter.orbit_time = 4333
jupiter.actual_radius = 69911
jupiter.gravity = 23.1
jupiter.mean_temp = -110

saturn = Planet(-9.537 * Planet.AU, 0, 4, SATURN)
saturn.y_vel = math.sqrt(Planet.G * sun.mass / (9.537 * Planet.AU))
saturn.mass = 568.34e24
saturn.name = "Saturn"
saturn.orbit_time = 10759
saturn.actual_radius = 58232
saturn.gravity = 9.0
saturn.mean_temp = -140

uranus = Planet(-19.191 * Planet.AU, 0, 4, URANUS)
uranus.y_vel = math.sqrt(Planet.G * sun.mass / (19.191 * Planet.AU))
uranus.mass = 86.810e24
uranus.name = "Uranus"
uranus.orbit_time = 30687
uranus.actual_radius = 25362
uranus.gravity = 8.7
uranus.mean_temp = -195

neptune = Planet(30.069 * Planet.AU, 0, 4, NEPTUNE)
neptune.y_vel = -math.sqrt(Planet.G * sun.mass / (30.069 * Planet.AU))
neptune.mass = 102.413e24
neptune.name = "Neptune"
neptune.orbit_time = 60190
neptune.actual_radius = 24622
neptune.gravity = 11.0
neptune.mean_temp = -200

# Store all of the Planet objects in one list
planet_list = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]