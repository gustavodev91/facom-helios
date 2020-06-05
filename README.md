# Helios
Sistema de votação online para a Faculdade de Computação da Universidade Federal de Uberlândia, 
garantindo privacidade e não relacionamento entre votos, através de criptografia homomórfica.

# Guia de instalação e configuração do Helios

Neste tutorial são descritos os principais passos para instalação de um servidor para disponibilização do Helios.

Instalação servidor (Ubuntu)

Supondo uma máquina apenas com o sistema operacional

Atualizações/instalações de pacotes:

<code>
sudo apt-get dist-upgrade

sudo apt-get install apache2 postgresql-9.3 postgresql-server-dev-9.3 python-dev libsasl2-dev libldap2-dev python-ldap gettext libapache2-mod-wsgi
</code>

Se for baixar e/ou atualizar o código via github:

<code>
sudo apt-get install git 
</code>

##Configurações

# Banco

<code> 
sudo su postgres

psql

create user helios;

create role helios with createdb createrole login;

alter user helios with password 'sua senha';
</code>

Editar o arquiv pg_hba.conf e inserir a linha:

<code>
local all helios md5
</code>

logo acima da linha

<code>
local all all peer
</code>

A configuração acima corrige o seguinte erro:

Exception Type: OperationalError Exception Value: FATAL: Peer authentication failed for user "helios"

# Obtenção do código-fonte e preparação da aplicação

Você pode baixar um zip com o fonte ou clonar o repositório. Supondo que o código vai ser baixado via git:

git clone https://github.com/gustavosc91/facom-helios.git

Não é obrigatório, mas é uma boa prática, criar um ambiente virtual para a disponibilização do Helios, tanto para desenvolvimento quanto para implantação, pois isso permite separar as dependências do projeto e não interferir em outros sistemas na mesma máquina.

Primeiramente, instale o pip, seguindo as orientações do desenvolvedor: http://pip.readthedocs.org/en/stable/

Depois, instale o virtualenv, seguindo também as orientações disponíveis em: http://virtualenv.readthedocs.org/en/latest/

Terminada a instalação do virtualenv, dentro do diretório onde o helios foi baixado, basta dar o comando virtualenv venv

(venv é um exemplo, pode ser dado outro nome se necessário).

Para ativar o ambiente virtual, execute source venv/bin/activate

Com o ambiente virtual ativado, instale os requisitos para a execução do helios:

<code>
pip install -r requirements.txt
</code>

ATENÇÃO: Utilize o requirements.txt deste repositório, para instalar o pacote django-auth-ldap e outros necessários às customizações realizadas. Lembrando também que apesar de se pretender manter este repositório atualizado com o do Ben Adida, não necessariamente vai ser simultâneo, então se você utilizar o dele, pode haver versões diferentes de pacotes.

Após terminar a instalação dos pacotes necessários, é possível realizar as devidas execuções de banco de dados (criação de banco, tabelas, etc) executando o script reset.sh:

<code>
$./reset.sh
</code>

Se tiver algum problema rodando o script acima, provavelmente vai ser relacionado à configuração do PostgreSQL e, nesse caso, o google é seu amigo.

Para disponibilizar o helios em português, é preciso compilar os arquivos de tradução. Execute o seguinte comando a partir do diretório do Helios:

<code>
python manage.py compilemessages
</code>

Após a compilação, arquivos .mo devem ter sido gerados em locale/pt_BR/LC_MESSAGES

Maiores informações em https://docs.djangoproject.com/en/1.6/ref/django-admin/

Se tudo estiver correto até aqui, agora você pode rodar o servidor de desenvolvimento, distribuído com o django, e testar a instalação básica:

<code>
$python manage.py runserver 0.0.0.0:8000
</code> 0.0.0.0 para que fique acessível da rede. Pode executar até runserver, se preferir. Também pode trocar a porta!
