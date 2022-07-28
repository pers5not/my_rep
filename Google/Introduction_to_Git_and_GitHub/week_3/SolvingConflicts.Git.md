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
git push --delete origin <name...branch>
# Удаление удаленной ветки git
git rebase <name...branch>
# Перебазирование — это процесс перемещения последовательности коммитов к новому базовому коммиту или их объединение
```
### Ссылки для устранения конфликтов слияния 

Конфликты слияния не редкость при работе в команде разработчиков или в программном обеспечении с открытым исходным кодом. К счастью, на GitHub есть хорошая документация о том, как справляться с такими ситуациями:

- [GitHub-merge-conflicts](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts)

- [GitHub-conflict-using-the-command-line](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line)

Вы также можете использовать git rebase имя ветки , чтобы изменить базу текущей ветки на имя ветки.
Команда git rebase намного мощнее. Перейдите по [этой ссылке](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) для получения дополнительной информации.

