import json
# import sklearn
# import pandas as pd 
from tester.test import dummy_function

def lambda_handler(event, context):
   return {
      "statusCode": 200,
      "headers": {
         "Content-Type": "application/json"
      },
      "body": json.dumps(
         {"Version ": dummy_function(1,5)}
      )
   }