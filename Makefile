test:
	venv/bin/nosetests --with-specplugin tests/

pep8:
	pep8 --max-line-length=119 --show-source typograf/
	pep8 --max-line-length=119 --show-source tests/

pyflakes:
	pylama -l pyflakes typograf/
	pylama -l pyflakes tests/

lint:
	make pep8
	make pyflakes

make ci_test:
	nosetests --with-specplugin tests/
	make lint
