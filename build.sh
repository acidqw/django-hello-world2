python3.9 -m venv venv

source venv/bin/activate
pip install -r requirements.txt

python3.9 manage.py collectstatic --no-input --clear
# python3 manage.py runserver
