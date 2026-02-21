import re
from pathlib import Path

# Mapping of month names to numbers
MONTHS = {
    'January': '01', 'February': '02', 'March': '03', 'April': '04',
    'May': '05', 'June': '06', 'July': '07', 'August': '08',
    'September': '09', 'October': '10', 'November': '11', 'December': '12'
}

def fix_date(content):
    # Regex to match date: Month DD, YYYY
    pattern = r'date: (\w+) (\d{1,2}), (\d{4})'
    def replace(match):
        month, day, year = match.groups()
        month_num = MONTHS[month]
        day_num = f"{int(day):02d}"  # Zero-pad day
        return f'date: {year}-{month_num}-{day_num}'
    return re.sub(pattern, replace, content)

# Process all .md files in content/posts
posts_dir = Path('./content/posts')
for md_file in posts_dir.glob('*.md'):
    content = md_file.read_text(encoding='utf-8')
    new_content = fix_date(content)
    md_file.write_text(new_content, encoding='utf-8')
    print(f'Fixed date in {md_file.name}')

print('All dates fixed!')
