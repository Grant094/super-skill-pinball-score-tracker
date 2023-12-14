# super-skill-pinball-score-tracker
Tracking my scores recorded in the Super Skill Pinball games.

These games are made by [WizKids](https://wizkids.com/) and you can see more info about the Super Skill Pinball games at:
- [Super-Skill Pinball: 4-Cade](https://shop.wizkids.com/products/pre-order-super-skill-pinball-4-cade)
- [Star Trek: Super Skill Pinball](https://shop.wizkids.com/products/star-trek-super-skill-pinball)
- [Super-Skill Pinball: Ramp It Up!](https://shop.wizkids.com/products/super-skill-pinball-ramp-it-up)

This app is in no way affiliated with WizKids or the Super-Skill Pinball brand.

# Tech
- HTML
- Python
- Django
- JavaScript
- React.js

# Quickstart
- Install Python on your computer, possibly via https://www.python.org/downloads/
- Open a terminal and be at `super-skill-pinball-score-tracker/sspscoretrackersite/`
- Create a virtual environment by running `python -m venv venv`
- Activate the virtual environment:
    - On Windows, execute the file `venv/Scripts/activate`
    - On Unix or MacOS, execute the file `venv/bin/activate`
- Install Django: `python -m pip install Django`
- Setup Database by running `python manage.py migrate`
- Run server: `python manage.py runserver`
- Visit https://localhost:8000/ to see the homepage!
