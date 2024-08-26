To start project for the first time on your local machine, you need to follow the following steps:
1. Clone the repository to your local machine.
2. CD into the group directory -> cd $\Moffat-Bay
3. Create a virtual environment -> python -m venv venv
4. Activate the virtual environment -> venv\Scripts\activate
    -If on a Mac, use the following command -> source venv/bin/activate
5. Install Django -> pip install django
    -There may be more dependencies that need to be installed, especially as we continue to progress with the project. Please install them as needed via -> pip install <dependency>
6. CD into the project directory -> cd MoffatBayDjango
7. Migration -> python manage.py migrate
8. Run the server -> python manage.py runserver

Server will start and you can access the project on your local machine via a local host address.

Any time after the first time to start the project:
1. CD into the group directory -> cd $\Moffat-Bay
2. Activate the virtual environment -> venv\Scripts\activate
    -If on a Mac, use the following command -> source venv/bin/activate
3. CD into the project directory -> cd MoffatBayDjango
4. Run the server -> python manage.py runserver
    -Again, there may be more dependencies that need to be installed. Install them as needed via -> pip install <dependency>

If there are any questions, please contact me and I will get back to you asap - John Garcia