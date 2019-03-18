run commands 
tsc -t es2015 main.ts
npx browserify -p esmify main.js -o bundle.js

1 - состояние
class Document is
    field state: string
    // ...
    method publish() is
        switch (state)
            "draft":
                state = "moderation"
                break
            "moderation":
                if (currentUser.role == 'admin')
                    state = "published"
                break
            "published":
                // Do nothing.
                break
    // ...
2 - Цепочка обязанностей -> Создание цепочки работы ??
3 - Фасад  ( много классов -> единый интерфейс работы)
4 - Посетитель ( класс которому передают объект и он определяет что с ним делать)
5 - Наблюдатель ( класс который следит за другими классами и реагирует на изменения)



убрать все кроме фильтров с класса imagefilter
перенести всю логику действия с файлами в обсервер
дописать функцию ApplyFilter в Observer классе
вынести единый интерфейс для работы