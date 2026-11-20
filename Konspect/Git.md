*   Git - введет историю проекта, сохраняя ее версии, как набор снимков(commit). Каждый commit хранит состояние файлов на момент сохранения, и так же что изменилось.
*   История хранится локально, внутри репозитория в скрытой папке .git
*   GitHub - удаленная копия репозиториев, хранящаяся на сервере и дающая возможность получить к ним доступ удаленно с любого устройства
    
    <span style="--tn-color:#e64d4d;color:#e64d4d;">Команды:</span>
    
    *   mkdir(make directory) - создет директорию(папку), модификатор ~ создает директорию в домашней папке пользователя.
    *   cd(change directory) - меняет папку. cd .. - возвращает в домашнюю лиректорию ~, а cd . - указывает на нынешнюю директорию.
    *   cp откуда(путь) куда(путь) - копировать из папки а в папку б
    *   git init - превращает папку в директорию гита: создает служебную папку для хранения версий
    *   ls - показывает содержание директории, с модификаторо -а(all), показывает вообще все(скрытые или имя с точки)
    *   echo - вывод на экран
    *   <span style="--tn-background:#e64d4d;background-color:#e64d4d;">echo</span> “# DevOps” > README.md - выводит текст в “” на экран, > перезаписывает текств в файл README.md,  а >> добавляет запись в конец файла
    *   git status - показывает что гит знает о текущей папке и файлах в ней
    *   git add файл - добавляет файл в индекс, то есть он добавлен для комита, но комит еще не произошел, просто добавл файл в коробку можно сказать.
    *   git commit -m “Описание изменений”- создет как раз коммит из файлов в индексе(коробке). Модификатор -m говорит что комит будет с message(сообщением)
    *   git log - показывает историю комитов и данные о них.
    
    Длинная строка после commit в git lob, его хэш(уникальный идентификатор)
    
    *   git remote add origin <span class="link-mention" data-url="https://github.com/Velensian/DevOps" data-embed-type="opengraph" data-title="Velensian/DevOps" data-description="Contribute to Velensian/DevOps development by creating an account on GitHub." data-image="api/attachments/l8dma4hs0frt/image/github.com-DevOps-a19cd5c2.jpg" data-favicon="api/attachments/sLmmj3dHXxBS/image/github.com.svg" data-site-name="GitHub"><a href="https://github.com/Velensian/DevOps">Velensian/DevOps</a></span> - аписывает адрес удалённого репозитория под коротким именем `origin` (так принято называть основной удалённый репозиторий).
    *   git remote -v - показывает список удалённых репозиториев, которые знает Git.
    *   git brach -M main - переименовать репозиторий а майн как принято
    *   `git push -u origin main` отправляет ветку `main` в `origin`, а флаг `-u` запоминает эту связь, чтобы дальше хватало просто `git push`.