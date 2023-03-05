import sys
import os
from os.path import isdir
import json

jsonFile = 'data/links/links.json'
templateFilepath = 'templates/links.html'
outputPage = 'links.html'

f = open(jsonFile)
data = json.load(f)

content = ''
for link in data['links']:
    content = content + '<li><a href="'+link['url']+'">'+link['title']+'</a> - '+link['description']+' (<i>added by '+link['owner']+'</i>)</li>\n'

templateFile = open(templateFilepath, "r", encoding="utf8")
template = templateFile.read()
output = template.replace('{{content}}', content)
out = open(outputPage, "w", encoding="utf8")	
out.write(output)
out.close()
templateFile.close()
