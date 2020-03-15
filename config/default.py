import os
import urllib

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY') or 'not-the-droid-youre-looking-for'

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLSERVER = {
    'user': 'sa',
    'pw': '123$sa4',
    'server': 'CORPUS1',
    'db': 'test_fk',
    'host': 'corpus.zapto.org',
    'port': '1433',
    'odbc': '{ODBC Driver 17 for SQL Server}'
}

CONN_STRING = (
    f"DRIVER={SQLSERVER['odbc']};SERVER={SQLSERVER['server']};"
    f"DATABASE={SQLSERVER['db']};UID={SQLSERVER['user']};"
    f"PWD={SQLSERVER['pw']}"
)
conn_params = urllib.parse.quote_plus(CONN_STRING)
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % conn_params
# SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:123$sa4@https://corpus.zapto.org:1433/test_fk'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True
