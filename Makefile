all: americanVoices.html

gather:
	python americanVoices.py >> results.txt

americanVoices.html: results.txt
	sort $< | uniq | python genHtml.py > $@