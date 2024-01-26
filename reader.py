import json
import yaml

def addImages(caption, file_path, title, username, filename):
    try:
        with open('./data/images.json', 'r') as file:
            data = json.load(file)
        
        if 'images' not in data:
            data['images'] = []
        
        new_image_data = {
            'caption': str(caption),
            'file_path': str(file_path),
            'title': str(title),
            'username': str(username),
            'filename': str(filename)
        }
        
        data['images'].append(new_image_data)
        
        with open('./data/images.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        return {'data': new_image_data, 'code': 200, 'message': 'success'}
    except Exception as e:
        return {'code': 500, 'message': str(e)}

def read_yaml_config():
    filepath = './config.yaml'
    with open(filepath, 'r') as file:
        try:
            config = yaml.safe_load(file)
            return config
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file: {exc}")
            return None
