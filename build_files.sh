echo "BUILD START"
python -m pip install Django
python -m pip install virtualenv
python -m venv my_env
source  my_env/Scripts/activate
cd Ecommerce
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput
echo "BUILD END"

