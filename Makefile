.PHONY: all a b c d

all: a b c d

a:
	@read -p "Enter input: " input; \
    echo "Input: $$input"; \
    echo "$$input" > input.txt; \
	python fetchapi.py "$$input"

b:
	python script.py

c:
	@input=$$(cat input.txt); \
    echo "Input: $$input"; \
	python pushapi.py "$$input"

d:
	@echo "Convert markdown to pdf ..."
	pandoc REPORT.md -V geometry:landscape -f markdown -o report.pdf

clean:
	@echo "Deleting all the markdown and pdf files ..."
	@rm -f *.md
	@rm -f *.txt
	@rm -f *.html
	# @rm -f *.png
	@rm -f OtherMarkdown/*.md
	@rm -f DefaultMarkdown/*.md