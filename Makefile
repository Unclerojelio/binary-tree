.PHONY: test clean

test:
	python3 -m unittest -v node_test.TestNode
	python3 -m unittest -v btree_test.TestTree

clean:
	rm -rf __pycache__ *.pyc
