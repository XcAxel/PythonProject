# encoding=utf-8

import sys
import getopt
import httplib
import urllib
import json
import os
from datetime import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

Dev = {
    'name': 'Dev',
    'url': '10.8.102.7:7070',
    'auth': 'YWRtaW46S1lMSU4='
}

Beta = {
    'name': 'Beta',
    'url': '10.7.64.49:7070',
    'auth': 'YWRtaW46S1lMSU4='
}

Prod = {
    'name': 'Prod',
    'url': '10.7.78.34:7070',
    'auth': 'YWRtaW46RUhqVjIzKlFVeQ=='
}

backup_path = "/tmp"


def print_help():
    help_info = '''
-------------------------The cube sync command line parameters----------------------
    -m:            whether to sync model
    -c:            whether to sync cube
    --project:     project name
    --model:       model name
    --cube:        cube name
    -f,--from:     [Dev, Beta, Prod]
    -t,--to:       [Dev, Beta, Prod]
    
for example: 
    python cube_sync.py -m -c --project=XXX --model=XXX --cube=XXX -f Beta -t Dev
------------------------------------------------------------------------------------
'''
    print help_info


def fetch_model(profile, model_name):
    headers = {"Authorization": "Basic %s" % profile['auth']}
    conn = httplib.HTTPConnection(profile['url'])
    conn.request("GET", '/kylin/api/models?modelName=' + model_name, urllib.urlencode({}), headers)
    response = conn.getresponse()
    res = response.read()
    if response.status == 200:
        return json.loads(res)
    else:
        print("fetch model from [%s] error, error msg: %s, response: %s" % (profile['name'], response.reason, res))
        exit(1)


def insert_model(profile, project_name, model_json):
    params = {'project': project_name, 'modelDescData': json.dumps(model_json)}
    headers = {"Authorization": "Basic %s" % profile['auth'], "Content-Type": "application/json"}
    conn = httplib.HTTPConnection(profile['url'])
    conn.request("POST", '/kylin/api/models', json.dumps(params), headers)
    response = conn.getresponse()
    res = response.read()
    if response.status == 200:
        res = json.loads(res)
        if hasattr(res, 'exception'):
            print 'sync model error, msg: %s, response: %s' % (res['exception'], res)
            exit(1)
        else:
            print 'sync model success'
    else:
        print "sync model error, msg: %s, response: %s" % (response.reason, res)
        exit(1)


def update_model(profile, project_name, model_json):
    params = {'project': project_name, 'modelDescData': json.dumps(model_json)}
    headers = {"Authorization": "Basic %s" % profile['auth'], "Content-Type": "application/json"}
    conn = httplib.HTTPConnection(profile['url'])
    conn.request("PUT", '/kylin/api/models', json.dumps(params), headers)
    response = conn.getresponse()
    res = response.read()
    if response.status == 200:
        res = json.loads(res)
        if hasattr(res, 'exception'):
            print 'sync model error, msg: %s, response: %s' % (res['exception'], res)
            exit(1)
        else:
            print 'sync model success'
    else:
        print "sync model error, msg: %s, response: %s" % (response.reason, res)
        exit(1)


def fetch_cube(profile, cube_name):
    headers = {"Authorization": "Basic %s" % profile['auth']}
    conn = httplib.HTTPConnection(profile['url'])
    conn.request("GET", '/kylin/api/cube_desc/' + cube_name, urllib.urlencode({}), headers)
    response = conn.getresponse()
    res = response.read()
    if response.status == 200:
        if res is None or res == '':
            return []
        else:
            return json.loads(res)
    else:
        print("fetch cube from [%s] error, error msg: %s, response: %s" % (profile['name'], response.reason, res))
        exit(1)


def insert_cube(profile, project_name, cube_json):
    params = {'project': project_name, 'cubeName': cube_json['name'], 'cubeDescData': json.dumps(cube_json)}
    headers = {"Authorization": "Basic %s" % profile['auth'], "Content-Type": "application/json"}
    conn = httplib.HTTPConnection(profile['url'])
    conn.request("POST", '/kylin/api/cubes', json.dumps(params), headers)
    response = conn.getresponse()
    res = response.read()
    if response.status == 200:
        res = json.loads(res)
        if hasattr(res, 'exception'):
            print 'sync cube error, msg: %s, response: %s' % (res['exception'], res)
            exit(1)
        else:
            print 'sync cube success'
    else:
        print "sync cube error, msg: %s, response: %s" % (response.reason, res)
        exit(1)


def update_cube(profile, project_name, cube_json):
    params = {'project': project_name, 'cubeName': cube_json['name'], 'cubeDescData': json.dumps(cube_json)}
    headers = {"Authorization": "Basic %s" % profile['auth'], "Content-Type": "application/json"}
    conn = httplib.HTTPConnection(profile['url'])
    conn.request("PUT", '/kylin/api/cubes', json.dumps(params), headers)
    response = conn.getresponse()
    res = response.read()
    if response.status == 200:
        res = json.loads(res)
        if hasattr(res, 'exception'):
            print 'sync cube error, msg: %s, response: %s' % (res['exception'], res)
            exit(1)
        else:
            print 'sync cube success'
    else:
        print "sync cube error, msg: %s, response: %s" % (response.reason, res)
        exit(1)


def fetch_project(profile, project_name):
    headers = {"Authorization": "Basic %s" % profile['auth']}
    conn = httplib.HTTPConnection(profile['url'])
    conn.request("GET", '/kylin/api/projects?projectName=' + project_name, urllib.urlencode({}), headers)
    response = conn.getresponse()
    res = response.read()
    if response.status == 200:
        return json.loads(res)
    else:
        print("fetch project from [%s] error, error msg: %s, response: %s" % (profile['name'], response.reason, res))
        exit(1)


def main():
    opts, args = getopt.getopt(sys.argv[1:], 'f:t:mch', ['from=', 'to=', 'cube=', 'model=', 'project='])
    from_profile = None
    to_profile = None
    sync_model = False
    sync_cube = False
    cube_name = None
    model_name = None
    project_name = None

    for o, v in opts:
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
        if o in ('-m',):
            sync_model = True
        if o in ('-c',):
            sync_cube = True
        if o in ('-h',):
            print_help()
            exit(1)
        if o in ('--cube',):
            if v != '' or v is None:
                cube_name = v
            else:
                print "--cube param value [%s] is invalid" % v
                print_help()
                exit(1)
        if o in ('--model',):
            if v != '' or v is None:
                model_name = v
            else:
                print "--model param value [%s] is invalid" % v
                print_help()
                exit(1)
        if o in ('--project',):
            if v != '' or v is None:
                project_name = v
            else:
                print "--project param value [%s] is invalid" % v
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
    if sync_model is False and sync_cube is False:
        print "sync model and cube param are all False ,please resign it"
        print_help()
        exit(1)
    if sync_model is True and (project_name is None or model_name is None):
        print 'sync model should specify project name and model name '
        print_help()
        exit(1)
    if sync_cube is True and (project_name is None or model_name is None or cube_name is None):
        print 'sync cube should specify project name and model name and cube name'
        print_help()
        exit(1)
    decide = raw_input("do you have sync hive table metadata to kylin? Y or N\n")
    if decide == 'Y' or decide == 'y' or decide == 'YES' or decide == 'yes':
        pass
    else:
        print("please sync hive table metadata to kylin first.")
        exit(1)
    to_projects = fetch_project(to_profile, project_name)

    is_to_has_project_flag = False
    for project in to_projects:
        if project['name'] == project_name:
            is_to_has_project_flag = True
    if not is_to_has_project_flag:
        print "project [%s] is not exists, please make it at the [%s] UI" % (project_name, to_profile['name'])
        exit(1)

    if sync_model:
        print 'starting transfer model [%s] from [%s] to [%s]' % (model_name, from_profile['name'], to_profile['name'])
        from_models = fetch_model(from_profile, model_name)
        if len(from_models) == 0:
            print 'model [%s] is not exists in [%s]' % (model_name, from_profile['name'])
            exit(1)
        from_model = from_models[0]

        to_models = fetch_model(to_profile, model_name)
        if len(to_models) == 0:
            from_model['last_modified'] = 0L
            insert_model(to_profile, project_name, from_model)
        else:
            to_model = to_models[0]
            from_model['last_modified'] = to_model['last_modified']
            if to_profile == Prod:
                decide = raw_input("model [%s] is already exist in [%s], do you want to overwrite it? Y or N\n" % (model_name, to_profile['name']))
                if decide == 'Y' or decide == 'y' or decide == 'YES' or decide == 'yes':
                    file_path = backup_path.rstrip(os.path.sep) + os.path.sep + ('%s_model_%s_%s.json' % (to_profile['name'], to_model['name'], datetime.strftime(datetime.now(), '%Y-%m-%d_%H_%M_%S')))
                    print file_path
                    os.system("echo %s > %s" % (json.dumps(to_model), file_path))
                    update_model(to_profile, project_name, from_model)
                else:
                    print "Your operation has been cancelled."
                    exit(1)
            else:
                update_model(to_profile, project_name, from_model)

    if sync_cube:
        print 'starting transfer cube [%s] from [%s] to [%s]' % (cube_name, from_profile['name'], to_profile['name'])
        from_cubes = fetch_cube(from_profile, cube_name)
        if len(from_cubes) == 0:
            print 'cube [%s] is not exists in [%s]' % (cube_name, from_profile['name'])
            exit(1)
        from_cube = from_cubes[0]

        from_models = fetch_model(to_profile, from_cube['model_name'])
        if len(from_models) == 0:
            print 'model [%s] is not exists in [%s], please resign params to sync model' % (from_cube['model_name'], to_profile['name'])
            exit(1)

        to_cubes = fetch_cube(to_profile, cube_name)
        if len(to_cubes) == 0:
            from_cube['last_modified'] = 0L
            insert_cube(to_profile, project_name, from_cube)
        else:
            to_cube = to_cubes[0]
            from_cube['last_modified'] = to_cube['last_modified']
            if to_profile == Prod:
                decide = raw_input("cube [%s] is already exist in [%s], do you want to overwrite it? Y or N\n" % (cube_name, to_profile['name']))
                if decide == 'Y' or decide == 'y' or decide == 'YES' or decide == 'yes':
                    file_path = backup_path.rstrip(os.path.sep) + os.path.sep + ('%s_cube_%s_%s.json' % (to_profile['name'], to_cube['name'], datetime.strftime(datetime.now(), '%Y-%m-%d_%H_%M_%S')))
                    print file_path
                    os.system("echo %s > %s" % (json.dumps(to_cube), file_path))
                    update_cube(to_profile, project_name, from_cube)
                else:
                    print "Your operation has been cancelled."
                    exit(1)
            else:
                update_cube(to_profile, project_name, from_cube)


if __name__ == '__main__':
    main()
