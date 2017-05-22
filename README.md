Exemplos do curso [Curso de Flask](https://www.youtube.com/playlist?list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX) de Júlia Rizza
========================
* Autor: César Magalhães
* Tecnologias: Python 3.5.2, Flask 0.12.2, SQLite
* Resumo: Curso de Flask
* Linguagens: Python
* Fonte: <https://github.com/cams7/exemplos-flask-juliarizza>
* Linkedin: <https://br.linkedin.com/in/cams7>

Qual a finalidade desses exemplos?
-------------------
Esses exemplos foram estudados e testados com intuíto de aprender um pouco mais sobre o Framework Flask.

Sistemas requeridos
-------------------
* [Microsoft Windows 10](https://www.microsoft.com/pt-br/software-download/windows10)
* [Ubuntu 16.04.5 LTS](http://releases.ubuntu.com/16.04/)
* [Git](https://git-scm.com/downloads)
* [SQLite](https://www.sqlite.org/)
* [PyCharm](https://www.jetbrains.com/pycharm/)

Para testa todos os exemplos
-------------------
* Instale o Git
* Instale o PyCharm Community

Exemplos do curso [Curso de Flask](https://www.youtube.com/playlist?list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX) de Júlia Rizza
-------------------
01. [Aula 1 - Introdução - Curso de Flask](https://www.youtube.com/watch?v=r40pC9kyoj0&index=1&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
```sh
sudo apt-get update
sudo apt-get install python3-pip
sudo pip install virtualenv

mkdir -P Projects/cursoflask
cd Projects/cursoflask
virtualenv -p python3 venv
source venv/bin/activate

pip install Flask
python aula1/hello.py
#Running on http://localhost:5000/
#CTR-C
#deactivate
```
02. [Aula 2 - Ambiente - Curso de Flask](https://www.youtube.com/watch?v=Pz9rayiDHW0&index=2&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
```sh
pip freeze > requirements.txt
#pip install -r requirements.txt
python run.py
#Running on http://localhost:5000/
#CTR-C
```
03. [Aula 2 - (Continuação) Ambiente - Curso de Flask](https://www.youtube.com/watch?v=0iHsyTkyoXo&index=3&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
04. [Aula 3 - Models - Curso de Flask](https://www.youtube.com/watch?v=R3nS66dgo2w&index=4&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
```sh
pip install flask-sqlalchemy
pip freeze > requirements.txt

Aula 04
pip install flask-migrate
pip install flask-script
pip freeze > requirements.txt

python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py db --help

python manage.py runserver
#Running on http://localhost:5000/
#CTR-C
```
05. [Aula 4 - Migrações - Curso de Flask](https://www.youtube.com/watch?v=tJZjniFdaIw&index=5&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
06. [Aula 5 - Configurações - Curso de Flask](https://www.youtube.com/watch?v=i5IiqFIPjbw&index=6&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
```sh
python manage.py shell
```
```py
import settings as s
print(s.DEBUG)
print(s.SQLALCHEMY_DATABASE_URI)
print(s.SQLALCHEMY_TRACK_MODIFICATIONS)
exit()
```
07. [Aula 6 - Rotas - Curso de Flask](https://www.youtube.com/watch?v=2eN51HrYl9A&index=7&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
08. [Aula 7 - Templates - Curso de Flask](https://www.youtube.com/watch?v=iDZo0aPIHec&index=8&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
09. [Aula 8 - Mais Templates - Curso de Flask](https://www.youtube.com/watch?v=Q_SpLfhFiK8&index=9&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
10. [Aula 9 - Formulários - Curso de Flask](https://www.youtube.com/watch?v=ypF6jxwes8g&index=10&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
```sh
pip install flask-wtf
pip freeze > requirements.txt

python manage.py runserver
#Running on http://localhost:5000/
#CTR-C
```
11. [Aula 10 - CRUD - Curso de Flask](https://www.youtube.com/watch?v=_yTjp9IiUB0&index=11&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
```sh
python manage.py db migrate
python manage.py db upgrade

python manage.py shell
```
```py
from app import db
from app.models.tables import User
user = User('cams7','12345','Cesar A. Magalhaes','ceanma@gmail.com')
db.session.add(user)
db.session.commit()
user = User.query.filter_by(username='cams7').first()
print(user)
users = User.query.filter_by(username='cams7').all()
print(users)
exit()
```
12. [Aula 11 - Login - Curso de Flask](https://www.youtube.com/watch?v=ddjT_Gdp_cc&index=12&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
```sh
pip install flask-login
pip freeze > requirements.txt

python manage.py runserver
#Running on http://localhost:5000/
#CTR-C
```
