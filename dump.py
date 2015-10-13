import json
import os


def mongodb(rs, hosts, out): 
    os.system('mongodump --host %s/%s --out="%s"' % (rs, ','.join(hosts), out))

# Execution
root_dir = os.path.dirname(os.path.abspath(__file__))
with open(root_dir + 'config.json') as f:
    config = json.load(f)

if 'mongodb' in config:
    mongodbConfig = config['mongodb']
    mongodb(mongodbConfig['rs'], mongodbConfig['hosts'], mongodbConfig['out'])
    
if 'mysql' in config:
    # TODO: implement dump
