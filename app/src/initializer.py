import os
import pickle
import boto3
from tempfile import NamedTemporaryFile
from aws_lambda_powertools import Logger
from mypy_boto3_s3 import S3ServiceResource
from exceptions import DownloadModelError
from sklearn.ensemble import RandomForestClassifier

logger = Logger()

resource: S3ServiceResource = boto3.resource("s3")

def download_model(tmp_file: NamedTemporaryFile):

    try:

        s3_obj = resource.Object(bucket_name=f"{os.environ['ACCOUNT_ID']}-ml-rest-api")
        
        with open(f"/tmp/{tmp_file}", "wb") as f:
            s3_obj.download_fileobj(f)

    except Exception as e:
        logger.error(e)
        raise DownloadModelError("Model could not be downloaded.")

    else:
        logger.info("Model successfully downloaded.")

def load_model(tmp_file: NamedTemporaryFile) -> RandomForestClassifier:

    try:
        
        with open(f"/tmp/{tmp_file}", "wb") as f:
            model = pickle.load(f)

    except Exception as e:
        logger.error(e)
        raise DownloadModelError("Model could not be loaded.")

    else:
        logger.info("Model successfully loaded.")
        return model

def init_lambda():

    tmp_file = NamedTemporaryFile()
    download_model(tmp_file)
    estimator = load_model(tmp_file)

    return estimator