from google.cloud import language_v1
import requests

def keywords(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    fileName = file['name']
    analyze_entities(fileName)
    print(f"Processing file: {file['name']}.")


def analyze_entities(fileName):
    """
    Analyzing Entities in text file stored in Cloud Storage

    Args:
      gcs_content_uri Google Cloud Storage URI where the file content is located.
      e.g. gs://[Your Bucket]/[Path to File]
    """

    client = language_v1.LanguageServiceClient()

    # gcs_content_uri = 'gs://cloud-samples-data/language/entity.txt'
    gcs_content_uri = 'gs://make3400_transcripts/{0}'.format(fileName)

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"gcs_content_uri": gcs_content_uri, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
    response_array = []
    # Loop through entitites returned from the API
    for entity in response.entities:
        found_url = False
        current_entity = ''
        print(u"Entity: {}".format(entity.name))
        for metadata_name, metadata_value in entity.metadata.items():
            if 'wikipedia_url' in metadata_name:
                current_entity = "{0}|{1}".format(entity.name, metadata_value)
                found_url = True
        if not found_url:
            current_entity = "{0}|".format(entity.name)
        
        response_array.append(current_entity)
        
    send_words(fileName, response_array)

def send_words(prefix, words):
    url = "https://brickhack-8.anvil.app/_/api/keywords/{unique_id}".format(unique_id=prefix)
    content = {'response': words}
    sender = requests.post(url, data = content)
    print("Sender status: {0}".format(sender.status_code))
