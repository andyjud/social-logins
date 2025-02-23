#### Commands
##### Set up:
git clone https://github.com/andyjud/django-starter.git . && rm -rf .git <br/>
python3 -m venv venv <br/>
source venv/bin/activate <br/>
pip install --upgrade pip <br/>
pip install -r requirements.txt <br/>
python manage.py migrate <br/>
python manage.py createsuperuser <br/>
python manage.py runserver <br/>
ctrl + c <br/>

##### Sociallogin:
pip install "django-allauth[socialaccount]"<br/>
pip install django-environ<br/>
<br/>

##### Callback URI:
http://localhost:8000/accounts/google/login/callback/<br/>


