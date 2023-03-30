import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def synthesize_speech(text):
    polly = boto3.client('polly')
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    audio_stream = response['AudioStream'].read()

    s3 = boto3.resource('s3')
    bucket_name = os.getenv('AWS_S3_BUCKET_NAME')
    object_name = f'{text}.mp3'
    s3.Object(bucket_name, object_name).put(Body=audio_stream)

    audio_url = f'https://{bucket_name}.s3.amazonaws.com/{object_name}'
    return audio_url
