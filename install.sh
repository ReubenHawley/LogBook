pip install django
$env:SECRET_KEY=$(python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())')
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser