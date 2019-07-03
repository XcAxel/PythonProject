import commands
import getopt
import os
import re

import sys

Dev = {
    'name': 'Dev',
    'name_node': 'hdfs://l-datacenter1.dev.dc.cn0:8020',
    'hive_server': 'jdbc:hive2://l-datacenter3.dev.dc.cn0:10000'
}

Beta = {
    'name': 'Beta',
    'name_node': 'hdfs://l-namenode1.beta.dc.cn4:8020',
    'hive_server': 'jdbc:hive2://l-datanode1.beta.dc.cn4:10000'
}

Prod = {
    'name': 'Prod',
    'name_node': 'hdfs://l-namenode2.dc.cn1:8020',
    'hive_server': ''
}


def print_help():
    help_info = '''
-------------------------sync hive to hive command line parameters----------------------------------
    -T, --table    tables to sync
    -f,--from:     [Dev, Beta, Prod]
    -t,--to:       [Dev, Beta]

note:
    1.Please make sure that each table is less than 200M
    2.Ensure the [to] profile hiveserver2 and hive metastore service are online if the sync table is partitioned
    3.Please use hive user
    4.Ensure that table structure is consistent
for example: 
    python hive_table_sync.py -T 'default.dim_table(dt=a)' -f Beta -t Dev
    python hive_table_sync.py -T 'default.fact_table' -f Dev -t Beta
-----------------------------------------------------------------------------------------------------
'''
    print help_info


def parse_args():
    opts, args = getopt.getopt(sys.argv[1:], 'T:f:t:', ['table=', 'from=', 'to='])
    table_str = ''
    from_profile = None
    to_profile = None
    for o, v in opts:
        if o in ('-T', '--table'):
            if v != '' and v is not None:
                table_str = v
            else:
                print "-t or --table param value [%s] is invalid" % v
                print_help()
                exit(1)
        if o in ('-f', '--from'):
            if v == 'Dev':
                from_profile = Dev
            elif v == 'Beta':
                from_profile = Beta
            elif v == 'Prod':
                from_profile = Prod
            else:
                print "-f, --from param value [%s] is invalid" % v
                print_help()
                exit(1)
        if o in ('-t', '--to'):
            if v == 'Dev':
                to_profile = Dev
            elif v == 'Beta':
                to_profile = Beta
            elif v == 'Prod':
                to_profile = Prod
            else:
                print "-t, --to param value [%s] is invalid" % v
                print_help()
                exit(1)
    if table_str is None or table_str == '':
        print 'please assign correct params'
        print_help()
        exit(1)
    if from_profile is None or to_profile is None:
        print "from profile or to profile is None ,please resign it"
        print_help()
        exit(1)
    if from_profile == to_profile:
        print "from[%s] is equal to to[%s] ,please resign it" % (from_profile['name'], to_profile['name'])
        print_help()
        exit(1)
    if to_profile == Prod:
        print "to [%s] is not allowed ,please resign it" % to_profile['name']
        print_help()
        exit(1)

    to_sync_tables = []
    for item in table_str.replace(' ', '').replace('"', '').replace("'", '').split(';'):
        r = re.findall(r'([^.]*)\.([^(]*)(\(.*\))?', item)
        if len(r) != 1:
            print '%s is not invalid, please recheck it.' % item
            exit(1)
        pf = re.findall(r'([^=(,]*)=([^,)]*)', r[0][2])
        pf_m = []
        for x in pf:
            pf_m.append((x[0], x[1]))
        to_sync_tables.append({
            'hive_database': r[0][0],
            'hive_table': r[0][1],
            'partitions': pf_m
        })
    return to_sync_tables, from_profile, to_profile


def check_is_exist_hive_database(hive_database):
    cmd = 'c=`hive -e "show databases" | grep "^%s$" | wc -l` && if [ $c -eq 1 ];then echo 1; else exit 1; fi' % hive_database
    print cmd
    if os.system(cmd) != 0:
        print '%s database is not exist in hive, please check it' % hive_database
        exit(1)


def check_is_exist_hive_table(hive_database, hive_table):
    cmd = 'c=`hive -e "show tables in %s" | grep "^%s$" | wc -l` && if [ $c -eq 1 ];then echo 1; else exit 1; fi' % (
    hive_database, hive_table)
    print cmd
    if os.system(cmd) != 0:
        print '%s.%s is not exist in hive, please check it' % (hive_database, hive_table)
        exit(1)


def fetch_create_table(hive_database, hive_table):
    cmd = """hive -e 'show create table %s.%s'""" % (hive_database, hive_table)
    (status, output) = commands.getstatusoutput(cmd)
    if status != 0:
        print 'execute: %s error.' % cmd
        exit(1)
    return output.replace('\n', ' ')


def extract_partition_field(ddl):
    r = re.findall(r"PARTITIONED BY \([^)]*\)", ddl)
    print(ddl)
    if len(r) > 0:
        ps = re.findall(r"`([^`]*)`", r[0])
        return ps
    r = re.findall(r"CREATE (EXTERNAL )?TABLE `([^.]*)\.([^`]*)`", ddl)
    if len(r) > 0:
        print "can't find %s.%s partition, maybe is's not a partition table, so continue." % (r[0][0], r[0][1])
        return []
    print 'execute extract_partition_field method error.'
    exit(1)


def extract_location(ddl):
    r = re.findall(r"LOCATION +'hdfs://([^/]*)([^']*)'", ddl)
    if len(r) > 0:
        return r[0][1]
    r = re.findall(r"CREATE TABLE `([^.]*)\.([^`]*)`", ddl)
    if len(r) > 0:
        print "can't find %s.%s LOCATION, so exit." % (r[0][0], r[0][1])
        exit(1)


def check_args(to_sync_tables):
    for item in to_sync_tables:
        check_is_exist_hive_database(item['hive_database'])
        check_is_exist_hive_table(item['hive_database'], item['hive_table'])
    for item in to_sync_tables:
        ddl = fetch_create_table(item['hive_database'], item['hive_table'])
        p_f = extract_partition_field(ddl)
        if len(p_f) != 0:
            item['partitioned'] = True
        else:
            item['partitioned'] = False
        item["file_path"] = extract_location(ddl)


def check_cmd_status(cmd):
    print cmd
    if os.system(cmd) != 0:
        print 'execute %s error.' % cmd
        exit(1)


def sync_data(to_sync_tables, from_profile, to_profile):
    for item in to_sync_tables:
        partition_str = ''
        if item['partitioned']:
            ps = []
            for x in item['partitions']:
                ps.append('/%s=%s' % (x[0], x[1]))
            partition_str = ''.join(ps)

        cmd = """hdfs dfs -rm -r -f %s%s%s""" % (to_profile['name_node'], item['file_path'], partition_str)
        if cmd.__contains__('cn1') :
            print """you are deleting online file, it's dangerous operator. please check your config."""
            exit(1)
        check_cmd_status(cmd)
        cmd = """hdfs dfs -mkdir -p %s%s%s""" % (to_profile['name_node'], item['file_path'], partition_str)
        check_cmd_status(cmd)
        cmd = """hdfs dfs -cp -f %s%s%s/* %s%s%s""" % (from_profile['name_node'], item['file_path'], partition_str,
                                                    to_profile['name_node'], item['file_path'], partition_str)
        check_cmd_status(cmd)
        if item['partitioned']:
            cmd = """beeline -u %s -e 'set hive.msck.path.validation=ignore; MSCK REPAIR TABLE %s.%s'""" % (to_profile['hive_server'], item['hive_database'], item['hive_table'])
            check_cmd_status(cmd)


def main():
    (to_sync_tables, from_profile, to_profile) = parse_args()
    check_args(to_sync_tables)
    sync_data(to_sync_tables, from_profile, to_profile)
    print 'success'


if __name__ == '__main__':
    if os.environ['HOME'] != '/home/hive':
        print 'please use hive user to execute this script.'
        exit(1)
    main()


