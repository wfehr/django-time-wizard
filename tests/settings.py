HELPER_SETTINGS = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        },
    },
    'INSTALLED_APPS': (
        'polymorphic',
        'time_wizard',
    ),
    'SECRET_KEY': 'foobar1337',
    'TIME_WIZARD_COUNTRIES': ['US'],
    'TIME_WIZARD_COUNTRY_PROVINCES': {'US': ['AL']},
}


def run():
    from app_helper import runner
    runner.run('time_wizard')


if __name__ == '__main__':
    run()
