all:
	python3.11 setup.py build_ext --inplace

clean:
	rm -rf *.out *.bin *.exe *.o *.a *.so test build
	rm -rf *.out *.bin *.exe *.o *.a *.so test build

test:
	python3.11 checkC.py
	python3.11 compute.py
