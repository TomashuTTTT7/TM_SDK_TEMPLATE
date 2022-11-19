@echo off
set /p name="set project name>"
ren "TM_SDK_TEMPLATE.sln" "%name%.sln"
ren "TM_SDK_TEMPLATE\TM_SDK_TEMPLATE.vcxproj" "%name%.vcxproj"
ren "TM_SDK_TEMPLATE\TM_SDK_TEMPLATE.vcxproj.user" "%name%.vcxproj.user"
ren "TM_SDK_TEMPLATE\TM_SDK_TEMPLATE.vcxproj.filters" "%name%.vcxproj.filters"
ren "TM_SDK_TEMPLATE" "%name%"
start /WAIT python init.py
del init.py
del init.bat