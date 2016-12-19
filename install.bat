@echo off
REM This will start the installation of Jurymatic in an elevated PowerShell.

@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex %cd%\Install-Jurymatic.ps1"