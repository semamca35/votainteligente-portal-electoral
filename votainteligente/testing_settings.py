import os
## TESTING ENVIRONMENT
LOCAL_ELASTICSEARCH = True
CELERY_ALWAYS_EAGER = True
TRAVIS = os.environ.get('TRAVIS')
CACHES={'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}}
MEREPRESENTA_VOLUNTARIOS_ON = True

if TRAVIS:
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'votainteligente_test',
        },
    }
    DB = os.environ.get('DB')

    if DB == 'postgres':
        default_db = {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travis_ci_test',
            # The following settings are not used with sqlite3:
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '',
            }
    else:
        default_db = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'writeit.db',                      # Or path to database file if using sqlite3.
            }

    DATABASES = {'default': default_db}
