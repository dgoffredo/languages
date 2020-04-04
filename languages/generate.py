import json
import sqlite3
import sys

db = sqlite3.connect(sys.argv[1])

# See https://iso639-3.sil.org/code_tables/download_tables for more information
query = """
select distinct Id, Ref_Name
from Language
where Scope = 'I'                  -- (I)ndividual
  and Language_Type in ('L', 'C'); -- (L)iving or (C)onstructed
"""


def quote(text):
    return json.dumps(text, ensure_ascii=False)  # let the UTF-8 flow...


# go_entries is all the (key, value) lines in the map literal in the generated
# code.
go_entries = ',\n'.join(f'    {quote(code)}: {quote(name)}'
                        for code, name in db.execute(query))

# The generated Go code is printed to standard output.
print(f"""
package languages

// Language is a three-letter ISO-639-3 language code.
type Language string

// Names maps each three-letter ISO-639-3 language code to a UTF-8 encoded name
// for the language, e.g. "aae" maps to "Arbëreshë Albanian".
var Names = map[Language]string{{
{go_entries}}}
""")
