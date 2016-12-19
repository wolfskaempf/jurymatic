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

Write-Output "Welcome to the jurymatic installer!
   _                                  _   _
  (_)_   _ _ __ _   _ _ __ ___   __ _| |_(_) ___
  | | | | | '__| | | | '_ ` _ \ / _` | __| |/ __|
  | | |_| | |  | |_| | | | | | | (_| | |_| | (__
 _/ |\__,_|_|   \__, |_| |_| |_|\__,_|\__|_|\___|
|__/            |___/"

Write-Output "=============================="
Write-Output "This file will start the installation process."
Write-Output "=============================="

python.exe $PSScriptRoot\get-pip.py

pip install virtualenv

virtualenv $PSScriptRoot

Invoke-Expression .\Scripts\activate.ps1

pip install -r requirements.txt

python.exe manage.py migrate

Write-Output "============================="

Write-Output "We are now going to create the administration user for the jurymatic server. Please remember the details you enter here. Only username and password are required fields."

Write-Output "============================="

python.exe manage.py createsuperuser

Write-Output "Congratulations, you are done. You can now run start.bat or Start-Jurymatic.ps1 respectively."
