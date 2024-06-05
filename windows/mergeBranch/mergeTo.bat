@echo off
setlocal EnableDelayedExpansion

REM 获取当前分支名称并保存到变量 current_branch
for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD') do set current_branch=%%i

REM 输出当前分_branch是
echo Current branch is: %current_branch%

REM 对于每一个传入的分支参数
:loop
if "%~1"=="" goto afterloop
    REM 切换到传入的分
    git checkout %1
    git pull

    REM 将之前保存的当前分支合并到传入的分支
    git merge %current_branch%

    REM 推送修改到远程仓库
    git push origin %1

    REM 切换回之前的分支
    git checkout %current_branch%

    REM 移动到下一个参数
    shift
goto loop

:afterloop
REM 恢复当前分支
git checkout %current_branch%

endlocal