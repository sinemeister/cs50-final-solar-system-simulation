import pygame
import math
from planets import planet_list
pygame.init()


# Set window
WIDTH, HEIGHT = 1920, 1080
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Set fonts and legend texts
FONT = pygame.font.SysFont("Consolas", 18)
PAUSE_FONT = pygame.font.SysFont("Consolas", 24)
LEGEND_TEXTS = ["P Pause", "M Mute", "I Info off", "Q Quit", 
                "0 Sun", "1 Mercury", "2 Venus", "3 Earth", "4 Mars", "5 Jupiter", "6 Saturn", "7 Uranus", "8 Neptune"]

# Open the background music and play it on loop
BG_MUSIC = pygame.mixer.Sound("assets\sounds\\bg_music.mp3")
BG_MUSIC.set_volume(0.2)
BG_MUSIC.play(loops=-1)


# Main function
def main():
    clock = pygame.time.Clock()
    running = True
    paused = False
    displayed_planet = None
    time_passed = 0
    pause_text = ""
    muted = False

    while running:
        clock.tick(60)

        # Handle events
        for event in pygame.event.get():
            # If user quits it breaks out of the loop
            if event.type == pygame.QUIT:
                running = False

            # Handle key presses
            if event.type == pygame.KEYDOWN:
                # If P is pressed pause/unpause
                if event.key == pygame.K_p:
                    if paused:
                        paused = False
                    elif not paused:
                        paused = True
                        pause_text = PAUSE_FONT.render("PAUSED", 1, (255, 255, 255))
                        win.blit(pause_text, (WIDTH / 2 - pause_text.get_width() / 2, 20))
                        pygame.display.update()
                                    
                # Check if user pressed the keys 1-8
                if pygame.K_0 <= event.key <= pygame.K_8:
                    # Shift it by 48 to the lef tomatch their original indexes 
                    # (K_0 ASCII value is 48, planets start from index 0, hence minus 48)
                    planet_index = event.key - pygame.K_0 # 48
                    displayed_planet = planet_list[planet_index]

                # Toggle info text off if displayed
                if event.key == pygame.K_i:
                    if displayed_planet:
                        displayed_planet = None

                # Quit program when Q is pressed
                if event.key == pygame.K_q:
                    running = False

                # Mute background music when M is pressed
                if event.key == pygame.K_m:
                    if muted:
                        BG_MUSIC.set_volume(0.3)
                        muted = False
                    elif not muted:
                        BG_MUSIC.set_volume(0)
                        muted = True

            # Toggle information off with mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if displayed_planet:
                    displayed_planet = None
        
        # Calculate gravitational forces exerted on planets
        if not paused:
            # Keep track of the time passed since start of the simulation to be displayed later
            time_passed += planet_list[0].TIMESTEP

            # Calculate force for each of the planets and move them in their orbit
            for planet in planet_list:
                planet.calculate_gravitational_force(planet_list)

            # Fill the window before drawing the planets to avoid flickering
            win.fill((0, 0, 0))

            # Draw planets
            for planet in planet_list:
                x, y = planet.draw_planet()
                pygame.draw.circle(win, planet.color, (x, y), planet.radius)

        # Draw legend to the top right corner of the screen
        text_x = WIDTH - 105
        text_y = 20
        for legend_text in LEGEND_TEXTS:
            # Differentiate with color if any celestial body is selected
            if displayed_planet:
                if displayed_planet.name.capitalize() in legend_text:
                    text = FONT.render(legend_text, 1, displayed_planet.color)
                else:
                    text = FONT.render(legend_text, 1, (255, 255, 255))
                win.blit(text, (text_x, text_y))
                text_y += 30
            else:
                text = FONT.render(legend_text, 1, (255, 255, 255))
                win.blit(text, (text_x, text_y))
                text_y += 30

        # User can also display info texts by hovering mouse on planets
        for planet in planet_list:
            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Get distance between mouse and the planet (scaled down)
            distance = math.sqrt((planet.x * planet.SCALE + 1920 / 2 - mouse_x) ** 2 + (planet.y * planet.SCALE + 1080 / 2 - mouse_y) ** 2)
            if distance <= planet.radius and not paused:
                idx = planet_list.index(planet)
                displayed_planet = planet_list[idx]

        # If one of 1-8 keys is pressed information text is blitted
        if displayed_planet:
            if displayed_planet.name != "Sun":
                # Set variables to be shown
                days_passed = time_passed / (3600 * 24)
                days_left = int(displayed_planet.orbit_time - days_passed)
                velocity = math.sqrt(displayed_planet.x_vel ** 2 + displayed_planet.y_vel ** 2) / 1000
                distance_to_sun = displayed_planet.distance_to_sun / 1000
                days_left_for_full_orbit = days_left % displayed_planet.orbit_time
                years_passed_since_start = days_passed / displayed_planet.orbit_time

                # Blit the info text to the top left corner of the screen
                planet_info_text_1 = FONT.render(f"{displayed_planet.name}", 1, displayed_planet.color)
                planet_info_text_2 = FONT.render(
                    f"Mass: {displayed_planet.mass} kg\n"
                    f"Radius: {displayed_planet.actual_radius:,} km\n"
                    f"Gravity: {displayed_planet.gravity} m/s^2\n"
                    f"Mean Temperature: {displayed_planet.mean_temp} °C\n"
                    f"Velocity: {velocity:.1f} km/s\n"
                    f"Distance to Sun: {distance_to_sun:,.1f} km\n"
                    f"Days left for one full orbit: {days_left_for_full_orbit} days\n"
                    f"Time passed since start: {years_passed_since_start:.2f} {displayed_planet.name} years\n"
                    "Symbol: ",
                    1,
                    (255, 255, 255)
                )
                source_text = FONT.render("Source: NASA", 1, (255, 255, 255))
                win.blit(planet_info_text_1, (10, 20))
                win.blit(planet_info_text_2, (10, 40))
                # Blit image to the bottom left corner of the screen
                win.blit(source_text, (10, HEIGHT - 20))
                win.blit(pygame.transform.scale(pygame.image.load(f"assets\images\planets\\{displayed_planet.name.lower()}.jpg"), (250, 250)), 
                         (0, HEIGHT - 270))
                # Blit astronomical symbol of the planet as an image
                win.blit(pygame.image.load(f"assets\images\symbols\\{displayed_planet.name.lower()}.jpg"), (85, planet_info_text_2.get_height() + 20))

            # Info text for Sun
            elif displayed_planet.name == "Sun":
                days_passed = int(time_passed / (3600 * 24))
                sun = displayed_planet
                sun_info_text_1 = FONT.render("Sun", 1, sun.color)
                sun_info_text_2 = FONT.render(
                    f"Mass: {sun.mass} kg\n"
                    f"Radius: {sun.actual_radius:,} km\n"
                    f"Gravity (Surface): {sun.gravity} m/s^2\n"
                    f"Mean Temperature (Surface): {sun.mean_temp} °C\n"
                    f"Time passed since start: {days_passed} Sun days\n"
                    "Symbol: ",
                    1,
                    (255, 255, 255)
                )
                source_text = FONT.render("Source: NASA", 1, (255, 255, 255))
                win.blit(sun_info_text_1, (10, 20))
                win.blit(sun_info_text_2, (10, 40))
                # Blit Sun image to the bottom left corner of the screen
                win.blit(source_text, (10, HEIGHT - 20))
                win.blit(pygame.transform.scale(pygame.image.load("assets\images\planets\\sun.jpg"), (250, 250)), (0, HEIGHT - 270))
                # Blit astronomical symbol of Sun as an image
                win.blit(pygame.image.load("assets\images\symbols\\sun.jpg"), (85, sun_info_text_2.get_height() + 20))

            # Draw a little circle around the planet to indicate it is selected
            # Get planet's coordinates to the scale
            x = int(displayed_planet.x * displayed_planet.SCALE + 1920 / 2)
            y = int(displayed_planet.y * displayed_planet.SCALE + 1080 / 2)
            pygame.draw.circle(win, (255, 255, 255), (x, y), displayed_planet.radius + 5, width=1)

            # Draw selected planet's orbit when it is selected
            # Orbit will be shown as a regular circle whose radius is changed with the planet's distance to the Sun
            current_x_distance = (displayed_planet.x - planet_list[0].x)
            current_y_distance = (displayed_planet.y - planet_list[0].y)
            center_x = int(planet_list[0].x * displayed_planet.SCALE + 1920 / 2)
            center_y = int(planet_list[0].y * displayed_planet.SCALE + 1080 / 2)
            current_distance = math.sqrt(current_x_distance ** 2 + current_y_distance ** 2) * displayed_planet.SCALE
            pygame.draw.circle(win, displayed_planet.color, (center_x, center_y), current_distance, width=1)

            # If Uranus or Neptune gets out of the screen user is informed
            if displayed_planet.name == "Neptune":
                neptune = displayed_planet
                neptune_out_up = neptune.y * neptune.SCALE + 1080 / 2 < 0
                neptune_out_down = neptune.y * neptune.SCALE + 1080 / 2 > 1080
                if neptune_out_up or neptune_out_down:
                    text = FONT.render("Neptune is out of screen now", 1, neptune.color)
                    win.blit(text, (10, planet_info_text_2.get_height() + 40))
                    if neptune_out_up:
                        line_start = (WIDTH / 2, 50)
                        line_end = (neptune.x * neptune.SCALE + 1920 / 2, neptune.y * neptune.SCALE + 1080 / 2)
                        neptune_indicator = FONT.render("Neptune", 1, (255, 255, 255))
                        pygame.draw.line(win, (255, 255, 255), line_start, line_end) 
                        win.blit(neptune_indicator, (line_start[0] - neptune_indicator.get_width() / 2, line_start[1] + 20))
                    elif neptune_out_down:
                        line_start = (WIDTH / 2, HEIGHT - 50)
                        line_end = (neptune.x * neptune.SCALE + 1920 / 2, neptune.y * neptune.SCALE + 1080 / 2)
                        neptune_indicator = FONT.render("Neptune", 1, (255, 255, 255))
                        pygame.draw.line(win, (255, 255, 255), line_start, line_end)
                        win.blit(neptune_indicator, (line_start[0] - neptune_indicator.get_width() / 2, line_start[1] - 20))
            elif displayed_planet.name == "Uranus":
                uranus = displayed_planet
                uranus_out_up = uranus.y * uranus.SCALE + 1080 / 2 < 0
                uranus_out_down = uranus.y * uranus.SCALE + 1080 / 2 > 1080 
                if uranus_out_up or uranus_out_down:
                    text = FONT.render("Uranus is out of screen now", 1, uranus.color)
                    win.blit(text, (10, planet_info_text_2.get_height() + 40))
                    if uranus_out_up:
                        line_start = (WIDTH / 2, 50)
                        line_end = (uranus.x * uranus.SCALE + 1920 / 2, uranus.y * uranus.SCALE + 1080 / 2)
                        uranus_indicator = FONT.render("Uranus", 1, (255, 255, 255))
                        pygame.draw.line(win, (255, 255, 255), line_start, line_end)
                        win.blit(uranus_indicator, (line_start[0] - neptune_indicator.get_width() / 2, line_start[1] + 20))
                    elif uranus_out_down:
                        line_start = (WIDTH / 2, HEIGHT - 50)
                        line_end = (uranus.x * uranus.SCALE + 1920 / 2, uranus.y * uranus.SCALE + 1080 / 2)
                        uranus_indicator = FONT.render("Uranus", 1, (255, 255, 255))
                        pygame.draw.line(win, (255, 255, 255), line_start, line_end)
                        win.blit(uranus_indicator, (line_start[0] - uranus_indicator.get_width() / 2, line_start[1] - 20))

        if not paused:
            # Display scale info to the bottom right corner of the screen
            scale_info_text = FONT.render("Distances are to scale, sizes are not to scale.", 1, (255, 255, 255))
            win.blit(scale_info_text, (WIDTH - scale_info_text.get_width(), HEIGHT - scale_info_text.get_height()))
        
            pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()