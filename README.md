#How to setup this
1. mkdir testasign && cd testasign
2. virtualenv -p python3 envname
3. git clone https://github.com/grv07/plotyl.git
4. source envname/bin/activate
5. cd plotly
6. python3.5 -m pip install -r req.txt

---- Setup for MySql ----<br>
<i>Username: root, pass: root (You can change these settings on settings.py file >> [line-80] )</i>

7. create database gram;
8. cd ~/testasign/plotyl
<p>Note: Run command `ls` on current console,<br>if you can find manage.py file then got to next step otherwise cd to plotly directory first</p>
9. ./manage.py migrate
10. ./manage.py runserver

Your server start on 127.0.0.1:8000

Changes on Cell Phone Sensor Network Assignment

11. config.yaml set >> report_url: "http://localhost:8000/plot/"
12. run your sim.bash now with ./sim.bash
13. open http://localhost:8000/plot/

#Have Fun
