PYPATH?=	PYTHONPATH=.
PYBIN?=		python3
LINTBIN?=	flake8

PY_FILES=	iclinic_wea.py

.PHONY: lint run test

lint:
	@${LINTBIN} ${PY_FILES}

run:
	@${PYPATH} ${PYBIN} ${PY_FILES}

test:
	@${PYPATH} ${PYBIN} -m unittest
