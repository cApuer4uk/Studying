git init
git status
git remote and origin https/...
git add
git config --global user.name "name"
git config --global user.email "@gmail.com"
git commit -m "аннотация изменений в файле"
git push -u origin master
 Логинимся на сайте, подтверждаем
git add task2
git commit -m "файл под решение задачи 2"
git push
git branch misha_task_2                              # создание личной ветки
git checkout misha_task_2                            # переход на нужную ветку
git status
git add
git commit
git push -u origin misha_task_2
git merge "название ветки (слить ветку в нынешнюю)"
git pull "скачать последнее обновление ветки / скачать ветку, которой нет"
git branch -d "название ветки" #удалить ветку
