"""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     MobileAPP
     Python (PROJECTS)
 Module:
     main.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys
import time
import datetime

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pandas


#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LULog
# import LUFile
# import LUProc
# import LUos
# import LUObjectsYT
# import LUDateTime
# import LUStrUtils
# import LUDecotators
# import LUSheduler
# import LUConsole

#------------------------------------------
# const
#------------------------------------------
sFileName = 'G:\\SOFT-install\\03 ЮРА_ТЕЛЕФОН\\STORE\\НАСТРОЙКА\\ЯРЛЫКИ\\HM20.xlsx'

#------------------------------------------
#
#------------------------------------------
def main ():
#beginfunction
    # название электронной таблицы
    # Если в качестве значения указать список, то будет возвращён словарь датафреймов
    sheet_name = 0
    sheet_name = 'Лист1'
    # сколько строк вы хотите пропустить
    skiprows = None
    skiprows = 1
    # При установленном значении “0” используется первая строка.
    # Если у столбцов не должно быть заголовков, установите значение “None”
    header = 0
    header = 1
    # список с именами столбцов
    names = None
    # список с номерами или названиями столбцов.
    usecols = None
    #
    dtype = None
    nrows = None

    APPs = pandas.read_excel(sFileName)

    # APPs = pandas.read_excel(sFileName, sheet_name = 'Лист1',
    #                          skiprows = 1, header = 1,
    #                          names = None, usecols = None, dtype = None,
    #                          nrows = None)

    LResult = 0
    s = 'ExitProgram...'
    LULog.LoggerAPPS.info (s)
    sys.exit(LResult)
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
