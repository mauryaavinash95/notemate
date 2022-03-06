import re
from google.cloud import storage
from gensim.summarization import summarize

def summarization(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    print(f"Processing file: {file['name']}.")
   
    client = storage.Client()
    bucket_name = 'make3400_transcripts'
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob(file['name'])
    document = blob.download_as_string()
    document = re.sub(r'\n|\r', ' ', document.decode("utf-8", "ignore"))
    document = re.sub(r' +', ' ', document)
    document = document.strip()
    textSummary = summarize(document, word_count=75, split=False)
    send_summary(file['name'].split('.')[0], textSummary)
    print(f"{file['name']} summarized.")


def send_summary(prefix, summary):
    import requests
    url = "https://brickhack-8.anvil.app/_/api/summary/{unique_id}".format(unique_id=prefix)
    content = {'response': summary}
    sender = requests.post(url, data = content)
    print("Sender status: {0}".format(sender.status_code))
