import yaml

CONFIG_FILE = 'arm.yaml'

with open(CONFIG_FILE, 'r') as file:
    # Parse the YAML into a Python object
    data = yaml.safe_load(file)

# Pretty-print it back to YAML (nice indentation)
print(yaml.dump(data, default_flow_style=False))
