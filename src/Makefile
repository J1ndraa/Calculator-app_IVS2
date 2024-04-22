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

pack:
	zip -r ../ivs2 ../IVS2 #netestováno
clean:
	rm -rf ../code/__pycache__

test:
	@echo "\e[1;97;44mbasic tests:\e[0m"
	@for number in 1 2 3 4 5 6 7 8 9 10 11 12 ; do \
		echo "\e[92mtest $$number:\e[0m" ; \
		cat "../code/tests/basic_operation_$$number.input" ; \
		echo "" ; \
		python3 ../code/calc.py < ../code/tests/basic_operation_$$number.input ; \
		echo "" ; \
	done

	@echo "\e[1;97;44madvanced tests:\e[0m"
	@for number in 1 2 3 4 5 6 7 8 ; do \
		echo "\e[92mtest $$number:\e[0m" ; \
		cat "../code/tests/advanced_operation_$$number.input" ; \
		echo "" ; \
		python3 ../code/calc.py < ../code/tests/advanced_operation_$$number.input ; \
		echo "" ; \
	done

doc:

run: main.py	# tohle nahradit hlavním souborem
	python main.py 

profile:

.PHONY: all pack clean test doc run profile
