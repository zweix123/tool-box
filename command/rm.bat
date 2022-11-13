@echo off

:param
set str=%1
if "%str%"=="" (
    goto end
)

del %str%

shift /0
goto param

:end