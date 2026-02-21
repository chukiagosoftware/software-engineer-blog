import os
import re
import glob

# Directory to search
content_dir = 'content'

# Regex pattern: : followed by word chars, then :
pattern = r':([a-zA-Z0-9_]+):'
replacement = r'{{< emoji \1 >}}'

# Find all .md files
md_files = glob.glob(os.path.join(content_dir, '**', '*.md'), recursive=True)

for file_path in md_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace using regex
        new_content = re.sub(pattern, replacement, content)
        
        # Write back only if changed
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print("Emoji replacement complete.")