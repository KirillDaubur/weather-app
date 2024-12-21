import json
from aioboto3 import Session

from services.storage import BaseStorage
from settings import Settings, get_settings


class S3Storage(BaseStorage):
    def __init__(self, settings: Settings = get_settings()):
        self.aws_access_key_id = settings.aws_access_key_id
        self.aws_secret_access_key = settings.aws_secret_access_key
        self.s3_bucket_name = settings.s3_bucket_name
        self.s3_endpoint_url = settings.s3_endpoint_url

    async def store(self, filename: str, data: dict) -> None:
        session = Session()
        async with session.client(
            "s3",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            endpoint_url=self.s3_endpoint_url
        ) as s3_client:
            await s3_client.put_object(
                Bucket=self.s3_bucket_name,
                Key=filename,
                Body=json.dumps(data)
            )

    async def load(self, filename: str) -> dict:
        session = Session()
        async with session.client(
            "s3",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            endpoint_url=self.s3_endpoint_url
        ) as s3_client:
            response = await s3_client.get_object(
                Bucket=self.s3_bucket_name,
                Key=filename
            )
            async with response["Body"] as stream:
                content = await stream.read()
                return json.loads(content)