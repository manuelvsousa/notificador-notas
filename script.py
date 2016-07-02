import ConfigParser #Configuration files
import urllib #Page is up
import urllib2 #get source code
import sys
import ast
import json
import hashlib
from hashlib import md5
import urllib2

################################################
FICHEIRO_CONFIG="config.ini"
FICHEIRO_DATA="teste.txt"
################################################

def is_up(link):
    return urllib.urlopen(link).getcode() == 200

def error_log(message):
    file = open("error.log", "rw+")
    line = file.write(message)
    file.close()

def ConfigSectionMap(Config,section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            error_log("#0000100001%s!" % option)
            dict1[option] = None
    return dict1

def get_sourcecode(link):
    response = urllib2.urlopen(link)
    m = hashlib.md5()
    m.update(response.read())
    return m.hexdigest()

def config_init(name):
    config = ConfigParser.ConfigParser()
    config.read(name)
    return config

def get_cadeiras(config):
    i=0
    for a in config.sections():
        if(a!="email"):
            i=i+1
        else:
            break
    return config.sections()[0:i]

def read_file_lines(file):
    with open(file) as f:
        lines = f.readlines()
    lines=[line.rstrip('\n') for line in open(file)]
    for i in range(0,len(lines)):
        json_acceptable_string = lines[i].replace("'", "\"")
        d = json.loads(json_acceptable_string)
        lines[i]=d
    return lines

def del_reverse_list_index(data,eliminar):
    for i in reversed(eliminar):
        del(data[i])

def atualizar_cadeira(data,config):
    if(is_up(data["link"])):
        md5=get_sourcecode(data["link"])
        if(md5 != data["md5"]):
            #alerta(data,config)
            altera_config(data["link"],config)
            del(data)
    else:
        error_log("IS DOWN!! " % data["link"])

def altera_config(data,config):
    config.set(data["cadeira"], data["ativo"], False)
    with open(FICHEIRO_CONFIG, 'w') as configfile:
        config.write(config)



def adicionar_cadeira(cadeira,config):
    new={}
    lista=[]
    new["cadeira"]=cadeira
    new["sigla"]=ConfigSectionMap(config,cadeira)['sigla']
    new["link"]=ConfigSectionMap(config,cadeira)['link']
    new["ativo"]=1
    new["md5"]=get_sourcecode(ConfigSectionMap(config,cadeira)['link'])
    return new




if __name__ == "__main__":
    config = config_init(FICHEIRO_CONFIG)
    cadeiras=get_cadeiras(config)
    data = read_file_lines(FICHEIRO_DATA)
    eliminar=[]
    #eliminar jsons que ja nao existem na config
    for a in range(0,len(data)):
        for b in range(0,len(cadeiras)):
            if cadeiras[b] == data[a]["cadeira"]:
                break
        if (b+1)!=len(data):
            eliminar.append(a)
    del_reverse_list_index(data,eliminar)
    #-------------------------------------
    #atualiza cadeiras e adiciona novas cadeiras
    novos=[]
    for b in range(0,len(cadeiras)):
        for a in range(0,len(data)):
            if cadeiras[b] == data[a]["cadeira"] and data[a]["ativo"]==True:
                atualizar_cadeira(data[a],config)
        if (b+1)!=len(cadeiras):
            novos.append(adicionar_cadeira(cadeiras[a],config))
    data=data+novos
    for i in data:
        print i
    #-------------------------------------




