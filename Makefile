python    := `which python`
pythondoc := `which pythondoc.py`
docopts   := "-Ogcwikiformatter -s"
pyfiles   := $(shell find ../trunk/ib/ -name "*.py")
modules   := $(sort $(wordlist 1, $(words $(pyfiles)), $(pyfiles)))


.PHONY: all $(modules)


all: $(modules)


$(modules):
	@echo [I] generating wiki doc for $@
	@export PYTHONPATH=$(shell pwd) && "$(python)" "$(pythondoc)" "$(docopts)" $@
