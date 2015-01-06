
venv:
ifndef VIRTUAL_ENV
	$(error Please install and activate a virtualenv before using the init targets)
endif

init: venv
	pip install wheel
	pip install nose
