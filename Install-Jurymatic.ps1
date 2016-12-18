<#
    .NOTES
        Coded with <3 by @rasmuskriest and @wolfskaempf
    
    .SYNOPSIS
        The final solution for creating jury booklets for events of the European Youth Parliament.

    .DESCRIPTION
        The final solution for creating jury booklets for events of the European Youth Parliament. This is script one out of two which is meant to install a new JURYMATIC instance.

    .EXAMPLE
        .\Install-Jurymatic.ps1
#>
#Requires -Version 3.0

echo "Welcome to the jurymatic installer!
   _                                  _   _
  (_)_   _ _ __ _   _ _ __ ___   __ _| |_(_) ___
  | | | | | '__| | | | '_ ` _ \ / _` | __| |/ __|
  | | |_| | |  | |_| | | | | | | (_| | |_| | (__
 _/ |\__,_|_|   \__, |_| |_| |_|\__,_|\__|_|\___|
|__/            |___/"

echo "=============================="
echo "This file will start the installation process in an elevated PowerShell."
echo "=============================="

python.exe $PSScriptRoot\get-pip.py

pip install virtualenv

virtualenv $PSScriptRoot

iex .\Scripts\activate.ps1

pip install -r requirements.txt

python manage.py migrate

echo "============================="

echo "We are now going to create the administration user for the jurymatic server. Please remember the details you enter here. Only username and password are required fields."

echo "============================="

python manage.py createsuperuser

echo "Congratulations, you are done. You can now run start.bat or Start-Jurymatic.ps1 respectively."
