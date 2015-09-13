## bottleck
Bottleck Custom To MVC Pattern

### Welcome Page
![welcome](https://binderyanwar.files.wordpress.com/2015/09/screenshot-from-2015-09-14-014941.png)

### Prepare
```
$ pip install -r requirements.txt
```

### Running Via `run` file ?
```
$ python run.py

Bottle v0.12.8 server starting up (using WSGIRefServer())...
Listening on http://0.0.0.0:8080/
Hit Ctrl-C to quit.
```

### Command Line Manager
**Running Server (via manager)**
```
$ python manager.py -s localhost@8080
```

**Creating Controller**
```
$ python manager.py -c mycontroller
```

**Creating Models**
```
$ python manager.py -m employees
```

**Creating Views**
```
$ python manager.py -v myviews
```

**Creating Base View**
```
$ python manager.py -b base
```

**Show Your Controllers, Models and Views**
```
$ python manager.py -s all
```

**Help**
```
usage: manager.py [-h] [-c CONTROLLER] [-m MODEL] [-v VIEW] [-b VIEWBASE]
                  [-a SHOWALL] [-s SERVE]

Bottleck Manager [Create By: _YanwarSolahudin]

optional arguments:
  -h, 				--help            			show this help message and exit
  -c CONTROLLER, 	--controller CONTROLLER		create controller
  -m MODEL, 		--model MODEL 				create model
  -v VIEW, 			--view VIEW  				create view
  -b VIEWBASE, 		--viewbase VIEWBASE			create view base
  -a SHOWALL, 		--showall SHOWALL			show all your controllers, models and views
  -s SERVE, 		--serve SERVE				running server, ex manager.py localhost@8080

```
