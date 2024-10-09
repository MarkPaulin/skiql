# skiql

skiql is a small python package for running a bunch of SQL files. This is to solve that issue where you have a lot of SQL files for functions, views, stored procedures and whatever else, you change the name of a column in a single table, then you need to follow that the whole way through and make sure everything has been synced up. So why not just run everything.

## Installation

Open a terminal in this directory and run `py -m pip install .` to install.

## Usage

Basic usage is like this:

```{shell}
py -m skiql sql/functions sql/views --connection_string "driver={something};server=my-server;database=my_database;" --max_tries 5
```

Arguments: a list of names of folders that contain the SQL files you want to run

Options:
* `connection_string` - connection string for the database you need to use. This gets passed to `pyodbc.connect()`, there's some useful documentation [here](https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows).
* `max_tries` - how many times to try and run files that don't work on the first go. Say you're updating a view and a stored procedure that uses that view, if the script for the stored procedure runs first then it might not work because the view hasn't been updated with a new column. `skiql` works round this in a very lazy way by just running things a few times to see if that fixes it. Default is 2.

If you don't want to have to type out your connection string every time (or you want a really high number of retries for some reason), you can create a TOML file called ".skiql" in the folder you're working in and set the options there, eg:

```{toml}
# .skiql
[options]
connection_string = "driver={something};server=my-server;database=my_database;"
max_tries = 20
```

