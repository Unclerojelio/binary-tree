.PHONY: test run clean

test:
	python3 -m unittest -v node_test.TestNode
	python3 -m unittest -v btree_test.TestTree
	
run:
	python3 main.py

clean:
	rm -rf __pycache__ *.pyc
