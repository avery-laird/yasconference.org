
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "0c6d746d-b03f-4836-9aaf-3bba54fe034506874592-ee3b-4aca-a295-9bd4e2d1abbc04f82621-847a-4c93-8cb4-06d800a9c342"
NEVERCACHE_KEY = "23804df4-72ee-4e57-b49a-16f6a0c82f894538bb46-6056-4d6d-aa10-1dee2d875905fe304b0c-3463-4059-bdc1-78b8e08355c3"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
