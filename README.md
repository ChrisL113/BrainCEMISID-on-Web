# BrainCEMISID on Web (BACKEND)

## BrainCEMISID V3.0
The BrainCEMISID project is the University of Los Andes (Mérida-Venezuela) first cognitive architecture that tackles problems such as visual and auditive
 information representation, sensorial ambiguities solving, basic visual stimula composition into more complex cultural
 information, autonomous intentions-based decision making, among others.

## Installation

The BrainCEMISID kernel is written in Python 3.7.4 this means that all machines with a 3.7.4 or higher Python interpreter can run the code.

Kernel dependencies:

* Virtual enviroment: to provide a virtual enviroment we recommend use pipenv, to install it just simply type the command ``` pip install pipenv```

* Packages:
django 
djangorestframework 
django-rest-knox 
psycopg2

to install it, run the pipfile.lock with ``` pipenv install```

* Postgres:
https://www.postgresql.org/download/

* DB models: run the command ``` py .\manage.py migrate```

Changing absolute path of the kernel

In the file "...\BrainCEMISID on Web\braincemisid_on_web\brain\api.py"
change the line 11 ```sys.path.append('D:\Desktop\BrainCEMISID on Web\\braincemisid_on_web\kernel')```
for the absolute path that you would have in your machine

To Run:
```python manage.py runserver```

Most of the modules, such as the MulticlassSingleLayerNetwork, contain independent tests that can be of help for the
comprehension of their functionality. Run, for instance:
 ```python multiclass_single_layer_network.py```

## Contributors

* Jonathan Monsalve
* Julio Muchacho
* Ricardo Graterol
* Ricardo Bruzual
* Johan Sosa
* Breytner Fernández, (breytnerm@gmail.com)
* Pedro Vilchez
* Kristo Lopez