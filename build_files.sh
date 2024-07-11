#!/bin/bash

echo "BUILD START"

# Activate the virtual environment
source my_env/Scripts/activate

# Ensure pip and Python are accessible
pip install -r requirements.txt
python manage.py collectstatic --noinput

# Verify the staticfiles_build directory
if [ ! -d "staticfiles_build" ]; then
    echo "Error: No Output Directory named 'staticfiles_build' found after the Build completed."
    echo "You can configure the Output Directory in your Project Settings."
    exit 1
fi

echo "BUILD END"

# Optionally, start the application
# python manage.py runserver
