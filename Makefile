PYPATH?=	PYTHONPATH=.
PYBIN?=		python3
LINTBIN?=	flake8

PY_FILES=	cli/iclinic-wea \
		weather/exc.py \
		weather/forecast.py \
		weather/misc.py \
		weather/req.py \
		weather/rule.py \
		weather/version.py
BIN=		cli/iclinic-wea

.PHONY: lint run

lint:
	@${LINTBIN} ${PY_FILES}

run:
	@${PYPATH} ${PYBIN} ${BIN}
