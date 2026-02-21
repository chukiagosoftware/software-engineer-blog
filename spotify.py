import pandas as pan
import json
from pathlib import Path

import pandas as pd

file = Path('/Users/ericarellano/MyData/YourLibrary.json')
with open(file) as f:
    lib = json.loads(f.read())
tracks = pd.DataFrame(lib['tracks'])
albums = pd.DataFrame(lib['albums'])
pass