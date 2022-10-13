import os
import boto3
import pickle
from tempfile import NamedTemporaryFile

from exceptions import DownloadModelError, LoadModelError
from sklearn.ensemble import RandomForestClassifier
from aws_lambda_powertools import Logger

from mypy_boto3_s3 import S3ServiceResource

logger = Logger()
resource: S3ServiceResource = boto3.resource('s3')

def download_model(tmp_file: NamedTemporaryFile) -> None:

    try:
        
        s3_obj = resource.Object(bucket_name=f'{os.environ["ACCOUNT_NUMBER"]}-ml-rest-api',
                                 key='model.pickle')

        with open(f"/tmp/{tmp_file}", 'wb') as file:
            s3_obj.download_fileobj(file)
                           
    except Exception as e:
        raise DownloadModelError("Error while downloading the model")

    else:
        logger.info("Model successfully downloaded")


def load_model(tmp_file:NamedTemporaryFile) -> RandomForestClassifier:

    try:

        with open(f"/tmp/{tmp_file}", 'rb') as f:
            data = pickle.load(f)

    except Exception as e:
        raise LoadModelError("Error while loading the model")

    else:
        logger.info("Model successfully loaded")
        return data

def init_lambda():
    tmp_file = NamedTemporaryFile()
    download_model(tmp_file)
    estimator = load_model(tmp_file)

    return estimator
