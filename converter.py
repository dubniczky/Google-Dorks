import sys
import json
import yaml


directory = sys.argv[1]


def write(file, data):
    with open(f'{directory}/{file}', 'w', encoding='utf8') as f:
        f.write(data)

# Read dorks file
with open('dorks.yaml', 'r') as f:
    dorks = yaml.safe_load(f)
print(f'Loaded {len(dorks["dorks"])} dorks')

dorklist = list(map(lambda x: x['dork'], dorks['dorks']))

# json
name = 'dorks.json'
write(name, json.dumps(dorks))
print(f'Created {name}')

# txt
name = 'dorks.txt'
write(name, '\n'.join(dorklist))
print(f'Created {name}')

# csv
name = 'dorks.csv'
write(name, '\n'.join(['Dorks', 'Descriptions'] + [f'{dork["dork"]},{dork["desc"]}' for _, dork in enumerate(dorks['dorks'])]))
print(f'Created {name}')
