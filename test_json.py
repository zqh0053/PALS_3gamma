import numpy as np
import json

data_test = []
for i in range(0, 10000000):
    data_0 = {'sd': 0.1 * i, 'qw': 'qwe'}
    data_test.append(data_0)
# data_json = json.dumps(data_test)
# with open("../a.json","w") as f:
#     json.dump(data_json, f)
print('123')
