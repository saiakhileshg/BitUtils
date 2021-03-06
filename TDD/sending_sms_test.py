# written in python 3.*
#-*- coding: utf-8 -*-

#pip install coolsms_python_sdk
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import Config

# set api key, api secret for sending sms
api_key = Config.SMS_API_KEY
api_secret = Config.SMS_API_SECRET

def sendSMS(msg):
    print("sendSMS()")
    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
    params['to'] = Config.PHONE_NUMBER_WO_COUNTRYCODE # Recipients Number '01000000000,01000000001'
    params['from'] = Config.PHONE_NUMBER_WO_COUNTRYCODE # Sender number
    params['text'] = msg # Message

    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        print(("Success Count : %s" % response['success_count']))
        print(("Error Count : %s" % response['error_count']))
        print(("Group ID : %s" % response['group_id']))

        if "error_list" in response:
            print(("Error List : %s" % response['error_list']))

    except CoolsmsException as e:
        print(("Error Code : %s" % e.code))
        print(("Error Message : %s" % e.msg))

sendSMS("테스트 메시지 보냄. asdjklasjd")