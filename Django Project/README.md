# Create a user
After the first installation you have to create the admin user.

locally:
`python3 manage.py createsuperuser`

via Docker compose:
`docker compose run app python3 manage.py createsuperuser`

# Apply migrations 
locally:
`docker compose run app python manage.py migrate`

via Docker compose:
`python manage.py migrate`

# Create migrations
locally:
`docker compose run app python manage.py migrate`

via Docker compose:
`python manage.py migrate`