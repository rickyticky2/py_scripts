import yaml
import os

# Specify the path to your YAML file
yaml_file = 'example.yaml'

# Open and read the YAML file
with open(yaml_file, 'r') as f:
    data = yaml.safe_load(f)

# Clone each repository listed in the YAML file
for repo in data:
    name = repo['name']
    if 'branch' in repo:
        branch = repo['branch']
    else:
        branch = 'main'  # or whatever default you prefer
    print(f'Cloning {name} ({branch})...')
    os.system(f'git clone --branch {branch} https://github.com/{name}')
