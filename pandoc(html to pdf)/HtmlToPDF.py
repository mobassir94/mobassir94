import pypandoc

conout = pypandoc.convert_file("index.html",'pdf',outputfile = "my.pdf", extra_args=['--pdf-engine=pdflatex'])
assert output ==""
