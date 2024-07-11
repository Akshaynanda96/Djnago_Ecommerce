echo "BUILD START"
python3.12 -m pip install virtualenv
python3.12 -m venv my_env
my_env/Scripts/activate
cd Ecommerce
python3.12 -m pip install Django
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput
echo "BUILD END"

