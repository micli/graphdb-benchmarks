from __future__ import print_function
import pandas as pd
import os.path

import time

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


#start time.
start = time.time()

# constraints
ENTITY_LABEL = 'ENTITY'
TYPE = 'RELATIONSHIP'

inputFilename = 'vertex.csv'
outputFilename = 'entity.csv'

# neo4j schema of entity
entity_map = {":ID": [], "name": [], ':LABEL': []}

# delete output file if already exists.
if(os.path.exists(outputFilename)):
    os.remove(outputFilename)

# reading file.
file = pd.read_csv(inputFilename, iterator=True, chunksize=1000000, encoding="utf_8")

i = 1;

pd.DataFrame(entity_map, columns=[":ID", "name", ':LABEL'])\
    .to_csv(outputFilename, encoding="utf_8_sig", index=False, header=True)

# handle data line by line.
for chunk in file:    
    for _, row in chunk.iterrows():
        entity_map[':ID'].append(row[0])
        entity_map['name'].append(str(row[1]))
        entity_map[':LABEL'].append(ENTITY_LABEL)
        print("Now handling:{}".format(i), end='\r')
        i = i + 1

    pd.DataFrame(entity_map, columns=[":ID", "name", ':LABEL'])\
        .to_csv(outputFilename, encoding="utf_8_sig", index=False, header=True)
    print("Now Writing:{}".format(i))
    entity_map = {":ID": [], "name": [], ':LABEL': []}

print('Total time:{}'.format(time.time() - start))
f = open("entity_completed.txt", "a")
f.write("Total records: {}".format(i))
f.close()
