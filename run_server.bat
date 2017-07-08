@ECHO off

CALL deactivate
CALL activate webapp
ECHO Activated Env

ECHO Starting Server

python manage.py runserver 0.0.0.0:8000

EXIT