
Если у вас есть Git 2.29 или более поздней версии, теперь вы можете установить значение pull.ff, чтобы избавиться от предупреждения. false true only
```
git config pull.ff true     # rebase
```
:point_up:  
> __true- Это поведение по умолчанию. Pull перематывается вперед, если это возможно, в противном случае он объединяется.__
``` 
git config pull.ff false        # merge (the default strategy)
```
:point_up:  
> __false- Pull никогда не перематывается вперед, и всегда создается слияние.__
```
git config pull.ff only          # fast-forward only
```
:point_up:  
> __only- Pull перематывается вперед, если это возможно, в противном случае операция прерывается с сообщением об ошибке__