# AnimeOasis
Welcome to AnimeOasis, your ultimate destination for all things anime! 🌟 Immerse yourself in a captivating world where you can stream, research, and engage in vibrant discussions about your favorite anime series.

## Backend Setup
1. Navigate to the folder where you would like to store this project, and run the following CLI command to clone this repository into it:
   ```
   git clone https://github.com/DomenikMoody/AnimeOasis.git
   ```
2. From the directory where you ran `git clone`, navigate to the backend folder:
   ```
    cd AnimeOasis/AnimeOasis/backend
   ```
3. Launch a virtual shell environment and install the pipfile dependencies by running the following CLI commands:
   ```
   pipenv shell
   pipenv install
   ```
   NOTE: The [pipenv](https://pipenv.pypa.io/en/latest/) command requires both [pip](https://pip.pypa.io/en/stable/) and [virtualenv](https://virtualenv.pypa.io/en/latest/) to be installed on your machine. 
4. If you need to make changes to the database models, after doing so you must generate a new migration file:
   ```
   python manage.py makemigrations app
   ```
   To apply the latest migration to your database, run:
   ```
   python manage.py migrate
   ```
5. Start the backend server with the following command:
   ```
   python manage.py runserver
   ```
   NOTE: By default, Django runs on port 8000; specify a port number after `runserver` to override this behavior.

