PYPATH?=	PYTHONPATH=.
PYBIN?=		python3
LINTBIN?=	flake8

PY_FILES=	iclinic_wea.py

.PHONY: lint run test

lint:
	@${LINTBIN} ${PY_FILES}

run:
	@${PYPATH} ${PYBIN} ${PY_FILES}

coverage:
	@${PYTPATH} coverage run -m unittest discover

test:
	@${PYPATH} ${PYBIN} -m unittest
