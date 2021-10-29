# TP_Integrador_Ing_de_Software

[![readthedocs](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](https://pygithub.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://en.wikipedia.org/wiki/MIT_License)
[![Slack](https://img.shields.io/badge/Slack%20channel-%20%20-blue.svg)](https://join.slack.com/t/pygithub-project/shared_invite/zt-duj89xtx-uKFZtgAg209o6Vweqm8xeQ)
[![Open Source Helpers](https://www.codetriage.com/pygithub/pygithub/badges/users.svg)](https://www.codetriage.com/pygithub/pygithub)
[![codecov](https://codecov.io/gh/PyGithub/PyGithub/branch/master/graph/badge.svg)](https://codecov.io/gh/PyGithub/PyGithub)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

TP Integrador de la materia de Ingeniería de Software, con archivos de ejemplo pyhton sobre IA, utilizando la librería [Simpleai].

[Simpleai]: https://github.com/simpleai-team/simpleai

## Install
To install simpleai to test the 
code
```bash
$ pip install simpleai
```
And if you want to use the interactive search viewers, also install:
```bash
$ pip install pydot flask
```

You will need to have pip installed on your system. On linux install the 
python-pip package, on windows follow [this].

[this]: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows

Also, if you are on linux and not working with a virtualenv, remember to use
``sudo`` for both commands
```bash
$ sudo pip install ...
```
## Simple Demo
Simple AI allows you to define problems and look for the solution with
different strategies. Another samples are in the ``samples`` directory, but
here is an easy one.

This problem tries to create the string "HELLO WORLD" using the A* algorithm:
```python
from simpleai.search import SearchProblem, astar

    GOAL = 'HELLO WORLD'


    class HelloProblem(SearchProblem):
        def actions(self, state):
            if len(state) < len(GOAL):
                return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            else:
                return []

        def result(self, state, action):
            return state + action

        def is_goal(self, state):
            return state == GOAL

        def heuristic(self, state):
            # how far are we from the goal?
            wrong = sum([1 if state[i] != GOAL[i] else 0
                        for i in range(len(state))])
            missing = len(GOAL) - len(state)
            return wrong + missing

    problem = HelloProblem(initial_state='')
    result = astar(problem)

    print(result.state)
    print(result.path())
```

## Help and discussion
Join us at the Simple AI [Google group].

[google group]: http://groups.google.com/group/simpleai