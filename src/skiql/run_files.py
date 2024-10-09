from pathlib import Path

import pyodbc


def run_sql_file(file, connection):
    queries = file.read_text().split("\ngo\n")
    cur = connection.cursor()
    for query in queries:
        cur.execute(query)


def run_all_files(folders, connection_string, max_tries):
    cnxn = pyodbc.connect(connection_string)

    reruns = []

    for folder in folders:
        for file in Path(folder).glob("*.sql"):
            print(f"Running file {file}")
            try:
                run_sql_file(file, cnxn)
            except pyodbc.ProgrammingError:
                print(f"Could not run {file}")
                reruns.append(file)

    i = 0
    while reruns and i < max_tries:
        print(f"Not all files ran, rerun attempt {i + 1}")
        for file in reruns:
            print(f"Running file {file}")
            try:
                run_sql_file(file, cnxn)
            except pyodbc.ProgrammingError:
                print(f"Could not run {file}")
                pass
        i += 1

    cnxn.close()
    return reruns
