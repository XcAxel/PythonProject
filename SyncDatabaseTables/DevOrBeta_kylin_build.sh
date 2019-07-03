#!/bin/sh
logInfo()
{
	echo "[INFO] "`date +"%Y-%m-%d %H:%M:%S"`" - $*"
}
logError()
{
	echo "[ERROR] "`date +"%Y-%m-%d %H:%M:%S"`" - $*"
}

########################
#判断上一步操作如果失败，则退出
########################
asertExecute()
{
	if [ $? -gt 0 ]; then
		if [ -n "$1" ]; then
			logError "$1"
		fi
		exit 1
	fi
}

if [ $# -ne 3 ]; then
    echo "Usage: $0 cube_name kylin_auth kylin_url"
    exit 1
fi

cube_name=$1
kylin_auth=$2
kylin_url=$3
start_time=631123200000
end_time=2524579200000

cube_name_1=${cube_name}

logInfo curl -H "Authorization: Basic ${kylin_auth}" http://${kylin_url}/kylin/api/cubes/${cube_name_1}
cube_info_1=`curl -H "Authorization: Basic ${kylin_auth}" http://${kylin_url}/kylin/api/cubes/${cube_name_1}`
cube_status_1=${cube_info_1%%\",\"segments\":*}
cube_status_1=${cube_status_1##*,\"status\":\"}
logInfo ${cube_name_1}" status is "${cube_status_1}

to_build_cube_name=$cube_name_1
to_build_cube_status=$cube_status_1

logInfo "ready to build "$to_build_cube_name

logInfo curl -X PUT -H "Authorization: Basic ${kylin_auth}" -H 'Content-Type: application/json' -d '{"startTime":'${start_time}', "endTime":'${end_time}', "buildType":"BUILD"}' http://${kylin_url}/kylin/api/cubes/${to_build_cube_name}/build
build_response=`curl -X PUT -H "Authorization: Basic ${kylin_auth}" -H 'Content-Type: application/json' -d '{"startTime":'${start_time}', "endTime":'${end_time}', "buildType":"BUILD"}' http://${kylin_url}/kylin/api/cubes/${to_build_cube_name}/build`
if [[ "$build_response" =~ "\"exception\":" ]]
then
    logError $build_response
    exit 1
fi

job_id=${build_response:9:36}
logInfo ${to_build_cube_name}" start building..., JOB_ID="$job_id

status=PENDING
while [ "$status" = "RUNNING" -o "$status" = "PENDING" ]
do
    status_response=`curl -H "Authorization: Basic ${kylin_auth}" http://${kylin_url}/kylin/api/jobs/${job_id}`
    status=${status_response##*\"job_status\":\"}
    process=${status##*\"progress\":}
    status=${status%%\",\"progress\"*}
    process=${process%\}}
    logInfo ${to_build_cube_name}" build status: "${status}" , process : "${process}
    sleep 15
done

if [ "$status" = "FINISHED" ];then
    logInfo ${to_build_cube_name}" build status: FINISHED"
    exit 0
else
    logInfo ${to_build_cube_name}" build status: "${status}
    exit 1
fi
