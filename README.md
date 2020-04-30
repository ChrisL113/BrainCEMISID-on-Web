# BrainCEMISID on Web (BACKEND)

## BrainCEMISID V3.0
The BrainCEMISID project is the University of Los Andes (Mérida-Venezuela) first cognitive architecture that tackles problems such as visual and auditive
 information representation, sensorial ambiguities solving, basic visual stimula composition into more complex cultural
 information, autonomous intentions-based decision making, among others.

## Installation

The BrainCEMISID kernel is written in Python 3.7.4 this means that all machines with a 3.7.4 or higher Python interpreter can run the code.

Kernel dependencies:

* Virtual enviroment: to provide a virtual enviroment we recommend use pipenv, to install it just simply type the command ``` pip install pipenv```


to install the braincemisid run the pipfile.lock with ``` pipenv install```

* Postgres:
https://www.postgresql.org/download/

* DB models: run the command ``` py .\manage.py migrate```

** Note: Remember create a database in postgres in order to make the migration succesful, for dev branch use in psql terminal ``` create database braincemisid_db_dev;``` and for master branch use ``` create database braincemisid_db;``` , otherwise, you can change the name of the database, DBMS provider or some other configuration by editing the file ```settings.py``` in the address ```\braincemisid_on_web\braincemisid_on_web\```

To Run:
```python manage.py runserver```

Most of the modules, such as the MulticlassSingleLayerNetwork contains independent tests, so that can be helpful for the
comprehension of his functionality. Run, for instance:
 ```python multiclass_single_layer_network.py```

* link of the frontend part of the project:
https://github.com/PedrouV/BrainCEMISID-frontend

## Support material

* Postman queries

In the root of the repo import the \Postman Queries\BrainCemisid_on_web.postman_collection.json

* Manuals

In the root of the repo the folder \Manuals\ contains several manuals to understand better the project

## Legacy

* Link of Braincemisid 2.0
https://github.com/braincemisid/kernel
* Link of Braincemisid 2.1 (Mudafar version)
https://github.com/mudafar/Brain-CEMISID-Parallel

###### Demos videos of the Braincemisid 2 versions

* Basic Learning

https://www.youtube.com/watch?v=BuB8OyYRkh4&feature=youtu.be

* Recognition

https://www.youtube.com/watch?v=OYY-w0j_ce4&feature=youtu.be

* Letters

https://www.youtube.com/watch?v=_OWHv3APHgQ&feature=youtu.be

* Syllables

https://www.youtube.com/watch?v=Zlsk-rDnqcQ&feature=youtu.be

* Words

https://www.youtube.com/watch?v=4M5qs4xYwpk&feature=youtu.be

* Addition

https://www.youtube.com/watch?v=cRCmvIEslIo&feature=youtu.be

* learning 1 6

https://www.youtube.com/watch?v=Rf_nd698rhs&feature=youtu.be

## Contributors

* Jonathan Monsalve
* Julio Muchacho
* Ricardo Graterol
* Ricardo Bruzual
* Johan Sosa
* Breytner Fernández, (breytnerm@gmail.com)
* Pedro Vilchez
* Kristo Lopez
