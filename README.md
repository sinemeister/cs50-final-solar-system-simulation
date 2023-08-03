# Solar System Simulation

![Language](https://img.shields.io/badge/language-python-blue)
![Module](https://img.shields.io/badge/module-pygame-orange)

## About

This project is developed as final project for Harvard University's CS50x Introduction to Computer Science Course, in August 2023.

It is a simple solar system simulation using **Python**'s **Pygame** module, using **Newton's second law of motion** and **Newton's law of universal gravitation** with actual properties of the celestial bodies (only Sun and the planets).

Main idea of the project is inspired from <a href="https://www.youtube.com/@TechWithTim">Tech With Tim</a>'s <a href="https://www.youtube.com/watch?v=WTLPmUHTPqo"><i>Planet Simulation In Python - Tutorial</i></a> video, which I have watched while I was trying to learn **Pygame** module before I enrolled in CS50x. I have added various features and applied it to the full scale of Solar System, using the same calculations, which are **Newton's universal laws**, as stated above.

**You may find the video demo of the project <a href="https://www.youtube.com/watch?v=n77mRVHwe5w">here</a>.**

## Features & Implementation

- Distances are to scale, sizes are not to scale.
- Calculations are done regarding Newton's laws with actual properties of the celestial bodies (Retrieved from <a href="https://nssdc.gsfc.nasa.gov/planetary/factsheet/">NASA's fact sheets</a>)
- Dynamically shown celestial body information (by selecting desired celestial body with keyboard or hovering mouse at desired instance)
- Dynamically colored indicators to show user that particular celestial body is selected
- Dynamically updating orbital velocities and orbits (not to forget that orbital velocities and orbits are just fine approximations as moons and other celestial bodies are excluded in this simulation)
- Ambient background music
- Ability to pause/unpause the simulation
- Ability to toggle on/off celestial body information (refer above)
- Ability to mute/unmute the background music
- Ability to quit the simulation any time by pressing Q as screen borders may be invisible depending user's display resolution
- As Uranus' and Neptune's orbits may sometimes be out of the screen, an arrow indicating current position of the related planet is drawn for user to be able to keep track of the planet

<center>
<div>
    <img src="https://i.imgur.com/MVt0M5c.png" width="360" height="240"/>
    <img src="https://i.imgur.com/9vjm11h.png" width="360" height="240"/>
</div>
</center>
<center>
<div>
    <img src="https://i.imgur.com/Odld53q.png" width="360" height="240"/>
    <img src="https://i.imgflip.com/7ulnl2.gif" width="360" height="240/">
</div>
</center>

## Instructions on Usage

- Make sure that all the files are in the same folder, e.g. ```project```
- Change your directory to the folder you keep the files, e.g. ```cd path\project```
- Install dependencies from the ```requirements.txt``` by executing ```pip install -r requirements.txt``` at your IDE's terminal (or command prompt). This will successfully install **Pygame**.
- Start the program at your IDE's terminal (or command prompt) by executing ```python main.py```

You may find the shortcuts useful:

| Key      | Function                                                  |
| ---------| ----------------------------------------------------------|
| P        | Pause / Unpause simulation                                |
| M        | Mute / Unmute background music                            |
| I        | Toggle information off (when on)                          |
| Q        | Quit simulation                                           |
| 0-8      | Display celestial body information (Sun to Neptune)       |
| MOUSE 1  | Toggle information off (when on)                          |

## Assets Used

All assets used in this project are copyright-free. 

- Background music is retrieved from <a href="https://pixabay.com/">Pixabay</a>. Credit to: **SamuelFrancisJohnson**. You may find it <a href="https://pixabay.com/sound-effects/superspacy-atmosphere-106826/">here</a>.
- Celestial bodies' images that appear on bottom-left corner are retrieved from <a href="https://images.nasa.gov/">NASA</a>.
- Celestial bodies' astronomical symbol images are retrieved from <a href="https://en.wikipedia.org">Wikipedia</a> under <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">Creative Commons License</a>. Find particular images: <a href="https://en.wikipedia.org/wiki/File:Sun_symbol_(fixed_width).svg">Sun</a>, <a href="https://en.wikipedia.org/wiki/File:Mercury_symbol_(fixed_width).svg">Mercury</a>, <a href="https://en.wikipedia.org/wiki/File:Venus_symbol_(fixed_width).svg">Venus</a>, <a href="https://en.wikipedia.org/wiki/File:Globus_cruciger_(fixed_width).svg">Earth</a>, <a href="https://en.wikipedia.org/wiki/File:Mars_symbol_(fixed_width).svg">Mars</a>, <a href="https://en.wikipedia.org/wiki/File:Jupiter_symbol_(fixed_width).svg">Jupiter</a>, <a href="https://en.wikipedia.org/wiki/File:Saturn_symbol_(fixed_width).svg">Saturn</a>, <a href="https://en.wikipedia.org/wiki/File:Uranus_symbol_(fixed_width).svg">Uranus</a>, <a href="https://en.wikipedia.org/wiki/File:Neptune_symbol_(fixed_width).svg">Neptune</a>. Converted to JPG and edited on MS Paint for black background - white foreground change.

## Misc

This project is developed solely by myself as a final project for Harvard University's <a href="https://cs50.harvard.edu/x/2023/">CS50x Introduction to Computer Science Course</a>. I have no commercial or monetary purposes. This is developed only for educational purposes.

Special thanks to Harvard University, Prof. David J. Malan, and the staff!

## Contact

Many thanks for checking this project and trying the simulation. Your interest is very much appreciated.

Please do not hesitate to contact me if you have questions regarding the project or any other related subject. Mail me <a href="mailto:leventpolat408@gmail.com">here</a>.
