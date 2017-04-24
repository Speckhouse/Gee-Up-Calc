#!/usr/bin/env make -f

prefix = /opt/GeeUpCalc

py_files := $(wildcard *.py)
py_exec := tests_mathlib.py Kalkulacka.py
py_lib := $(filter-out $(py_exec), $(py_files))

desktop_file = GeeUp-GeeUpCalc.desktop

pack_name = xignac00_xborko02_xdolez76_xhrabo08

# přeloží projekt
.PHONY: all
all:

# zabalí projekt tak aby mohl být odevzdán
.PHONY: pack
pack: doc deb
	(cd .. && git archive --prefix=$(pack_name)/repo/ --format zip HEAD) > $(pack_name).zip
	mkdir -p $(pack_name)/repo $(pack_name)/install $(pack_name)/doc
	ln -sfr -t $(pack_name)/repo ../.git
	ln -sfr -t $(pack_name)/doc html
	ln -sfr -t $(pack_name)/install debian/geeupcalc.deb
	zip -r $(pack_name).zip $(pack_name)

deb:
	make -C debian deb

# smaže všechny soubory co nemají být odevzdány
.PHONY: clean
clean:
	[ -d html ]&& rm -rf html/ ||true
	[ -f $(desktop_file) ]&& rm $(desktop_file) ||true
	[ -d $(pack_name) ]&& rm -rf $(pack_name) ||true
	[ -f $(pack_name).zip ]&& rm $(pack_name).zip ||true
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

.PHONY: $(desktop_file)
$(desktop_file): $(desktop_file).in
	sed 's#%PATH%#'$(prefix)'#' $< > $@

.PHONY: install
install: GeeUp-GeeUpCalc.desktop
	install -m 755 -D -t $(DESTDIR)$(prefix)/lib/ $(py_exec)
	install -m 644 -D -t $(DESTDIR)$(prefix)/lib/ $(py_lib) geeupcalc_icon.png
	install -d $(DESTDIR)$(prefix)/doc/
	cp -r -t $(DESTDIR)$(prefix)/doc/ html/ ../README.md ../user_guide.pdf
ifdef DESTDIR
	install -m 644 -D -t $(DESTDIR)/usr/share/applications $(desktop_file)
else
	xdg-desktop-menu install $(desktop_file)
endif
