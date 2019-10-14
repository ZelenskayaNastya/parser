import argparse
import json
import os
import tempfile



parser = argparse.ArgumentParser()
parser.add_argument('--key', type=str)
parser.add_argument('--val', type=str)
argum = parser.parse_args()




if argum.val and argum.key:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.isfile(storage_path) and os.path.getsize(storage_path) != 0:
        with open(storage_path, 'w+') as f:
            data = json.load(f)
            try:
                if argum.key in data:
                    print(data[argum.key])
                data[argum.key].append(argum.val)
                json.dump(data, f)
            except:
                data[argum.key] = [argum.val]
                with open(storage_path, "w") as f:
                    json.dump(data, f)
    else:
        with open(storage_path, "w") as f:
            dict = {}
            dict[argum.key] = [argum.val]
            json.dump(dict, f)


else:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.isfile(storage_path) and os.path.getsize(storage_path) != 0:
        with open(storage_path, "r") as f:
            data = json.load(f)
            if argum.key in data.keys():
                print(', '.join(data[argum.key]))
            else:
                print('None')
    else:
        print('None_2')



