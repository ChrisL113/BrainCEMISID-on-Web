# BrainCEMISID on Web (BACKEND)

## BrainCEMISID V3.0
The BrainCEMISID project is the University of Los Andes (Mérida-Venezuela) first cognitive architecture that tackles problems such as visual and auditive
 information representation, sensorial ambiguities solving, basic visual stimula composition into more complex cultural
 information, autonomous intentions-based decision making, among others.

## Installation

The BrainCEMISID kernel is written in Python 3.7.4 this means that all machines with a 3.7.4 or higher Python interpreter can run the code.

Kernel dependencies:

* Virtual enviroment: to provide a virtual enviroment we recommend use pipenv, to install it just simply type the command ``` pip install pipenv```


to install it, run the pipfile.lock with ``` pipenv install```

* Postgres:
https://www.postgresql.org/download/

* DB models: run the command ``` py .\manage.py migrate```


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