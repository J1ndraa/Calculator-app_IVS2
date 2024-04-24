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

all: 

pack: clean
	zip -r ../xhalva05_xcuprm01_xsmiddo00_xspacej00 ../xhalva05_xcuprm01_xsmiddo00_xspacej00

clean:
	rm -rf __pycache__

test:
	bash basic_test.sh

doc:

run: gui.py
	python3 gui.py

profile:

.PHONY: all pack clean test doc run profile
