import re
import json

#Test Result
#import os
#result = os.popen("top -bn 1").read()

def parse_top(result):
    data_result = result.split("\n")
    top_result = {}
    for i in data_result[1:5]:
        line = i.replace('%', '').replace(' ', '').replace('.', ',').split(":")
        item_name = line[0]
        sub_item = line[1]
        sub_item_values = re.findall("\d+,\d+|\d+", sub_item)
        sub_item_keys = re.findall("[A-z]+", sub_item)
        sub_item_dict = dict(zip(sub_item_keys, sub_item_values))

        top_result[item_name] = sub_item_dict
    top_result['process']= parse_process_data(result)
    top_result = json.dumps(top_result)

    return top_result

def parse_process_data(result):
    data_result = result.split("\n")
    proccess_keys = list(filter(None, data_result[6].split(' ')))

    proccess_result = []

    for proccess_line in data_result[7:-1]:
        proccess_values = list(filter(None, proccess_line.split(' ')))
        proccess_dict = dict(zip(proccess_keys, proccess_values))
        proccess_result.append(proccess_dict)

    return proccess_result
