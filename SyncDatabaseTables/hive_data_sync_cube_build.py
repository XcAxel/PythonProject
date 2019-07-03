# encoding=utf-8
import commands
import getopt
import re
import sys
import MySQLdb
import os

import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

database = {
    'host': 'l-dev1.corp.dev.cn0.sgrl.io',
    'user': 'corp_user',
    'password': 'corp_user'
}

#database = {
#    'host': 'l-beta1.corp.beta.cn0.sgrl.io',
#    'user': 'beta',
#    'password': 'Y54jaKx2FM6hxTOO'
#}


data_dir = '/tmp'
kylin_build_js_path = '/home/q/www/tools'

Dev = {
    'name': 'Dev',
    'url': '10.8.102.7:7070',
    'auth': 'YWRtaW46S1lMSU4='
}

Beta = {
    'name': 'Beta',
    'url': '10.8.101.12:7070',
    'auth': 'YWRtaW46S1lMSU4='
}


def print_help():
    help_info = '''
-------------------------sync mysql to hive and build cube command line parameters----------------------------------
    -t, --table    tables to sync
    -c             cube_name
    -p [Dev, Beta] profile

for example: 
    python hive_data_sync_cube_build.py -t 'default.ab_user->ods.t_ab_user_ful;default.task->ods.t_task_ful(dt=2018-09-08,a=2233)' -c cube_name -p Beta
    python hive_data_sync_cube_build.py -t 'cboard.orc_test->default.orc_test(dt=a,dt1=b)' -c c_orc_test -p Dev
-----------------------------------------------------------------------------------------------------
'''
    print help_info


def parse_args():
    opts, args = getopt.getopt(sys.argv[1:], 't:c:p:', ['table='])
    table = ''
    cube_name = None
    profile = None
    for o, v in opts:
        if o in ('-t', '--table'):
            if v != '' and v is not None:
                table = v
            else:
                print "-t or --table param value [%s] is invalid" % v
                print_help()
                exit(1)
        if o in ('-c',):
            if v != '' and v is not None:
                cube_name = v
            else:
                print "-c param value [%s] is invalid" % v
                print_help()
                exit(1)
        if o in ('-p',):
            if v != '' and v is not None and v in ('Dev', 'Beta'):
                if v == 'Dev':
                    profile = Dev
                if v == 'Beta':
                    profile = Beta
            else:
                print "-p param value [%s] is invalid" % v
                print_help()
                exit(1)

    if table is None or table == '' or cube_name is None or profile is None:
        print 'please assign correct params'
        print_help()
        exit(1)
    to_sync_tables = []
    for item in table.replace(' ', '').replace('"', '').replace("'", '').split(';'):
        r = re.findall(r'([^.]*).([^-]*)->([^.]*).([^(]*)(\(.*\))?', item)
        if len(r) != 1:
            print '%s is not invalid, please recheck it.' % item
            exit(1)
        pf = re.findall(r'([^=(,]*)=([^,)]*)', r[0][4])
        pf_m = {}
        for x in pf:
            pf_m[x[0]] = x[1]
        to_sync_tables.append({
            'mysql_database': r[0][0],
            'mysql_table': r[0][1],
            'hive_database': r[0][2],
            'hive_table': r[0][3],
            'partitions': pf_m
        })
    return to_sync_tables, cube_name, profile


def check_args(to_sync_tables):
    for item in to_sync_tables:
        check_is_exist_mysql_database(item['mysql_database'])
        check_is_exist_mysql_table(item['mysql_database'], item['mysql_table'])
        check_is_exist_hive_database(item['hive_database'])
        check_is_exist_hive_table(item['hive_database'], item['hive_table'])


def fetch_mysql_databases():
    databases = []
    conn = MySQLdb.connect(host=database['host'], user=database['user'], passwd=database['password'], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("show databases")
    results = cursor.fetchall()
    for row in results:
        databases.append(row[0])
    return databases


def fetch_mysql_tables(mysql_database):
    tables = []
    conn = MySQLdb.connect(host=database['host'], user=database['user'], passwd=database['password'], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("show tables in %s" % mysql_database)
    results = cursor.fetchall()
    for row in results:
        tables.append(row[0])
    return tables


def check_is_exist_mysql_database(mysql_database):
    if mysql_database not in fetch_mysql_databases():
        print '%s database is not exist in mysql, please check it' % mysql_database
        exit(1)


def check_is_exist_mysql_table(mysql_database, mysql_table):
    if mysql_table not in fetch_mysql_tables(mysql_database):
        print '%s.%s is not exist in mysql, please check it' % (mysql_database, mysql_table)
        exit(1)


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


def extract_compress_type(ddl):
    r = re.findall(r"STORED AS INPUTFORMAT +'org\.apache\.hadoop\.hive\.ql\.io\.orc\.OrcInputFormat'", ddl)
    if len(r) > 0:
        return 'orc'
    r = re.findall(r"STORED AS INPUTFORMAT +'com\.hadoop\.mapred\.DeprecatedLzoTextInputFormat'", ddl)
    if len(r) > 0:
        return 'lzo'
    r = re.findall(r"STORED AS INPUTFORMAT +'org\.apache\.hadoop\.mapred\.TextInputFormat'", ddl)
    if len(r) > 0:
        return 'text'
    r = re.findall(r"CREATE TABLE `([^.]*)\.([^`]*)`", ddl)
    if len(r) > 0:
        print 'extract %s.%s compress type error.' % (r[0][0], r[0][1])
        exit(1)
    print 'execute extract_compress_type method error.'
    exit(1)


def extract_field_delimited(ddl):
    r = re.findall(r"FIELDS TERMINATED BY '([^']*)'", ddl)
    if len(r) > 0:
        return '\t' if r[0] == '\\t' else r[0]
    r = re.findall(r"'field\.delim'='([^']*)'", ddl)
    if len(r) > 0:
        return '\t' if r[0] == '\\t' else r[0]
    r = re.findall(r"CREATE TABLE `([^.]*)\.([^`]*)`", ddl)
    if len(r) > 0:
        print "can't find %s.%s field delimited, use default.[\\001]" % (r[0][0], r[0][1])
        return '\001'
    print 'execute extract_field_delimited method error.'
    exit(1)


def extract_partition_field(ddl):
    r = re.findall(r"PARTITIONED BY \([^)]*\)", ddl)
    if len(r) > 0:
        ps = re.findall(r"`([^`]*)`", r[0])
        return ps
    r = re.findall(r"CREATE (EXTERNAL)? TABLE `([^.]*)\.([^`]*)`", ddl)
    if len(r) > 0:
        print "can't find %s.%s partition, maybe is's not a partition table, so continue." % (r[0][0], r[0][1])
        return []
    print 'execute extract_partition_field method error.'
    exit(1)


def extract_hive_info(hive_database, hive_table):
    ddl = fetch_create_table(hive_database, hive_table)
    return extract_compress_type(ddl), extract_field_delimited(ddl), extract_partition_field(ddl)


def fetch_mysql_data(mysql_database, mysql_table, f):
    conn = MySQLdb.connect(host=database['host'], user=database['user'], passwd=database['password'], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from %s.%s" % (mysql_database, mysql_table))
    results = cursor.fetchall()
    with open('%s/%s_%s.dat' % (data_dir, mysql_database, mysql_table), 'w') as w:
        for row in results:
            i = 0
            fields = []
            while i < len(row):
                fields.append('\N' if row[i] is None else str(row[i]).replace('\t', '\\t').replace('\r', '\\r').replace('\n', '\\n'))
                i += 1
            w.writelines(f.join(fields) + '\n')


def compress_mysql_data(mysql_database, mysql_table, c):
    if c == 'lzo':
        cmd = 'lzop -f %s/%s_%s.dat' % (data_dir, mysql_database, mysql_table)
        print cmd
        if os.system(cmd) != 0:
            print 'execute %s error.' % cmd
            exit(1)


def load_data_to_hive(mysql_database, mysql_table, hive_database, hive_table, partitions, c, f, p):
    if c == 'text' or c == 'lzo':
        file_name = '%s/%s_%s.dat' % (data_dir, mysql_database, mysql_table)
        file_name = file_name + '.lzo' if c == 'lzo' else file_name

        pf = []
        for x in p:
            if x not in partitions and x == 'dt':
                pf.append("dt='%s'" % (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))
            else:
                pf.append("%s='%s'" % (x, partitions[x]))
        partition_str = '' if len(pf) == 0 else "PARTITION (%s)" % ','.join(pf)

        cmd = """hive -e "LOAD DATA LOCAL INPATH '%s' OVERWRITE INTO TABLE %s.%s %s;" """ % (file_name, hive_database, hive_table, partition_str)
        print cmd
        if os.system(cmd) != 0:
            print 'execute %s error.' % cmd
            exit(1)

    if c == 'orc':
        cmd = """hive -e "create table IF NOT EXISTS %s.%s_tmp like %s.%s STORED AS TEXTFILE" """ % (hive_database, hive_table, hive_database, hive_table)
        print cmd
        if os.system(cmd) != 0:
            print 'execute %s error.' % cmd
            exit(1)
        file_name = '%s/%s_%s.dat' % (data_dir, mysql_database, mysql_table)
        pf = []
        for x in p:
            if x not in partitions and x == 'dt':
                pf.append("dt='%s'" % (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))
            else:
                pf.append("%s='%s'" % (x, partitions[x]))
        partition_str = '' if len(pf) == 0 else "PARTITION (%s)" % ','.join(pf)
        where_str = '' if len(pf) == 0 else "where %s" % ' and '.join(pf)
        cmd = """hive -e "LOAD DATA LOCAL INPATH '%s' OVERWRITE INTO TABLE %s.%s_tmp %s;" """ % (file_name, hive_database, hive_table, partition_str)
        print cmd
        if os.system(cmd) != 0:
            print 'execute %s error.' % cmd
            exit(1)
        cmd = """hive -e "set hive.support.quoted.identifiers=None; INSERT OVERWRITE TABLE %s.%s %s select \`(%s)?+.+\` FROM %s.%s_tmp %s;" """ % (hive_database, hive_table, partition_str, '|'.join(sorted(p, reverse=True)), hive_database, hive_table, where_str)
        print cmd
        if os.system(cmd) != 0:
            print 'execute %s error.' % cmd
            exit(1)
        cmd = """hive -e "drop table %s.%s_tmp" """ % (hive_database, hive_table)
        print cmd
        if os.system(cmd) != 0:
            print 'execute %s error.' % cmd
            exit(1)


def check_partitions(hive_database, hive_table, partitions, p):
    if len(partitions) != len(p) and len(partitions) + 1 != len(p):
        print 'please assign correct %s.%s partition info.' % (hive_database, hive_table)
        exit(1)

    for x in p:
        if x not in partitions and x != 'dt':
            print 'please assign correct %s.%s partition info. table partitions %s' % (hive_database, hive_table, p)
            exit(1)


def build_cube(c, p):
    cmd = """sh %s/DevOrBeta_kylin_build.sh %s %s %s """ % (kylin_build_js_path, c, p['auth'], p['url'])
    (status, output) = commands.getstatusoutput(cmd)
    if status != 0:
        print 'execute: %s error.' % cmd
        exit(1)


def main():
    (to_sync_tables, cube_name, profile) = parse_args()
    check_args(to_sync_tables)
    for item in to_sync_tables:
        (c, f, p) = extract_hive_info(item['hive_database'], item['hive_table'])
        check_partitions(item['hive_database'], item['hive_table'], item['partitions'], p)
        fetch_mysql_data(item['mysql_database'], item['mysql_table'], f)
        compress_mysql_data(item['mysql_database'], item['mysql_table'], c)
        load_data_to_hive(item['mysql_database'], item['mysql_table'], item['hive_database'], item['hive_table'], item['partitions'], c, f, p)
    print 'start to build cube, You can view progress in the kylin webUI, http://%s/kylin/jobs' % profile['url']
    build_cube(cube_name, profile)
    print 'success'


if __name__ == "__main__":
    main()



