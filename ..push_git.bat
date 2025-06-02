@echo off
chcp 65001 > nul
cd /d C:\git.harryputer1214.plogging

echo [Git Push 실행 중...]

git add .
git commit -m "자동 커밋"
git push

if %ERRORLEVEL%==0 (
    echo [✔] Push 완료! 변경사항이 업로드됐어요.
) else (
    echo [✘] Push 중 오류 발생. GitHub 토큰 인증이나 충돌을 확인하세요!
)

pause
