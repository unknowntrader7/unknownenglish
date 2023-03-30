import boto3
import os
from contextlib import closing

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")

polly_client = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name='us-west-2'
).client('polly')

def text_to_speech(text):
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    with closing(response['AudioStream']) as stream:
        with open('output.mp3', 'wb') as file:
            file.write(stream.read())
