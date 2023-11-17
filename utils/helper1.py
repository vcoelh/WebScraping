from datetime import datetime
from datetime import timedelta
from typing import Union
import os

import pandas as pd

from .consts import SHEET_PATH, MESES, REORDER_LIST, RENAME_COLUMNS


class DataReader:
    def __init__(self, delay: int = 0, date_filter: bool = True) -> None:
        self.date = datetime.now() - timedelta(delay)
        self.date_filter = date_filter
        self.dt_ini, self.dt_end = Folder._intervalo_datas()
        return None
        
    
    def get_sheet(self,
                  informant: str,
                  path: str = SHEET_PATH,
                 ):
        
        
        file = self.date.strftime("encomenda_%Y%m%d.xls")
        
        sheet = pd.read_csv(f'{path}/{file}',
                            delimiter='\t',
                            encoding="ISO-8859-1",
                            dtype={'CD_INFORM': str,
                                   'DATA_PREVISTA': str,
                                   'NR_SEQ_INSINF': str
                                   }
                           )
        
        sheet = sheet[sheet.CD_INFORM == informant]
        
        for _, row in sheet.iterrows():
                    data = row[1].split('/')
                    try:
                        row[1] = pd.Timestamp(
                                            year=int('20' + data[-1]), month=int(data[1]), day=int(data[0])
                                             )
                    except:
                        row[1] = pd.Timestamp(
                                            year=int(data[-1]), month=int(data[1]), day=int(data[0])
                                             )
        self.filter()

    
    def filter(self):
        match self.date_filter:
            case True:
                
                print(dt_prev_inicio, dt_prev_fim)
                sheet = sheet[sheet.DATA_PREVISTA <= dt_prev_fim]
                sheet = sheet[sheet.DATA_PREVISTA > dt_prev_inicio]
                sheet['DATA_PREVISTA'] = [
                                        f"{x.day}/{x.month}/{x.year}" for x in sheet['DATA_PREVISTA']
                                        ]
            case False:
                pass
            
        
class Folder(DataReader):
        def __init__(self) -> None:
             return None
                
        @staticmethod
        def request_dec(day: int) -> str:
            """
            Conditional insert DEC for directory based on current date

            Args:
                day [int]
            Return:
                dec [str]
            """
            print("Defining DEC to export information")
            if day <= 10:
                return "_1_dec"
            if 10 < day <= 20:
                return "_2_dec"
            if 20 < day <= 31:
                return "_3_dec"

        @classmethod
        def _intervalo_datas(self):
            '''Retorna o primeiro e ultimo dia do dec referente a data passada''')
            if self.date.day <= 10:
                dt_prev_inicio = pd.Timestamp(
                    year=self.date.year, month=self.date.month, day=1)
                dt_prev_fim = pd.Timestamp(
                    year=self.date.year, month=self.date.month, day=10)
            elif 10 < self.date.day <= 20:
                dt_prev_inicio = pd.Timestamp(
                    year=self.date.year, month=self.date.month, day=11)
                dt_prev_fim = pd.Timestamp(
                    year=self.date.year, month=self.date.month, day=20)
            else:
                dt_prev_inicio = pd.Timestamp(
                    year=self.date.year, month=self.date.month, day=21)
                dt_prev_fim = pd.Timestamp(
                    year=self.date.year, month=self.date.month, day=30)
            return dt_prev_inicio, dt_prev_fim
