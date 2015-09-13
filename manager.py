import argparse
import sys
import os.path
import glob

CONTROLLERS_FORMAT = """# -*- coding: utf-8 -*-

from project import app
from bottle import template, request
"""

MODELS_FORMAT = """
class {}(object):
	
	def __init__(self):
		pass
	
	def create(self):
		pass
	
	def read(self):
		pass
	
	def update(self):
		pass
	
	def delete(self):
		pass
	
	def all(self):
		pass
"""

VIEWS_FORMAT = """% rebase('{}.tpl')
<!-- do some thing -->
"""

VIEW_BASE_FORMAT = """
<html>
<head>
	<title>Welcome</title>
	<link rel='stylesheet' type='text/css' href='/bootstrap/css/bootstrap.min.css'/>
</head>
<body>
	<div class='container'>
		<div class="page-header">
			<h1>
				<span class="glyphicon glyphicon-equalizer" aria-hidden="true"></span>
				Your Big Title 
				<small>Your Small Title</small></h1>
		</div>
		{{!base}}
	</div>
	<script src='/bootstrap/js/jquery.min.js'></script>
	<script src='/bootstrap/js/bootstrap.js'></script>
</body>
</html>
"""

def initial(args=None):
	parser = argparse.ArgumentParser(description='Bottleck Manager [Create By: _YanwarSolahudin]')
	parser.add_argument('-c', '--controller', help='create controller')
	parser.add_argument('-m', '--model', help='create model')
	parser.add_argument('-v', '--view', help='create view')
	parser.add_argument('-b', '--viewbase', help='create view base')
	parser.add_argument('-a', '--showall', help='show all your controllers, models and views')
	parser.add_argument('-s', '--serve', help='running server, ex manager.py localhost@8080')
	
	results = parser.parse_args(args)
	
	return(results.controller, results.model, 
		results.view, results.viewbase, 
		results.showall, results.serve
	)


def create_controller(c):
	path = 'project/controllers/{}.py'.format(c)
	global CONTROLLERS_FORMAT
	if not os.path.isfile(path):
		with open(path, 'w') as file_controller:
			data = file_controller.write(CONTROLLERS_FORMAT)
		return True
	else:
		return False


def create_model(m):
	path = 'project/models/{}.py'.format(m.title())
	global MODELS_FORMAT
	if not os.path.isfile(path):
		with open(path, 'w') as file_model:
			data = file_model.write(MODELS_FORMAT.format(m.title()))
		return True
	else:
		return False


def create_view(v):
	path = 'project/views/{}.tpl'.format(v)
	global VIEWS_FORMAT
	if not os.path.isfile(path):
		with open(path, 'w') as file_view:
			data = file_view.write(VIEWS_FORMAT.format(v))
		return True
	else:
		return False


def create_view_base(b):
	path = 'project/views/{}.tpl'.format(b)
	global VIEW_BASE_FORMAT
	if not os.path.isfile(path):
		with open(path, 'w') as file_view_base:
			data = file_view_base.write(VIEWS_FORMAT.format(b))
		return True
	else:
		return False


def show_all_controllers():
	path = 'project/controllers/*.py'
	controllers = glob.glob(path)
	data = []
	filter_controllers = ['project/controllers/static.py', 
		'project/controllers/welcome.py', 'project/controllers/__init__.py'
	]
	if controllers:
		for controller in controllers:
			if controller not in filter_controllers:
				data.append(controller)
		return data
	else:
		return False


def show_all_models():
	path = 'project/models/*.py'
	models = glob.glob(path)
	data = []
	filter_models = ['project/models/__init__.py', 'project/models/Employees.py']
	if models:
		for model in models:
			if model not in filter_models:
				data.append(model)
		return data
	else:
		return False

def show_all_views():
	path = 'project/views/*.tpl'
	views = glob.glob(path)
	if views:
		return views
	else:
		return False
	

if __name__ == '__main__':
	c, m, v, b, a, s = initial(sys.argv[1:])
	if c:
		if create_controller(c):
			print("+ success create controller '{}'".format(c))
		else:
			print("- controller '{}' already to use.".format(c))
	
	if m:
		if create_model(m):
			print("+ success create models '{}'".format(m.title()))
		else:
			print("- models '{}' already to use.".format(m.title()))
	
	if v:
		if create_view(v):
			print("+ success create view '{}'".format(v))
		else:
			print("- view '{}' already to use.".format(c))
		
	if b:
		if create_view_base(b):
			print("+ success create base view '{}'".format(b))
		else:
			print("- base view '{}' already to use.".format(b))
	
	
	# show all 
	if a == "all":
		data = show_all_controllers()
		if data:
			print(" ")
			print("Your Controllers ({}): ".format(len(data)))
			print("------------------")
			for i in data:
				print("+ {} | {}".format("[PY]",i.replace('.py','')))
		else:
			print("- You have not yet created controllers file")
		
		data = show_all_models()
		if data:
			print(" ")
			print("Your Models ({}): ".format(len(data)))
			print("------------------")
			for i in data:
				print("+ {} | {}".format("[PY]",i.replace('.py','')))
		else:
			print("- You have not yet created models file")
		
		data = show_all_views()
		
		if data:
			print(" ")
			print("Your Views ({}): ".format(len(data)))
			print("------------------")
			for i in data:
				print("+ {} | {}".format("[TPL]",i.replace('.tpl','')))
		else:
			print("- You have not yet created views file")
	
	# run server
	if s:
		if "@" in s:
			import run
			host = s.split('@')[0]
			port = s.split('@')[1]
			if port.isnumeric():
				run.running(host, port)
			else:
				print("- Pport number is invalid.")
		else:
			print("can not run server")
		
