import sys
import os
from os.path import isdir
import json
from datetime import datetime

isTest = False
testTids = [1]

def readEncodedFile(file):
    try:
        f = open(file, encoding='utf-8')
        content = json.load(f)
        f.close()
    except:
        f = open(file, encoding='iso-8859-1')
        content = json.load(f)
        f.close()
    return content


def genPage(group, tid, md):
    dataPath = group+'data/topics/'
    topicJsonFile = dataPath+str(tid)+'.json'

    templateFilepath = 'templates/topic.html'
    outputPage = group+'forum/'+str(tid)+'.html'
    
    topic = readEncodedFile(topicJsonFile)
    
    templateFile = open(templateFilepath, "r", encoding="utf8")
    template = templateFile.read()
    output = template.replace('{{group}}', group.replace('_', ' ').replace('/', ' '))
    output = output.replace('{{title}}', md['subject'])
    
    content = ''
    messages = sorted(topic['messages'], key=lambda msg: msg['msgId'])
    for msg in messages:
        content = content + '<div id="msg-'+str(msg['msgId'])+'">\n'
        
        date = datetime.fromtimestamp(int(msg['postDate']))
        content = content + '#'+str(msg['msgId'])+' ['+date.strftime('%Y-%m-%d %H:%M:%S')+']\n'
        
        if isTest:
            content = content + ' '+str(msg['msgId'])+' '+str(msg['prevInTopic'])+' '+str(msg['nextInTopic'])+'\n'
            
        content = content + '<h3>'
        if msg['prevInTopic'] != 0:
            content = content + '<a href="#msg-'+str(msg['prevInTopic'])+'">&gt;</a> '
        subject = '(no subject)'
        if 'subject' in msg:
            subject = msg['subject']
        content = content + subject+'</h3>\n'
        
        author = '(no author)'
        if 'profile' in msg:
            author = msg['profile']
        elif 'authorName' in msg:
            author = msg['authorName']
        elif 'from' in msg:
            author = msg['from']
        content = content + 'by <i>'+author+'</i>\n<br/><br/>\n'
        
        content = content + msg['messageBody']+'\n<br/>\n'
        
        if msg['prevInTopic'] != 0:
            content = content + '<a href="#msg-'+str(msg['prevInTopic'])+'">[Previous]</a> '
        if msg['nextInTopic'] != 0:
            content = content + '<a href="#msg-'+str(msg['nextInTopic'])+'">[Next]</a>'
            
        content = content + '\n</div>\n<hr/>\n\n'
        
    output = output.replace('{{content}}', content)
    
    out = open(outputPage, "w+", encoding="utf8")	
    out.write(output)
    out.close()
    templateFile.close()
    
    

def genIndex(group):
    dataPath = group+'data/topics/'
    topicIdsFile = dataPath+'retrievedTopicIds.json'
    metadataFiles = {'': ['message_metadata_0.json', 'message_metadata_1.json', 'message_metadata_2.json', 'message_metadata_3.json'], 'Spy_Division/': ['message_metadata_0.json']}

    templateIndexFilepath = 'templates/topics.html'
    indexPage = group+'forum.html'


    f = open(topicIdsFile)
    topicIds = json.load(f)
    f.close()
    topicIds.sort(reverse=True)
    if isTest:
        topicIds = testTids

    metadataList = []
    for mf in metadataFiles[group]:
        md = readEncodedFile(dataPath+mf)
        metadataList.extend(md['messages'])
        

    print(len(metadataList))

    metadata = {}
    for md in metadataList:
        metadata[md['messageId']] = md

    content = ''
    for tid in topicIds:
        md = metadata[tid]
        date = datetime.fromtimestamp(md['date'])
        author = md['yahooAlias'] if md['yahooAlias'] != "" else md['email']
        nReplies = md['numRecords']
        if nReplies > 0:
            nReplies = nReplies-1
        if nReplies == 1:
            nReplies = str(nReplies) + ' reply'
        else:
            nReplies = str(nReplies) + ' replies'
            
        content = content + '<li>#'+str(tid)+' <b>['+date.strftime('%Y-%m-%d %H:%M')+']</b> '
        content = content + '<a href="forum/'+str(tid)+'.html">'+md['subject']+'</a> '
        content = content + '<b>('+nReplies+')</b> '
        content = content + '- <i>'+author+'</i><br/>\n'
        content = content + md['summary']+'...</li>\n'
        genPage(group, tid, md)

    templateIndexFile = open(templateIndexFilepath, "r", encoding="utf8")
    templateIndex = templateIndexFile.read()
    output = templateIndex.replace('{{group}}', group.replace('_', ' ').replace('/', ' '))
    output = output.replace('{{content}}', content)
    out = open(indexPage, "w", encoding="utf8")	
    out.write(output)
    out.close()
    templateIndexFile.close()
    

genIndex('')
genIndex('Spy_Division/')

