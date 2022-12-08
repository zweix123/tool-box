@echo off

if "%1" == "" ( 
    echo while file?
    goto end
) else (
    goto work
)
:work

cd %cd%

g++ -std=c++2a -W -Wall -Wfatal-errors %1

if %errorlevel% == 0 (
    echo Complete compilation
    a.exe
    del a.exe
)


:end