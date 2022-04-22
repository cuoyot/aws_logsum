# aws_logsum

## What is this script for 
Output the loggroups with more than 1GB generated on a specific time

## Requirements

* Python3
* aws_cli
* AWS_PROFILE set to an AWS Profile that have access to the Loggroups you want to analyze 

## Variables to change

* deltadays=1 # number of days to Sum

## Output example

    # ./aws_logsum.py
    looking from 2022-04-21T11:11:20 to 2022-04-22T11:11:20
    24.08 GB /aws/lambda/prod-kpiManager
     8.37 GB /aws/lambda/prod-mmGetSubscriptionInfo
     5.82 GB /aws/lambda/prod-compareSubscriptions
     4.14 GB /aws/lambda/prod-compareContracts
     3.76 GB /aws/lambda/prod-mmGetSubscriptionBonusesInfo
     3.73 GB TTB-Logs-NATGW
     3.17 GB /aws/lambda/prod-mmGetSubscriptionProductsInfo
     3.03 GB /aws/lambda/prod-invoiceCDRByInvoice_2
     2.53 GB /aws/lambda/prod-write_dynamo_mm_trafico
     2.48 GB /aws/lambda/prod-changeSubscriptionStateActive 

