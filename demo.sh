export mapreduce_map_input_file=doc1

chmod 777 */*.py

cat Documents/demo* | ./Job1/mapper.py | sort | ./Job1/reducer.py > outputDemo1.txt
cat outputDemo1.txt | ./Job2/mapper.py | sort | ./Job2/reducer.py > outputDemo2.txt
cat outputDemo2.txt | ./Job3/mapper.py | sort | ./Job3/reducer.py > outputFinal.txt