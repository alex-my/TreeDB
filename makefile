.PHONY: clean-build, clean-pyc
help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove python file artifacts"
	@echo "check - pypi check"
	@echo "sdist - pypi create package"
	@echo "upload - pypi upload package"

clean: clean-build, clean-pyc

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

check:
	python setup.py check

sdist: clean
	python setup.py sdist

upload: clean
	python setup.py sdist upload
