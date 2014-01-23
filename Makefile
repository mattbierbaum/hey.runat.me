.PHONY: all clean install serve

all:
	python ./python/process.py

clean:
	rm -r index.html pages/

install:
	./python/install.sh

serve:
	python -m SimpleHTTPServer 8080
