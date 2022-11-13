@echo off

:param
set str=%1
if "%str%"=="" (
    goto end
)

if exist %str% (
    echo %str% is exist
) else (
    copy nul %str% > nul
)



shift /0
goto param

:end