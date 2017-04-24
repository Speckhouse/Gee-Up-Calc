#!/usr/bin/env make -f

deb_name=geeupcalc

.PHONY: deb
deb:
	install -m 644 -D -t deb/DEBIAN control
	install -m 644 -D -t deb/usr/share/doc/$(deb_name) changelog copyright
	make -C .. DESTDIR=$(realpath .)/deb install
	fakeroot dpkg-deb -b deb $(deb_name).deb

clean:
	[ -d deb ]&& rm -rf deb ||true
	[ -f $(deb_name).deb ]&& rm $(deb_name).deb ||true
