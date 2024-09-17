import json
from os.path import join,dirname

data_path = join(dirname(__file__),"..","data.json")

def dump_data_to_json(data, file_path=data_path):
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def load_data_from_json(file_path=data_path):
        if file_path is not None:   
            with open(file_path, 'r+') as json_file:
                data = json.load(json_file)
                return data
        else:
            with open(file_path,'w') as json_file:
                json.dump({},json_file,indent=4)
                return {}
        


