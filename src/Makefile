#!/usr/bin/env make -f

prefix = /opt/GeeUpCalc

py_files := $(wildcard *.py)

# přeloží projekt
.PHONY: all
all:

# zabalí projekt tak aby mohl být odevzdán
.PHONY: pack
pack:

# smaže všechny soubory co nemají být odevzdány
.PHONY: clean
clean:
	[ -d html ]&& rf -rf html/ ||true
	make -C debian clean

# spustí testy matematické knihovny
.PHONY: test
test: 
	./tests_mathlib.py

# spustí generování dokumentace
.PHONY: doc
doc: html

html: Doxyfile-simeon $(py_files)
	doxygen $<

# spustí program
.PHONY: run
run: 
	./Kalkulacka.py

.PHONY: install
install:
	install -D -t $(DESTDIR)$(prefix)/lib/ $(py_files) geeupcalc_icon.png
	install -d $(DESTDIR)$(prefix)/doc/
	cp -r -t $(DESTDIR)$(prefix)/doc/ html/ ../README.md ../user_guide.pdf
