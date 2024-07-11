echo "BUILD START"
my_env/Scripts/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
echo "BUILD END"

# [optional] Start the application here 
# python manage.py runserver