import datadict
import json

workdata = datadict.data

with open('newdata.json', 'w') as writefile:
    writefile.write(json.dumps(workdata, sort_keys=True, indent=4))
