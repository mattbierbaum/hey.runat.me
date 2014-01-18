.PHONY: all clean

all:
	python ./python/process.py

clean:
	rm -r index.html pages/
