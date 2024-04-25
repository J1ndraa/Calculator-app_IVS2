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

all: dist
	./dist/gui

pack: clean
	cd ../../../ && zip -r xcuprm01_xhalva05_xsmiddo00_xspacej00 xcuprm01_xhalva05_xsmiddo00_xspacej00

clean:
	rm -rf __pycache__
	rm -rf dist
	rm -rf ../doc

test:
	chmod +x basic_test.sh && ./basic_test.sh -r 5 && python3 math_library_test.py

doc:
	rm -rf ../doc
	mkdir ../doc
	doxygen Doxyfile

run: 
	./dist/gui

profile:

dist:
	chmod +rwx ../../../xcuprm01_xhalva05_xsmiddo00_xspacej00
	pyinstaller --onefile gui.py
	rm -rf build gui.spec

uninstall:
	chmod +rwx ../../../xcuprm01_xhalva05_xsmiddo00_xspacej00
	rm -rf ../../../xcuprm01_xhalva05_xsmiddo00_xspacej00

.PHONY: all pack clean test doc run profile install
