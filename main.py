from datetime import datetime
import requests
import pandas as pd
from flask import Flask, jsonify

def create_csv_archive():
    packages = [
    'numpy',
    'pandas',
    'matplotlib',
    'scikit-learn',
    'tensorflow',
    'django',
    'flask',
    'requests',
    'beautifulsoup4',
    'pytest',
    'pytorch',
    'opencv-python',
    'seaborn',
    'plotly',
    'pyyaml',
    'tqdm',
    'sqlalchemy',
    'nltk',
    'jupyter',
    'pymongo',
    'flask-restful',
    'pyinstaller',
    'wxpython',
    'pillow',
    'pyqt5',
    'pydot',
    'pylint',
    'pygame',
    'keras',
    'cx-Freeze',
    'fastapi',
    'pyodbc',
    'openpyxl',
    'xlrd',
    'xlwt',
    'pyspark',
    'paramiko',
    'psycopg2',
    'scipy',
    'bokeh',
    'statsmodels',
    'dash',
    'pytz',
    'networkx',
    'pymysql',
    'pyserial',
    'google-api-python-client',
    'python-docx',
    'pywin32',
    'pycairo',
    'pygments',
    'pandasql',
    'scrapy',
    'pyarrow',
    'torchvision',
    'fasttext',
    'xgboost',
    'keras-tuner',
    'gensim',
    'pygraphviz',
    'pycryptodome',
    'fuzzywuzzy',
    'redis',
    'tweepy',
    'pyspellchecker',
    'imaplib',
    'pydantic',
    'selenium',
    'pycurl',
    'pdfminer.six',
    'pyqrcode',
    'weasyprint',
    'pdfkit',
    'python-telegram-bot',
    'dash-bootstrap-components'
    ]

    packages_info = {
        'Package name': [],
        'Publicantion Data': [],
        'Version of Python': [],
        'Last month downloads': []
    }

    for package in packages:
        response = requests.get(f'https://pypi.org/pypi/{package}/json')

        if response.status_code == 200:
            data= response.json()

            packages_info['Package name'].append(package)

            #Date of most recent version     
            releases = data['releases']       
            latest_release_date = None
            for date in releases.keys():
                try:
                    parsed_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
                    if not latest_release_date or parsed_date > latest_release_date:
                        latest_release_date = parsed_date
                except ValueError:
                    pass
                
            if latest_release_date:
                packages_info['Publicantion Data'].append(
                    latest_release_date.strftime('%Y-%m-%d')
                )
            else:
                last_upload_time = data['urls'][0]['upload_time']
                latest_release_date = datetime.strptime(last_upload_time, '%Y-%m-%dT%H:%M:%S')
                packages_info['Publicantion Data'].append(
                    latest_release_date.strftime('%Y-%m-%d')
                )

            #Python Version
            requires_python = data['info']['requires_python']
            packages_info['Version of Python'].append(requires_python if requires_python else 'N/A')

            #Last month downloads
            last_month_downloads = sum([release['last_month'] for release in releases.values() if 'last_month' in release])
            packages_info['Last month downloads'].append(last_month_downloads)
        else: 
            packages_info['Package name'].append(package)
            packages_info['Publicantion Data'].append('N/A')
            packages_info['Version of Python'].append('N/A')
            packages_info['Last month downloads'].append('N/A')
    
    df = pd.DataFrame(packages_info)
    df.to_csv('packages.csv', index=False)



#API

app = Flask(__name__)

#Route GET returning list of packages and their information (http://localhost:5000/packages)

@app.route('/packages', methods=['GET'])
def get_packages():
    df = pd.read_csv('packages.csv')
    packages = df.to_dict('records')
    return jsonify(packages)

if __name__ == '__main__':
    create_csv_archive()
    app.run()
