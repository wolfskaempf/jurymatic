#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Welcome to the jurymatic installer!
   _                                  _   _
  (_)_   _ _ __ _   _ _ __ ___   __ _| |_(_) ___
  | | | | | '__| | | | '_ ` _ \ / _` | __| |/ __|
  | | |_| | |  | |_| | | | | | | (_| | |_| | (__
 _/ |\__,_|_|   \__, |_| |_| |_|\__,_|\__|_|\___|
|__/            |___/"

echo "=============================="
echo "You will now have to enter your password. During the entire process, you may be asked multiple times to enter it. It is normal, that while you are typing your password, it does not show up on the screen."
echo "=============================="
sudo python $DIR/get-pip.py

sudo pip install virtualenv

virtualenv -p python3 $DIR

cd $DIR

source $DIR/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')"

echo "============================="

echo "Congratulations, you are done. You can now run start.command and log into jurymatic with username 'admin' and password 'admin."

echo "Please make sure to change the password after your first login."

echo "============================="
