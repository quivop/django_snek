# django_snek
Fooling around with django tutorial, only instead of a **polls** app, I made a **fic** one. 

## Tutorial link

Currently working off of the [polls tutorial in the official Django docs](https://docs.djangoproject.com/en/2.0/intro/tutorial01/). About to start on [part 3](https://docs.djangoproject.com/en/2.0/intro/tutorial03/).

### What I've done so far:
- Modified base site
  - changed timezone
  - changed database name
  - run initial db migration
  - setup urls.py to point to `fic` and `admin`
- Added `fic` app
  - added `Fanfic` and `Link` models
  - registered above models in admin.py
  - added a simple `index` view
  - pointed to `index` view in fic\urls.py
  - run initial db migrations that include the new models
  - added a little test data via django's db api

## To Do

- [x] add modified django install files to repo
- [x] make quick list of important stuff I've already done as part of the tutorial
- [ ] include admin user details
