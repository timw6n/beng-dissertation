all: report

prep:
	mkdir -p submission

report: prep
	pandoc sections/*.md appendices/*.md citations/bibliography.md -o submission/project.pdf \
	-V papersize:a4paper -V geometry:left=2cm,right=2cm,top=2cm,bottom=2.4cm \
	--template template.tex \
	--number-sections \
	--bibliography citations/biblio.yaml \
	--csl citations/ieee.csl \
	--latex-engine=xelatex

open:
	open submission/project.pdf

clean:
	rm -rf submission

md5:
	md5deep submission/project.pdf
