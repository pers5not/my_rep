### Рабочий процесс «вытягивание-слияние-проталкивание»

```
# Копирование файла с ветки на ветку
git checkout <name...branch> <name...file>
# Копирование всей ветки
git checkout <name...branch> ./
# Удалить коммит удаленно 
git reset  HEAD~
git push -f
# добавляем ветку в удаленный репозиторий
git push -u origin refactor
# удаляем ветку из удаленного репозитория 
git push -d origin <name...branch>
# еще один способ перенести изменения из одной ветки в другую
git rebase <name...branch>
```
