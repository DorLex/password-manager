### Запуск проекта:

#### 1. Клонировать репозиторий:

```bash
git clone https://github.com/DorLex/password-manager.git
```

#### 2. Перейдя в корневую папку проекта, создать файл `.env` (как в примере `.env.example`).

- *Если хотим другой ключ шифрования `CRYPTOGRAPHY_KEY`, можно сгенерировать с помощью:*

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
```

#### 3. Сбилдить через docker compose:

```bash
docker compose build
```

#### 4. Запустить:

```bash
docker compose up
```

#### 5. Открыть еще одну вкладку терминала и произвести миграции:

```bash
 docker compose run --rm app python manage.py migrate
```

#### 6. Если хотим прогнать тесты:

*(также в другой вкладке терминала при запущенном docker compose)*

```bash
docker compose run --rm app python manage.py test
```
