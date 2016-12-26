<#
    .NOTES
        Script <> with <3 by @rasmuskriest

    .SYNOPSIS
        The final solution for creating jury booklets for events of the European Youth Parliament.

    .DESCRIPTION
        The final solution for creating jury booklets for events of the European Youth Parliament. This is script one out of two which sets up a new jurymatic instance.

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

if (Get-Command py.exe -errorAction SilentlyContinue) {

    py.exe -2 $PSScriptRoot\get-pip.py

    pip2.exe install virtualenv

    virtualenv $PSScriptRoot

    Invoke-Expression .\Scripts\activate.ps1

    pip2.exe install -r requirements.txt

    py.exe -2 manage.py migrate

    Write-Output "============================="
    Write-Output "We are now going to create the administration user for the jurymatic server. Please remember the details you enter here. Only username and password are required fields."
    Write-Output "============================="

    py.exe -2 manage.py createsuperuser

    Write-Output "============================="
    Write-Output "Congratulations, you are done. You can now run start.bat or Start-Jurymatic.ps1 respectively."
    Write-Output "============================="

    Pause
}

else {
    python.exe $PSScriptRoot\get-pip.py

    pip.exe install virtualenv

    virtualenv $PSScriptRoot

    Invoke-Expression .\Scripts\activate.ps1

    pip.exe install -r requirements.txt

    python.exe manage.py migrate

    Write-Output "============================="
    Write-Output "We are now going to create the administration user for the jurymatic server. Please remember the details you enter here. Only username and password are required fields."
    Write-Output "============================="

    python.exe manage.py createsuperuser

    Write-Output "============================="
    Write-Output "Congratulations, you are done. You can now run start.bat or Start-Jurymatic.ps1 respectively."
    Write-Output "============================="

    Pause
}
