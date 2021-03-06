#!/usr/bin/env python3

# Outputs all loggroups with > 1GB of incomingBytes in the past N days

import boto3
from datetime import datetime as dt
from datetime import timedelta, date, time, datetime
deltadays=1 # number of days to Sum
output_list = []


logs_client = boto3.client('logs')
cloudwatch_client = boto3.client('cloudwatch')

localdate = datetime.combine(dt.today(), time()) #looking for exact dates
end_date = localdate.isoformat(timespec='seconds')
start_date = (localdate - timedelta(days=deltadays)).isoformat(timespec='seconds')
print("looking from %s to %s" % (start_date, end_date))

paginator = logs_client.get_paginator('describe_log_groups')
pages = paginator.paginate()
for page in pages:
     for json_data in page['logGroups']:
        log_group_name = json_data.get("logGroupName") 

        cw_response = cloudwatch_client.get_metric_statistics(
           Namespace='AWS/Logs',    
           MetricName='IncomingBytes',
           Dimensions=[
            {
                'Name': 'LogGroupName',
                'Value': log_group_name
            },
            ],
            StartTime= start_date,
            EndTime=end_date,
            Period=3600 * 24 * 7,
            Statistics=[
                'Sum'
            ],
            Unit='Bytes'
        )
        if len(cw_response.get("Datapoints")):
            stats_data = cw_response.get("Datapoints")[0]
            stats_sum = stats_data.get("Sum")   
            sum_GB = stats_sum /  (1000 * 1000 * 1000)
            if sum_GB > 1.0:
                output_list.append([sum_GB , log_group_name])
output_list.sort(reverse=True)
for result in output_list:
    print("%8.2f GB %s" % (result[0],result[1]))