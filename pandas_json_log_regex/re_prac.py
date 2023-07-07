import re

pattern = r'apple'
text = 'An apple a day keeps doctor away.'

# Match
match = re.match(pattern, text)
if match:
    print('Match found:', match.group())
else: print('No match found')

# Search
search = re.search(pattern, text)
if search:
    print('Search found:', search.group())

# Find all occurrences
matches = re.findall(pattern, text)
print('All occurrences:', matches)

# Replace
replaced_text = re.sub(pattern, 'orange', text)
print('Replaced text:', replaced_text)
