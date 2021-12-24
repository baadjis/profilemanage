# Profilemanage

A simple login register system and profile editing app built with django and bootsrap

## Usage:

### install

clone the repository 

build the image 

The makefile file contains docker commands shortands



### to build the image

  go to the root folder and run 

   `` make build ``

### To start the server


run:   

 ``  make up ``

if you want docker to run on background


 run:  
 
 `` make upd ``

 



### To create a superuser


run:


`` docker-compose run --rm web python manage.py createsuperuser``



### Login and registration


once the server is launched  
connect to :

http://127.0.0.1:8000/


you will be on homepage

Then you can register or login if you 

are already registered



### Profile edit

once successfuly loged, your profile page will appear

click on edit button to modify your 

email and also your bio (make sure it take at least ten characters)

