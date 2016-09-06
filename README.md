# Notificador de Notas

Versão: 1.0.0 (Beta) 

Script que deteta alterações de paginas WEB, e envia notificações através de emails e SMS. Composto por um sistema de configuração de fácil utilização.

#### Modos de Utilização

- O Script foi feito de modo a operar de 2 maneiras. Sobre uma sessão ```screen``` ou sobre um ```crontab```. No ficheiro de configuração do script é possível escolher a maneira como queremos executar o script. Por defeito, o ```screen``` está ativo visto que é a única opção para o sistema ```sigma``` do Instituto Superior Técnico, ao qual todos os alunos desta instituição têm acesso e podem recorrer para plantar o script.

- O sistema de configurações permite adicionar um numero ilimitado de disciplinas. Todas as disciplinas futuramente adicionadas devem ser adicionadas no topo e cumprir a mesma sintaxe das disciplinas default.

- Não é recomendado reproduzir o script abaixo dos 6 segundos de diferença 

#### Como Instalar

- Instalar com SCREEN (automático)

```
git clone git@github.com:manuelsousa7/notificador-notas.git
cd notificador-notas
sh install.sh
```
Após estes passos devera editar o ficheiro de configuracoes com as com todas as informações pessoais para as notificações. Por fim fazer ```Ctrl + X```, selecionar ```Y```, e por fim ```Enter```. Deste modo o script esta pronto a enviar uma notificação assim que detetar uma mudanca numa das paginas de notas.


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

- Sistema de Emails (Ativo por defeito)

O script utiliza uma API de um serviço de emails chamado MailGun. Por defeito já vem configurada uma conta que pode utilizada por quem utilizar o script. Existe uma cota mensal de 10.000 emails pelo que será necessário cada utilizador criar a sua própria conta se esta cota for ultrapassada.

- Sistema de SMS

De modo construir um script que notificasse o utilizador por SMS de forma simples, seria necessário investir em serviços deste tipo. De forma a contornar este problema com uma solução gratuita o script é capaz de enviar SMSs pelo serviço TextLocal, que oferece 10 sms gratis por cada conta criada. No ficheiro de configuração é possível alterar as API's. (com alguma criatividade é possível ter esta funcionalidade sempre ativa)


#### Bugs / Reporte de Problemas / Sugestões

Em caso de problemas abrir ISSUE no Github, ou enviar email para manuelvsousa@tecnico.ulisboa.pt
