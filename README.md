# *BookShelf_BOT*

***
+ 📁 __BookShelf_BOT__ - *корневая директория всего проекта*
  - **bot.py** - *основной исполняемый файл - точка входа в бот*
  - **.env.example** - *файл с примерами секретов*
  - 📁 **book** - *директория, в которой хранится файл книги*
    * **book.txt** - *собственно, сам текстовый файл книги*

  - 📁 **config_data** - *директория с модулем конфигурации бота*
    * **config.py** - *модуль для конфигурации бота*

  - 📁 **database** - *пакет для работы с базой данных.*
    * **database.py** - *модуль с базой данных*

  - 📁 **handlers** - *пакет с обработчиками*
    * **other_handlers.py** - *модуль с обработчиком любых текстовых сообщений, которые не попали в другие обработчики*
    * **user_handlers.py** - *модуль с хэндлерами пользователей. Все основные обработчики апдейтов бота будут в этом модуле*

  - 📁 **keyboards** - *пакет с клавиатурами бота*
    * **bookmarks_kb.py** - *модуль с клавиатурами для работы с закладками пользователя*
    * **main_menu.py** - *модуль для формирования главного меню бота*
    * **pagination_kb.py** - *модуль для формирования кнопок пагинации - для управления книгой*

  - 📁 **lexicon** - *директория для хранения словарей бота*
    * **lexicon.py** - *файл со словарем соответствий команд и запросов отображаемым текстам.*

  - 📁 **services** - *пакет со вспомогательными инструментами для работы бота*
    * **file_handling.py** - *модуль для подготовки книг*
***