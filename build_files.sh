echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv my_env

# activate the virtual environment
source my_env/Scripts/activate

# install all deps in the venv
pip install -r requirements.txt

# collect static files using the Python interpreter from venv
python manage.py collectstatic --noinput

echo "BUILD END"

# [optional] Start the application here 
# python manage.py runserver