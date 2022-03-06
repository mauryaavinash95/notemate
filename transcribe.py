def transcribe(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    print(f"Processing file: {file['name']}.")
    fileName = file['name']
    expectedFileType = ['mp3', 'wav', 'webm']
    if fileName.split('.')[-1] in expectedFileType:
        transcribe_gcs(fileName)
    else:
        print("File type not supported!")


def transcribe_gcs(fileName):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud import storage

    gcs_uri = "gs://make3400_audiofiles/{0}".format(fileName)
    prefix = fileName.split('.')[0]
    client = speech.SpeechClient()
    gcs = storage.Client()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        language_code="en-US",
    )
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)
    fullContent = ''

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        fullContent.join(result.alternatives[0].transcript.join('\n'))
        print(u"{}".format(result.alternatives[0].transcript))
    
    textFileName = prefix + '.txt'
    targetBucket = gcs.get_bucket("make3400_transcripts")
    blob = targetBucket.blob(textFileName)
    send_transcript(prefix, fullContent)
    blob.upload_from_string(fullContent)

def send_transcript(prefix, transcript):
    import requests
    url = "https://brickhack-8.anvil.app/_/api/transcript/{unique_id}".format(unique_id=prefix)
    content = {'response': transcript}
    sender = requests.post(url, data = content)
    print("Sender status: {0}".format(sender.status_code))
