DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'polymorphic',
    'time_wizard',
)

SECRET_KEY = 'foobar1337'

TIME_WIZARD_COUNTRIES = ['US']

TIME_WIZARD_COUNTRY_PROVINCES = {'US': ['AL']}
