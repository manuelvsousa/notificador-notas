# Notificador de Notas

Script que deteta alteracões de paginas WEB, e envia notificações através de emails e SMS. Composto por um sistema de configuração de fácil utilização.

#### Modos de Utilização

O Script foi feito de modo a operar de 2 maneiras. Sobre uma sessao screen ou sobre um crontab. No ficheiro de configuração do script é possivel escolher a maneira como queremos executar o script. Por defeito, o Screen está ativo visto que é a única opção para o sistema SIGMA do Instituto Superior Técnico.

#### Como Instalar

- Instalar com SCREEN (automático)

```
git clone git@github.com:manuelsousa7/notificador-notas.git
cd notificador-notas
sh install.sh
```
Após estes passos devera editar o ficheiro de configuracoes com as com todas as informações pessoais para as notificações. Por fim fazer Ctrl + X, selecionar Y, e por fim Enter. Deste modo o script esta pronto a enviar uma notificação assim que detetar uma mudanca na pagina das notas.


- Instalar com crontab

```
git clone git@github.com:manuelsousa7/notificador-notas.git
cd notificador-notas
nano config.ini
```

Editar o ficheiro de configurações, com todas as informações pessoais para as notificações e alterar o modo running para trabalhar com crontab. Por fim:

```
crontab -e
```

Adicionar o seguinte exemplo no final do ficheiro que executara o script a cada 15 segundos.

```
* * * * * $HOME/notificador-notas/script.py
* * * * * sleep 15; $HOME/notificador-notas/script.py
* * * * * sleep 30; $HOME/notificador-notas/script.py
* * * * * sleep 45; $HOME/notificador-notas/script.py
```

#### API's

- Sistema de Emails



- Sistema de SMS


#### Bugs / Reporte de Problemas

Abrir ISSUE no Github

#### Sugestões

Enviar um email para manuelvsousa@tecnico.ulisboa.pt
