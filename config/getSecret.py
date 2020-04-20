# Import the Secret Manager client library.
from google.cloud import secretmanager

# GCP project in which to store secrets in Secret Manager.
project_id = 'iconic-hue-273619'

# Create the Secret Manager client.
client = secretmanager.SecretManagerServiceClient()

def getSecret(secret_id):
    # Build the resource name of the secret version.
    name = client.secret_version_path(project_id, secret_id, 'latest')

    # Access the secret version.
    response = client.access_secret_version(name)

    return response.payload.data.decode('UTF-8')