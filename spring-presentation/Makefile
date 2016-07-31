all: presentation
	
prep:
	mkdir -p output

slides: prep
	pandoc spring-slides.md -o output/spring-slides.pdf -t beamer

notes: prep
	pandoc spring-notes.md  -o output/spring-notes.pdf \
		-V papersize:a4paper -V geometry:left=2cm,right=2cm,top=2cm,bottom=2.4cm

presentation: slides notes

open:
	open output/*.pdf

clean:
	rm -rf output
