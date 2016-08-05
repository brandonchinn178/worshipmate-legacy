Worship Song Database
=====================

A Django-powered website hosted on Openshift that centralizes a collection of worship songs, for use by worship leaders in choosing worship sets. This website allows users to easily filter songs by category, search songs by lyrics, and download song sheets.

The website also features a custom administrative interface that allows admins to easily add songs and themes to the database. Everytime a song is added to the database, the Facebook page will also automatically write a post announcing the addition of the song.

Installation
============

1. Clone this repo
1. Install [conda](http://conda.pydata.org/docs/install/quick.html)
1. `conda env create` to set up the environment
1. Get the `.env` file
1. `source activate_environment` to activate the environment
1. `python site/manage.py runserver` and go to `localhost:8000` to see the site
