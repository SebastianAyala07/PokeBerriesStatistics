# PokeBerriesStatistics
Api that provides statistics data about growth time of berries from PokeAPI


## Up the server 📋

### __Con Docker__ 🚀

_In the root folder of the project (where the entrypoint.py is) execute the following commands_
```
$ docker build --tag pokeapi .
$ docker run -d -p 5000:5000 pokeapi
```

__Run tests__

```
$ docker exec -it <name_container> bash
$ pytest
```

### __With virtual environment__ 🧪
_In the root folder of the project (where the entrypoint.py is) execute the following commands_

You should create a virtual environment with the python 3 preference tool, then activate the environment in console. And now if I run the following commands:

```
$ python -m pip install -r requeriments.txt
$ source env_configuration.sh development
$ flask run
```

__Run tests__

```
$ pytest
```


# Important note

It is recommended to use docker to run the application instance or an environment with ubuntu.

# Testing API
_For testing api I provide you this aws instance and the url is:_

_http://ec2-3-92-255-107.compute-1.amazonaws.com/_

_In this url you can see the histogram image_

## /allBerryStats
_http://ec2-3-92-255-107.compute-1.amazonaws.com/allBerryStats_