import sys
import json
import os
import datetime


def mongodb(rs, hosts, out):
    os.system('mongodump --host %s/%s --out="%s"' % (rs, ','.join(hosts), out))


def mariadb(host, out):
    os.system('mysqldump --host=%s --single-transaction --skip-comments --all-databases > %s' % (host, out))


def archivate(target, out):
    os.system('tar -zcvf %s.tar.gz %s' % (out, target))
    return '%s.tar.gz' % out


def rm(target):
    os.system('rm -r %s' % target)


def mv(target, out):
    os.system('mv %s %s' % (target, out))


def ln(target, out):
    os.system('ln -s %s --target-directory="%s"' % (target, out))


def echo(message):
    os.system('echo "%s"' % message)


# Execution
echo('Dump execution:')

root_dir = os.path.dirname(os.path.abspath(__file__))
with open(root_dir + '/config.json') as f:
    config = json.load(f)

if len(sys.argv) < 2 or not sys.argv[1]:
    echo('Bad request: %s.' % sys.argv)
    exit(1)

task = sys.argv[1]
echo('Task selected: %s.' % task)

if task == 'mongodb' and 'mongodb' in config:
    mongodbConfig = config['mongodb']
    mongodb(mongodbConfig['rs'], mongodbConfig['hosts'], './tmp')
    name = '%s_mongodb' % datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    name = archivate('./tmp/*', name)

if task == 'mariadb' and 'mariadb' in config:
    mariadbConfig = config['mariadb']
    mariadb(mariadbConfig['host'], './tmp/dump.sh')
    name = '%s_mariadb' % datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    name = archivate('./tmp/*', name)

if 'name' in locals():
    rm('./tmp')
    mv(name, config['out'])
    name = '%s/%s' % (config['out'], name)
    echo('Dump created: %s.' % name)

    if 'distribution' in config:
        ln(name, config['distribution'])
else:
    echo('Wrong configuration')
    exit(1)
