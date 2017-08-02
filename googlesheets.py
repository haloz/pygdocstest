import httplib2
import os

from apiclient import discovery
from oauth2client.file import Storage
from oauth2client import client
from oauth2client import tools


class GoogleSheets:
    def get_credentials(self, secret_file, scopes, application_name):
        """
        Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(
            credential_dir,
            'sheets.googleapis.com-python-qa-kpi.json'
        )

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(secret_file, scopes)
            flow.user_agent = application_name
            credentials = tools.run_flow(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def get_service(self, secret_file, scopes, application_name):
        credentials = self.get_credentials(
            secret_file,
            scopes,
            application_name
        )
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = (
            'https://sheets.googleapis.com/$discovery/rest?version=v4'
        )
        service = discovery.build(
            'sheets',
            'v4',
            http=http,
            discoveryServiceUrl=discoveryUrl
        )
        return service
