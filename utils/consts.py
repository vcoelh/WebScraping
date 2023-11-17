# local da minha encomenda
# r"W:/Coleta Web/PROJETO PILOTO/Encomenda"
SHEET_PATH = r"W:/Coleta Web/PROJETO PILOTO/Encomenda"
#r'G:\Meu Drive\FGV\REFATORIZAÇÃO\lista de espera'


MESES = {'1': 'janeiro', '2': 'fevereiro', '3': 'marco', '4': 'abril', '5': 'maio', '6': 'junho',
         '7': 'julho', '8': 'agosto', '9': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'}

CEPS = {'AC': '69914480', 'AL': '57060530', 'AM': '69010000', 'AP': '68925147', 'PA': '66050000', 'RN': '59064902',
        'RO': '76824246',
        'RR': '69316400', 'TO': '77024028', 'DF': '70830020', 'GO': '74933130', 'MS': '79044490', 'MT': '78120665',
        'BA': '40015030', 'CE': '60720095',
        'MA': '65015330', 'PB': '58020671', 'PE': '52010000', 'PI': '64016-380', 'SE': '49015350', 'ES': '29010930',
        'MG': '30140120',
        'RJ': '22231000', 'SP': '01310000', 'PR': '80730420', 'RS': '90560005', 'SC': '88010001'}

RENAME_COLUMNS = {
    "CD_PERIOD": "Periodicidade",
    "DATA_PREVISTA": "Data Prevista",
    "CD_COLETOR": "Coletor Padrão",
    "CD_INFORM": "Código do Informante",
    "CD_INSUMO": "Código do Insumo",
    "NM_INSUMO": "Nome Insumo",
    "DS_INSUMO": "Característica Insumo",
    "CD_MARCFAB": "Marca Insumo",
    "CD_MEDIDA": "Unidade Medida Insumo",
    "QT_MED_INSUMO": "Quantidade Insumo",
    "CD_EMB": "Embalagem Insumo",
    "NR_SEQ_INSINF": "Insumo Informado",
    "CD_TPPRECO": "Tipo de Preço",
    "CD_COTACAO": "Cotação",
    "DS_SINO_NOME_INS_INSINF": "Sinônimo Insumo Informado",
    "S_OBS_INSINF": "Obs Insumo",
    "CD_JOB": "JOB",
    "PAÍS": "Pais",
    "REGIÃO": "Região",
    "ESTADO": "Estado",
    "MUNICÍPIO": "Municipio",
    "URL DO INSUMO": "URL Insumo Informado",
    "GRUPO DE COLETA": "Grupo de Coleta Insumo",
    "EAN": "EAN Insumo",
    "data_coleta": "Data do Preço",
    "VL_PRECCOL": "valor_anterior",
    "TAXA_FRETE": "Taxa do Frete",
    "preco_coleta": "Valor do Preço",
    "ELEMENTAR": "Elementar",
    "frete_coleta": "Valor do Frete"
}

REORDER_LIST = [
    "JOB",
    "Insumo Informado",
    "Sinônimo Insumo Informado",
    "Código do Informante",
    "Código do Insumo",
    "Tipo de Preço",
    "Pais",
    "Região",
    "Estado",
    "Municipio",
    "Bairro",
    "Pais_Retirada",
    "Regiao_Retirada",
    "Estado_Retirada",
    "Municipio_Retirada",
    "Bairro_Retirada",
    "Cotação",
    "Periodicidade",
    "Data do Preço",
    "Data Prevista",
    "Valor do Preço",
    "valor_anterior",
    "Moeda",
    "Preço Promocional",
    "Valor do Frete",
    "Taxa do Frete",
    "Frete Incluso",
    "Frete Nao Declarado",
    "Valor do Desconto",
    "Taxa do Desconto",
    "Desconto Incluso",
    "Desconto Não Declarado",
    "Coletor Padrão",
    "FT",
    "Justificativa Livre",
    "URL Insumo Informado",
    "Arquivo com Preço",
    "Nome Insumo",
    "Característica Insumo",
    "Especificação Insumo",
    "Marca Insumo",
    "Embalagem Insumo",
    "Quantidade Insumo",
    "Unidade Medida Insumo",
    "Grupo de Coleta Insumo",
    "Obs Insumo",
    "EAN Insumo"
]

DICT_ELEMENTOS = {
    "confirm_button": "body > header > div.container-header > div.header__content > div > div > div > div.header__right-links > div.header__minicart > div > div.minicart-free-shippingBar > form > fieldset > p > button",
    "cep_input": "#cep",
    # ".minicart-control.minicart-control--more",
    "add_quantity": '.minicart-control--more',
    "add_cart": "#main > section.product-info > div > div > div.product-infos.av-col-24.av-col-md-9.offset-md-2 > div.product-buy-content > div.product-buy > a",
                "get_shipment": ".monetary",
                "get_price": ".quantity-price .total-selling-price",
                'click_end_buy': '.minicart-checkout.button.button--medium'
}