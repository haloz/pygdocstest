import unittest
from googlesheets import GoogleSheets


class GsheetTestCase(unittest.TestCase):
    def setUp(self):
        scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
        client_secret_file = 'client_secret.json'
        application_name = 'Google Sheets API Python Quickstart'

        gs = GoogleSheets()
        self.service = gs.get_service(
            client_secret_file,
            scopes,
            application_name
        )

    def test_read_from_gsheet(self):
        spreadsheetId = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
        rangeName = 'Class Data!A2:E'
        result = self.service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName).execute()
        values = result.get('values', [])
        self.assertEqual(len(values), 30)
