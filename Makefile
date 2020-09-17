PYTHON = python3

main:
	$(PYTHON) ./scripts.py build

clean:
	rm build/ dist/ pashmak.spec -rf

update-headers:
	$(PYTHON) ./scripts.py update-headers

test:
	$(PYTHON) ./scripts.py test

docs:
	$(PYTHON) ./scripts.py build-doc

module:
	$(PYTHON) ./scripts.py build-modules

all: update-headers docs module test
	git status

install:
	cp ./dist/pashmak /usr/bin/pashmak

