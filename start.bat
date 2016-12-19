@echo off
REM This will start Jurymatic in an elevated PowerShell.

@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex %cd%\Start-Jurymatic.ps1"