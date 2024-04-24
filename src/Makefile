# all		(přeloží projekt – včetně programu pro profiling) – při zvolení skriptovacího jazyka využijte pro stažení závislostí, případně volte variantu níže
# pack		(zabalí projekt tak, aby mohl být odevzdán)
# clean		(smaže všechny soubory, co nemají být odevzdány)
# test		(spustí testy matematické knihovny)
# doc		(spustí generování dokumentace)
# run		(spustí program)
# profile	(spustí překlad programu pro výpočet směrodatné odchylky na profiling) – při zvolení skriptovacího jazyka využijte pro stažení závislostí, případně volte variantu níže
# Při spuštění make bez uvedení cíle se provede make all.

CC = python3
.DEFAULT_GOAL := all

all: run

pack: clean
	cd ../../ && zip -r xcuprm01_xhalva05_xsmiddo00_xspacej00 IVS2

clean:
	rm -rf __pycache__
	rm -rf build dist gui.spec
	rm -rf ../doc

test:
	chmod +x basic_test.sh && ./basic_test.sh -r 5 && python3 math_library_test.py

doc: Doxyfile
	rm -rf ../doc
	mkdir ../doc
	doxygen Doxyfile

run: gui.py
	python3 gui.py

profile:

install:
	chmod +rwx ../../IVS2
	pyinstaller --onefile gui.py
	rm -rf build gui.spec

uninstall:
	rm -rf ../../IVS2


.PHONY: all pack clean test doc run profile install
