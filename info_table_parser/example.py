from config import *
import info_table_parser as itp

table = itp.init_table(URL)

print(itp.get_columns_indexes(table))
