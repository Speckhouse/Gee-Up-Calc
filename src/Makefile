
py_files := $(wildcard *.py)

.PHONY: all pack clean test doc run

# přeloží projekt
all:

# zabalí projekt tak aby mohl být odevzdán
pack: 

# smaže všechny soubory co nemají být odevzdány
clean: 

# spustí testy matematické knihovny
test: 
	./tests_mathlib.py

# spustí generování dokumentace
doc: Doxyfile-simeon $(py_files)
	doxygen $<

# spustí program
run: 
	./Kalkulacka.py
