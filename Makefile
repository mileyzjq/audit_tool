.PHONY: all a b c

all: a b c

a:
	python fetchapi.py

b:
	python script.py

c:
	python pushapi.py


clean:
	@echo "Deleting all the markdown and pdf files ..."
	@rm -f *.md
	@rm -f *.pdf