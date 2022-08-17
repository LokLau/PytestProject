from Utilities import configreader
from Utilities import excelreader


def data_provider(sheet_name):
    path = configreader.read_config("basic info", "data_path")
    return excelreader.get_excel_data(path, sheet_name)