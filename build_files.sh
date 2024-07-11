echo "BUILD START"
pip install virtualenv
source  my_env/Scripts/activate
cd Ecommerce
pip install -r requirements.txt
python manage.py collectstatic --noinput
echo "BUILD END"

