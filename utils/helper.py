import pandas as pd
import os
import numpy as np
from calendar import isleap
from datetime import datetime
from utils.consts import RENAME_COLUMNS, REORDER_LIST, MESES, INPUT_TABLE


class DataReader:
    def __init__(self, date=datetime.now()) -> None:
        self.date = date

    def folder(self, nome_pasta):
        '''Cria uma pasta com o nome especificado e navega até ela'''
        try:
            # Converte o nome da pasta em uma string, caso ainda não seja uma
            nome_pasta = str(nome_pasta)
            # Cria o caminho completo da pasta, concatenando o diretório atual com o nome da pasta
            dir_destino = os.path.join(os.getcwd(), nome_pasta)
            # Verifica se a pasta já existe, se não existir, cria a pasta
            if not os.path.exists(dir_destino):
                # Cria a pasta com o nome especificado
                os.makedirs(dir_destino)
            # Navega para a pasta criada
            os.chdir(dir_destino)
            # Exibe mensagem de sucesso
            print(f"Foi para a pasta {nome_pasta}")
        except OSError as e:
            # Exibe mensagem de erro caso não seja possível criar a pasta
            print(f"Não foi possível criar a pasta {nome_pasta}: {e}")

    def create_folder(self, name_folder: str, informant_code: str, folder_prints: str = 'prints'):
        '''Cria as pastas necessárias para armazenar os arquivos da coleta e saída'''
        _, dt_prev_fim = self._intervalo_datas()

        main_name = f"{informant_code}_{name_folder}"
        self.folder(main_name)
        # Cria a pasta coleta_n, onde n é o ano da data prevista
        year_folder = f'coleta_{self.date.year}'
        self.folder(year_folder)

        # Cria a pasta coleta_mes, onde mes é o mês correspondente à data prevista
        month_folder = f'coleta_{MESES.get(str(self.date.month))}'
        self.folder(month_folder)

        decendio = self.request_dec(day=self.date.day)        
        self.folder(f"coleta{decendio}")

        # Cria a pasta saida_ano_mes_dia correspondente à data prevista
        self.folder(f"saida_{self.date.strftime('%Y_%m_%d')}")

        try:
            os.mkdir(folder_prints)
        except OSError as e:
            # Exibe mensagem de erro caso não seja possível criar a pasta
            print(f"Não foi possível criar a pasta {folder_prints}: {e}")
            
            
            
    c

            
    def _intervalo_datas(self):
        '''Retorna o primeiro e ultimo dia do dec referente a data passada'''
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


    def read_table(self,
                   informant_code: str,
                   input_sheet: str = INPUT_TABLE, date_filter=True):

        print('datetime now', self.date)
        dt_prev_ini, dt_prev_fim = self._intervalo_datas()
        file = self.date.strftime("encomenda_%Y%m%d.xls")
        # file = "encomenda_20231102.xls"
        sheet = pd.read_csv(f'{input_sheet}/{file}',
                            delimiter='\t',
                            encoding="ISO-8859-1",
                            dtype={'CD_INFORM': str, 'DATA_PREVISTA': str, 'NR_SEQ_INSINF': str})

        sheet = sheet[sheet.CD_INFORM == informant_code]
        for i in range(len(sheet)):
            data = sheet.iloc[i, 1].split('/')
            try:
                sheet.iloc[i, 1] = pd.Timestamp(
                    year=int('20' + data[-1]), month=int(data[1]), day=int(data[0]))
            except:
                sheet.iloc[i, 1] = pd.Timestamp(
                    year=int(data[-1]), month=int(data[1]), day=int(data[0]))

        if date_filter:
            print(dt_prev_ini, dt_prev_fim)
            sheet = sheet[sheet.DATA_PREVISTA <= dt_prev_fim]
            sheet = sheet[sheet.DATA_PREVISTA > dt_prev_ini]
        sheet['DATA_PREVISTA'] = [
            '{}/{}/{}'.format(x.day, x.month, x.year) for x in sheet['DATA_PREVISTA']]

        return sheet


class DataBuilder:

    def load_creator(self, sheet, name_website, informant_code, rename_columns=RENAME_COLUMNS, reorder_list=REORDER_LIST, date=datetime.now()) -> pd.DataFrame:

        sheet["data_coleta"] = date.strftime(
            '%d/%m/%Y')  # criando outra coluna
        # sheet.to_excel("carga_prep_teste.xls")
        sheet = sheet.rename(columns=rename_columns)
        sheet = sheet.reindex(columns=reorder_list)
        sheet = sheet.fillna("")

        print('encomenda', sheet.shape)
        dataframe = sheet[reorder_list].copy()
        print('carga', sheet.shape)
        dataframe['FT'] = np.where(dataframe['Valor do Preço'] == "", "S", "")
        dataframe['Justificativa Livre'] = np.where(dataframe['Valor do Preço'] == '',
                                                    'ITEM EM FALTA NO SITE/BOLETIM/TABELA', 'PREÇO CONFORME SITE/BOLETIM/TABELA')
        dataframe['Moeda'] = 'R$'
        dataframe['Valor do Preço'] = dataframe['Valor do Preço'].replace(
            '.', '')
        dataframe['Frete Incluso'] = ''
        # np.where(((dataframe['Tipo de Preço'] == 'AE') and (dataframe['Valor do Frete'] == '')), 'S', 'N')
        dataframe['Frete Nao Declarado'] = ''
        #np.where(((dataframe['Tipo de Preço'] == 'AE') and (dataframe['Valor do Frete'] == '')), 'S', 'N')
        dataframe['Data Prevista'] = sheet['Data Prevista']
        file_name = f"carga_{name_website}_BP{informant_code}_{date.strftime('%d_%m_%Y')}.xls"

        dataframe.to_excel(file_name, sheet_name='Carga BP', index=False)








########################################################################

    # def intervalo_datas(self):
    #     '''Retorna o primeiro e ultimo dia do dec referente a data passada'''

    #     # caso o mês seja fevereiro
    #     if self.date.month == 2:

    #         # A função isleap irá verificar se fevereiro está em um ano bissexto. Caso esteja, o mes terá 29 dias ou 28 dias.
    #         if isleap(self.date.year):
    #             max_day = 29
    #         else:
    #             max_day = 28

    #     # Os meses Abril, Junho, Setembro e Novembro são meses com 30 dias, logo o máximo será 30 dias.
    #     elif self.date.month in {4, 6, 9, 11}:
    #         max_day = 30

    #     # O restante dos meses contêm 31 dias em seu total.
    #     else:
    #         max_day = 31

    #     intervalo = [
    #         {'ini': 1, 'fim': 10},
    #         {'ini': 11, 'fim': 20},
    #         # A condicional irá obter a quantidade máxima de dias que aquele mês possui.
    #         {'ini': 21, 'fim': max_day}
    #     ]

    #     # retorna o intervalo do dec em que a data está.
    #     for dec in intervalo:
    #         if self.date.day <= dec['fim']:
    #             dt_prev_ini = dec['ini']
    #             print("Data Prevista inicial: ", dt_prev_ini)
    #             dt_prev_fim = dec['fim']
    #             print("Data Prevista final: ", dt_prev_fim)
    #             break

    #     return dt_prev_ini, dt_prev_fim