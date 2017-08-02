from __future__ import print_function
from oauth2client import tools
from googlesheets import GoogleSheets


def main():
    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/sheets.googleapis.com-python-quickstart.json
    scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    client_secret_file = 'client_secret.json'
    application_name = 'QA-KPI python tool'

    gs = GoogleSheets()
    service = gs.get_service(
        client_secret_file,
        scopes,
        application_name
    )

    spreadsheetId = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    rangeName = 'Class Data!A2:E'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))


if __name__ == '__main__':
    main()
