=============
Menu Resolver
=============

MenuResolver is a simple Django aplication to create and insert menues in a template


Quick start
-----------

Add 'menuresolver' to your INSTALLED_APPS

INSTALLED_APPS = (
	....
	'menuresolver',
)

Register it in the admin page and let's create your own menues.


Add into your template '{% load menuresolver_tags %}' and '{% create_menu [slug_of_menu] %}' to render.
