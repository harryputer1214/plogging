@echo off
chcp 65001 > nul
cd /d C:\git.harryputer1214.plogging

echo [Git Pull 실행 중...]
git pull

if %ERRORLEVEL%==0 (
    echo [✔] Pull 완료! 최신 상태로 동기화됐어요.
) else (
    echo [✘] Pull 중 오류 발생. 확인이 필요해요!
)

pause
