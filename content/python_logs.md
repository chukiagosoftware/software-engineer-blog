Title: Analyzing Logs with Python
Category: Python
Tags: , SRE, DevOps, Data Science
Date: September 18, 2022
Summary: Python logs with Regex and Pandas

### The logfile, old frenemy  :poop: 

From time to time, shit happens. In this trying time, you will have no choice but to review some logs. Times 
have changed and whereas our tools of choice used to be *egrep*, *Notepad++* or a good old *Nagios* handler.  Now most 
likely you will be reading logs in a fancy colorful GUI running *Grafana*, *Kibana*, *Datadog* or whathaveyou 
replacement 
tool your employer has had the brilliant idea to use instead of industry best practices  :smile:

Take this Revolutionary moment in time:

---
time="1968-05-02 00:08:49.150" level=MERDE msg="[ Paris is on Fire! ] \"DELETE https://capitalism from A.
Bunch.of.Situationists - 200 200B in 3100 µs"
---

:fire:
How do we find out how many people revolted against capitalism in Paris, May of 1968? Well, we analyze the logs.

### Using Regex

You might not be able to get away with using Regex for logs, not until you fix them up a bit. What Data Scientists 
like to call "Extract" and "Transform", or "Data preparation"

But for now, let's assume that the Paris anarchists decided to generate some nice and orderly, mostly uniform logs.  
Here, Pythons regex engine or built-in module *re* can shine.  

#### Method:

1. Build a regular expression to match your desired log classification information, such as the Time, Date, visited 
   URL, HTTP status code, level of mayhem, error count, etc.  For example:
   

      hours = r'\d\d\d\d-\d\d-\d\d\s\d\d'


2. Use Python's find_all, match or other appropriate method to gather all the results you need in one place.

       datum = open(log_file).readlines()   
       re.findall(hours, datum)
 

3. Use Python collections.Counter to find the most prevalent hour of revoutionary strife, the most visited URL, or 
   other interesting data points.

    
    the_most = Counter(list("find results"))

#### The code:

    from pathlib import Path
    import sys
    from collections import defaultdict, Counter
    import re
    
    logs_dir = Path('.')
    
    logs_files = logs_dir.iterdir()
    list_files = []
    data_files = []
    
    INFO_re = 0
    ERROR_re = 0
    
    hours_re = []
    minutes_re = []
    
    for file in logs_files:
        if file.suffix == ".py":
            continue
        list_files.append(file)
    
    total_lines = 0
    datum = ''
    for file in list_files:
        with open(file, 'r') as f:
            datum += f.read()
    
    hours = re.findall(r'\d\d\d\d-\d\d-\d\d\s\d\d', datum)
    minutes = re.findall(r'\d\d\d\d-\d\d-\d\d\s\d\d:\d\d', datum)
    
    hours_counter = Counter(hours)
    minutes_counter = Counter(minutes)
    max_hour = hours_counter.most_common(1)
    max_minute = minutes_counter.most_common(1)
    
    INFO_re += len(re.findall(r'level=info', datum))
    ERROR_re += len(re.findall(r'level=error', datum))
    
    URL_re = re.findall(r'https?://[.\w\d/]*\s', datum)
    u = Counter(URL_re)
    top_5 = u.most_common(5)
    
    lines = datum.split('\n')
    total_lines += len(lines)
    
    print(f"Top hour: {max_hour}", f"Top minute: {max_minute}")
    
    print(f"5 most common urls: {top_5}")
    print(f"Info lines by regex: {INFO_re}")
    print(f"Info lines by regex: {ERROR_re}")
    print(f"We have {total_lines} total lines")

### Using Pandas  :panda_face:

Yeah but, that's old school, right? Everyone wants to use Pandas nowadays, and we are onboard. Pandas is 
amazing, powerful and fast.  However, it doesn't magically read all your data in the fields you want, still gotta do 
the data preparation. 

At a large scale, we can call this "Extract, Transform and Load" and send it through some 
fancy "data pipelines", "Kafka stream", "Hadoops" :basketball: and thus we enter the realm of Data Engineering. 

But on a small scale, it's just some Pyton file, buffer and string manipulation, wrangling with Dates, and figuring out 
again which are our special regular expressions to be found and catalogued.

#### The code:

      import pandas as pd
      from pathlib import Path
      import re
      
      logs_dir = Path('.')
      logs_files = logs_dir.iterdir()
      
      lines = []
      fields = None
      
      for file in logs_files:
          if file.suffix == ".py":
              continue
          with open(file) as f:
              while ln := f.readline():
                  if fields is None:
                      spaces = ln.split(" ")
                      fields = len(spaces)
                  spaces = ln.split(" ")
                  current_fields = len(ln.split(" "))
                  if current_fields != fields:
                      print(f"Non-standard line ignored: {ln}")
                      continue
                  date = spaces[0].split("=")[1].strip('"').strip("'")
                  time = spaces[1].strip('"').strip("'")
                  datetime = date + " " + time
                  level = spaces[2].split('=')[1].strip("'").strip('"')
                  msg = ' '.join(spaces[3:]).split('=')[1].strip("\n").strip('"')
                  if match := re.search(r'(https?://[\w./]*)\s', msg):
                      url = match.group(0)
                  else:
                      url = None
                  date_fmt = "%Y-%m-%dT%H:%M:%S.%f%z"
                  lines.append([datetime, level, url, msg])
      
      names = ["datetime", "level", "url", "msg"]
      df = pd.DataFrame(lines, columns=names)
      print(df.url.value_counts())

There we go. :swimmer: in the world of Data, we are! :chart:
