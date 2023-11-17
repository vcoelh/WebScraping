from datetime import datetime

from sqlalchemy import create_engine

from scraper import BOOK

date = datetime.now().strftime('%d_%m_%y')
host = 'localhost'
user = 'root'
password = '!v20182014V'
database = 'dataframe'
table = f'coleta_{date}'
connection = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'


if '__main__' == __name__ :
    book = BOOK()
    sheet = book.scraper()
    
    engine = create_engine(connection)

    sheet.to_sql(name=table, con=engine, if_exists='replace', index=False)
        