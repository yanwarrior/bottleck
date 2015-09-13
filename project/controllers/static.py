# -*- coding: utf-8 -*-
from project import app
from bottle import static_file
from project.config import static
from project.config import routing

# Static for css
@app.route(routing.ROUTES['static_bootstrap_css'])
def serve_css(filename):
	return static_file(filename, static.CSS_PATH)

# Static for js
@app.route(routing.ROUTES['static_bootstrap_js'])
def serve_js(filename):
	return static_file(filename, static.JS_PATH)

# Static for fonts
@app.route(routing.ROUTES['static_bootstrap_fonts'])
def serve_font(filename):
	return static_file(filename, static.FONTS_PATH)

# Static for media images
@app.route(routing.ROUTES['static_media_images'])
def serve_images(filename):
	return static_file(filename, static.IMAGES_PATH)

# Static for media thumbs
@app.route(routing.ROUTES['static_media_thumbs'])
def serve_thumbs(filename):
	return static_file(filename, static.THUMBS_PATH)

# Static for media other
@app.route(routing.ROUTES['static_media_other'])
def serve_other(filename):
	return static_file(filename, static.OTHER_PATH)

