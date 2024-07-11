echo "BUILD START"
source  my_env/Scripts/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
echo "BUILD END"

