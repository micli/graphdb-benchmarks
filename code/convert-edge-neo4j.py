from __future__ import print_function
import pandas as pd
import os.path

import time

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# starting time.
start = time.time()

# constraints
ENTITY_LABEL = 'ENTITY'
TYPE = 'RELATIONSHIP'

inputFilename = 'edge.csv'
outputFilename = 'rel.csv'

# neo4j schema of entity
rel_map = {":START_ID": [], "name": [], ':END_ID': [], ":TYPE": []}

# delete output file if already exists.
if(os.path.exists(outputFilename)):
    os.remove(outputFilename)

# reading file.
file = pd.read_csv(inputFilename, iterator=True, chunksize=1000000, encoding="utf_8")

i = 1;

pd.DataFrame(rel_map, columns=[":START_ID", "name", ':END_ID', ":TYPE"]) \
    .to_csv(outputFilename, encoding="utf_8_sig", index=False, header=True)

# handle data line by line.
for chunk in file:    
    for _, row in chunk.iterrows():
        rel_map[':START_ID'].append(row[0])
        rel_map['name'].append(str(row[2]))
        rel_map[':END_ID'].append(row[1])
        rel_map[':TYPE'].append(TYPE)

        print("Now handling: {}".format(i), end='\r')
        i = i + 1

    pd.DataFrame(rel_map, columns=[":START_ID", "name", ':END_ID', ":TYPE"]) \
        .to_csv(outputFilename, encoding="utf_8_sig", index=False, header=True)
    print("Now Writing:{}".format(i))
    rel_map = {":START_ID": [], "name": [], ':END_ID': [], ":TYPE": []}

print('Total time: {}'.format(time.time() - start))
f = open("rel_completed.txt", "a")
f.write("Total records: {}".format(i))
f.close()
