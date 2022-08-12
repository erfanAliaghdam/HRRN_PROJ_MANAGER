# HRRN based process manager


this proj is for interview:
used HRRN formula to calculate the process manager's priority
HRRN formula:
>(duration in seconds + waiting time in seconds) / duration in seconds







use this structure for .env file inside root:

jwt token validation in days: 

> ACCESS_TOKEN_LIFETIME_BY_DAYS = 10

jwt refresh token validation :

> REFRESH_TOKEN_LIFETIME_BY_DAYS = 11

db config : 

> ENGINE = 'django.db.backends.postgresql'

> NAME = 'postgres'

> USER = 'postgres'

> PASSWORD = 'postgres'

> HOST = 'postgres'

> PORT = '5432'

secret key, you can use https://djecrety.ir website:

> SECRET_KEY = ''



Command to run the project:
> python manage.py runserver

Command for running process manager script:
> python manage.py runscript process_manager

now you can login with jwt and make process with this endpoint :
> http://localhost:8000/api/process

you can see progress of each process in admin panel :
> http://127.0.0.1:8000/admin/processManager/process/