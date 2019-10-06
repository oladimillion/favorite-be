

###  aws ubuntu terminal after login
create key

select ec2 (do the necessary thing)

launch instance


###  aws ubuntu terminal after login

sudo apt-get update

sudo apt-get upgrade -y


> check whether python is installed

python3 --version 


> install python env

sudo apt-get install python3-venv


> create env

python3 -m venv env


> activate env

source env/bin/activate


> install gunicorn to run python base application

sudo apt-get install nginx -y


> install gunicorn to run django application

pip3 install gunicorn
