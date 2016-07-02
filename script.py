import ConfigParser #Configuration files
import urllib #Page is up
import urllib2 #get source code
import sys
import ast
import json

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
    return response.read()

def config_init(name):
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
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


print is_up("http://google.com")



if __name__ == "__main__":
    config = config_init("config.ini")
    cadeiras=get_cadeiras(config)
    data = read_file_lines("teste.txt")
    eliminar=[]
    #eliminar jsons que ja nao existem na config
    for a in range(0,len(data)):
        for b in range(0,len(cadeiras)):
            if cadeiras[b]==data[a]:
                break
        if (b+1)!=len(data):
            eliminar.append(a)
    del_reverse_list_index(data,eliminar)
    #-------------------------------------
    adicionar=[]
    for a in range(0,len(cadeiras)):
        for b in range(0,len(data)):
            if cadeiras[b]==data[a]:
                atualizar_cadeira()
        if (b+1)!=len(cadeiras):
            adicionar_cadeira(data,cadeiras[i],config)





