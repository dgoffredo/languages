import sqlite3
import sys

db = sqlite3.connect(sys.argv[1])

# See https://iso639-3.sil.org/code_tables/download_tables for more information
query = """
select distinct Id, Ref_Name
from Language
where Scope = 'I'                  -- (I)ndividual
  and Language_Type in ('L', 'C') -- (L)iving or (C)onstructed
  and Part1 != ''; -- corresponds to an alpha-2 language
"""

def id_from_alpha3(alpha3):
    """Return a positive integer ID corresponding to the three-letter language
    code `alpha3`. The ID is the number resulting from interpreting `alpha3`
    as base-26 big-endian unsigned integer, and then adding one. The
    offset-by-one is to reserve the value zero."""
    alpha3 = alpha3.upper()
    high, mid, low = alpha3
    origin = ord('A')
    high, mid, low = ord(high) - origin, ord(mid) - origin, ord(low) - origin
    base = 26
    return high * base**2 + mid * base**1 + low * base**0 + 1


print('enum Language {')
print('  LANGUAGE_UNSPECIFIED = 0;')
for alpha3, name in db.execute(query):
    print(f'  LANGUAGE_{alpha3.upper()} = {id_from_alpha3(alpha3)}; // {name}')

print('}')
