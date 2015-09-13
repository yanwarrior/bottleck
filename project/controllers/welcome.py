# -*- coding: utf-8 -*-
from project import app
from project.models import Employees as emps
from bottle import template, request

@app.route('/', method='GET')
def index():
	svg_file = '/media/other/bechmark_result.svg'
	employees = emps.Employees()
	employees.add(
		'90AS', 'Lenya', 'Engineer', 'lenya@mail.com', 44
	)
	employees = employees.get_all_employees()
	return template('welcome', message='Welcome To Bottle MVC', svg_data=svg_file, employees=employees)
