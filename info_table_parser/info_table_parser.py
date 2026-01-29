import requests
import csv
import io
import json
from pathlib import Path

def init_table(url: str) -> list[list[str]]:
    response = requests.get(url)
    response.raise_for_status()

    text = response.content.decode("utf-8")
    reader = csv.reader(io.StringIO(text))
    table = []

    for row in reader:
        table.append(row)

    return table


def get_columns_indexes(table: list[list[str]]) -> tuple[int ,list[int]]:
    surname_index = -1
    marks_indexes = []

    for i in range(len(table[0])):
        if(table[0][i] == "Фамилия"):
            surname_index = i
            break

    for i in range(len(table[1])):
        if(table[1][i][:1].lower() == "о"):
            marks_indexes.append(i)

    return surname_index, marks_indexes
