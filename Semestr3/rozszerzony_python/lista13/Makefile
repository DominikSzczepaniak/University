run:
	python3 zipapp.py 
	python3 my_app.pyz 
setup:
	pip install -r requirements.txt
clean:
	rm -rf src/__pycache__
	rm -rf tests/__pycache__
	rm -rf docs 
	rm -rf .mypy_cache
	rm -rf __pycache__
test: 
	python3 -m unittest discover -s tests -p 'test.py' -v
pep8:
	autopep8 --in-place --recursive src
documentation:
	pdoc3 --html src/zad.py --output-dir docs
typing:
	mypy src/zad.py