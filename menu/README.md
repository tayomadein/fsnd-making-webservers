# FSND Project: Restaurants and Menus
#### by Omotayo Madein

## Description

This is a project for [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). The Restaurant Menu project focuses on testing and improving my skills in Creating Webservers, Performing CRUD Operations, Routing, Creating API endpoints and rendering the output via HTML templates using the Flask Framework and SQLAlchemy while applying Iterative Development principles. 

## Project contents

The required files/folders for this project to run include:

* static/ - contains the necessary css files and media files.
* templates/ - contains HTML templates for pages.
* database_setup.py - Script to setup DB for our restaurants
* populate_db.py - Script to populate our Restaurant DB with dummy data
* finalproject.py - Main script that holds all the necessary information for our webserver and website to run

## Requirements
* Vagrant
* VirtualBox

## How to run

* Step 0:

Clone this repo to your desktop
```
git clone https://github.com/tayomadein/restaurant-menu.git
```
___or___
Download this repo as a zipped file from [Github](https://github.com/tayomadein/restaurant-menu/archive/master.zip)

* Step 1: 

Setup your virtual environment by following these [instructions](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)

* Step 2:

Move your copy of the repo to your shared virtual environment folder `/vagrant/restaurant-menu` 

* Step 3:

Switch to your virtual environment folder `/vagrant` in the terminal. Then start up your virtual environment by running these commands
```
$ vagrant up
$ vagrant ssh
```

* Step 4:

Fireup your webserver by switching into your shared folder from terminal `cd /vagrant/restaurant-menu`, then run this command

```
python finalproject.py
``` 

* Step 5:

Open your favorite browser and go to `http://localhost:5000/` or `http://0.0.0.0:5000/`

**Notes:**
* If your webserver is running properly, you can visit the following URLs:

- `/` and `/restaurants` - Home page that shows a list of all restaurants
- `/restaurant/new` - Page for creating new restaurants
- `/restaurant/restaurant_id/edit` - Page to edit the info of a restaurant
- `/restaurant/restaurant_id/delete` - Page to delete a restaurant
- `/restaurant/restaurant_id` and `/restaurant/restaurant_id/menu` - Page that displays a restaurant's menu
- `/restaurant/restaurant_id/menu/new` - Page to create a new menu item
- `/restaurant/restaurant_id/menu/menu_id/edit` - Page to edit info of a menu item
- `/restaurant/restaurant_id/menu/menu_id/delete` - Page to delete a menu item
- `/restaurants/JSON/` - API Endpoint for all restaurants
- `/restaurants/restaurant_id/menu/JSON/` - API Endpoint for a restaurant's menu
- `/restaurants/restaurant_id/menu/menu_id/JSON/` - API Enpoint for a menu item

* PS: Replace `restaurant_id` and the `menu_id` with their respective ID numbers.
