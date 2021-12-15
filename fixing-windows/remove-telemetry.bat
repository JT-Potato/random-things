: Removes all forms of telemetry
sc config DiagTrack start= disabled
sc stop DiagTrack
sc config dmwappushservice start= disabled
sc stop dmwappushservice
echo "" > C:\\ProgramData\\Microsoft\\Diagnosis\\ETLLogs\\AutoLogger\\AutoLogger-Diagtrack-Listener.etl
reg add HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection /v AllowTelemetry /t REG_DWORD /d 0 /f

: Disables every non-important telemetry scheduled task - it kinda doesn't do anything and takes up a bunch of CPU
SchTasks /CHANGE /TN "Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /DISABLE
SchTasks /CHANGE /TN "Microsoft\Windows\Application Experience\PcaPatchDbTask" /DISABLE
SchTasks /CHANGE /TN "Microsoft\Windows\Application Experience\ProgramDataUpdater" /DISABLE

echo Potential issues: needs administrator permissions.

: Removes delivery optimisation because wtf
sc config DoSvc start= disabled
sc stop DoSvc