import json
import os
import datetime


def mongodb(rs, hosts, out): 
    os.system('mongodump --host %s/%s --out="%s"' % (rs, ','.join(hosts), out))


def archivate(target, out):
    os.system('tar -zcvf %s.tar.gz %s' % (out, target))
    return '%s.tar.gz' % out


def rm(target):
    os.system('rm -r %s' % target)
    
    
def mv(target, out)
    os.system('mv %s %s' % (target, out))

# Execution
root_dir = os.path.dirname(os.path.abspath(__file__))
with open(root_dir + 'config.json') as f:
    config = json.load(f)

if 'mongodb' in config:
    mongodbConfig = config['mongodb']
    mongodb(mongodbConfig['rs'], mongodbConfig['hosts'], './tmp')
    name = '%s_mongodb' % datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    name = archivate('./tmp/*', name)
    rm('./tmp')
    mv(name, mongodbConfig['out'])
    
if 'mysql' in config:
    # TODO: implement dump
