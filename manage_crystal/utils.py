import re

def strip_uncertainity(data): 
  return float(re.sub(r'\([^)]*\)', '', data)
