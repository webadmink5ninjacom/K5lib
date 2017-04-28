from os import environ as env
import k5lib
import logging
import json

# add filemode="w" to overwrite
logging.basicConfig(filename="get_project_info.log", level=logging.DEBUG)

username = env['OS_USERNAME']
password = env['OS_PASSWORD']
domain = env['OS_USER_DOMAIN_NAME']
projectName = env['OS_PROJECT_NAME']
region = env['OS_REGION_NAME']

projectToken = k5lib.get_project_token(username,password,domain,projectName,region)
queueInfo = k5lib.get_image_import_queue_status(projectToken)
print(json.dumps(queueInfo, indent = 2))
