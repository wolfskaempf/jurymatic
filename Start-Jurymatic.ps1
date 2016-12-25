<#
    .NOTES
        Script coded with <3 by @rasmuskriest

    .SYNOPSIS
        The final solution for creating jury booklets for events of the European Youth Parliament.

    .DESCRIPTION
        The final solution for creating jury booklets for events of the European Youth Parliament. This is script two out of two which starts an installed jurymatic instance.

    .EXAMPLE
        .\Start-Jurymatic.ps1
#>
#Requires -Version 3.0

$localip = Test-Connection -ComputerName (hostname) -Count 1  | Select-Object IPV4Address

Write-Output "Your local IP address: ${localip}:8000"

Write-Output "=============================="

Invoke-Expression .\Scripts\activate.ps1
Start-Process http://localhost:8000
py.exe -2 $PSScriptRoot\manage.py runserver 0.0.0.0:8000
