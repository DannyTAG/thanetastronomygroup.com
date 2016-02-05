=====
ThanetAstronomyGroup.com
=====

This is the (soon to be) source code to ThanetAstronomyGroup.com, we're powered by Python and Django andMezzanine. Feel free to fix bugs or make improvements, or use this code for your own projects :)

Quick start
-----------

1. Clone this repository using `git clone https://github.com/Azelphur/thanetastronomygroup.com.git`

2. Create a virtual environment with `virtualenv env` and activate it `with source env/bin/activate`

3. Install the requirements with pip install -r requirements.txt

4. Copy thanetastronomygroup/local_settings.py.example to thanetastronomygroup/local_settings.py

5. Run `python manage.py migrate` to create the models

6. Start the development server with `python manage.py runserver`
   and visit http://127.0.0.1:8000/

7. (optional) run `python manage.py createsuperuser` to create an admin account
