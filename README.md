<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0a0a,50:5865F2,100:0a0a0a&height=180&section=header&text=Discord%20Token%20Checker&fontSize=48&fontColor=ffffff&fontAlignY=42&desc=Fast%20%26%20clean%20token%20validator&descAlignY=62&descSize=15" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=800&color=5865F2&center=true&vCenter=true&width=600&height=40&lines=Check+validity;Get+account+info;Save+working+tokens"/>

<img src="https://img.shields.io/badge/Python-3.10%2B-5865F2?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-5865F2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Version-2.0-5865F2?style=for-the-badge"/>

</div>

---

## ✨ Что делает

- ✅ Проверяет валидность Discord-токенов
- 📋 Показывает **полную информацию**: username, ID, email, phone, 2FA, Nitro, billing, количество серверов
- 📦 Три режима: **один токен**, **список из файла**, **вставить вручную**
- 💾 Сохраняет валидные токены в `valid_tokens.txt`
- 🎨 Красивый цветной вывод в консоль
- ⚡ Работает быстро, с задержкой между запросами (обход rate-limit)

---

## 🚀 Установка

### 1. Клонировать

```bash
git clone https://github.com/QwixxTwix/Discord-Test-Token.git
cd Discord-Test-Token
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

### 3. Запуск

**Windows:** двойной клик по `run.bat`

**Linux / macOS:**
```bash
python3 main.py
```

---

## 🎯 Использование

При запуске откроется меню:

```
  Выбери режим:

  [1] Проверить один токен
  [2] Проверить список из файла (tokens.txt)
  [3] Вставить список вручную (по одному в строке)
  [0] Выход
```

### Режим 1 — один токен

Вставь токен → получишь полную информацию:

```
[✓] MTA5…xYz  →  VALID
    ID       : 123456789012345678
    Username : qwixxa#0001
    Display  : Qwixx
    Email    : user@example.com ✓
    Phone    : +7 ***
    2FA      : ON
    Nitro    : Nitro
    Billing  : YES
    Guilds   : 42
    Locale   : ru
```

### Режим 2 — список из файла

Создай `tokens.txt` рядом с `main.py`:

```
MTIzNDU2Nzg5.ABCDEF.xyz...
OTk5OTk5OTk5.ABCDEF.abc...
```

Запусти режим `[2]` — все токены проверятся по очереди.

### Режим 3 — вручную

Вставляй токены построчно. Пустая строка — запуск проверки.

---

## 📁 Куда сохраняются валидные токены

Все рабочие токены автоматически пишутся в **`valid_tokens.txt`** в формате JSON (по одной строке на токен):

```json
{"token": "MTIz…", "info": {"id": "...", "username": "...", ...}}
```

---

## ⚙️ Технические детали

| Параметр | Значение |
|---|---|
| API | Discord v10 |
| Timeout | 10 сек |
| User-Agent | Chrome 120 (спуфинг) |
| Rate-limit | авто-пауза 0.5с между запросами |
| Формат сохранения | JSON Lines |

**Дополнительные запросы для каждого валидного токена:**
- `/users/@me/billing/payment-sources` — наличие платежей
- `/users/@me/guilds` — количество серверов

---

## 🖼 Скриншот

<img width="788" height="442" alt="image" src="https://github.com/user-attachments/assets/3aaa5a53-d11f-4d28-b64a-0194204ab1c6" />

---

## ⚠️ Дисклеймер

> Инструмент создан **исключительно в образовательных целях**.
> Проверяй только **свои** токены.
> Использование чужих токенов — нарушение Discord ToS и может преследоваться по закону.
> Автор не несёт ответственности за любое использование.

---

<div align="center">

**by [QwixxTwix](https://github.com/QwixxTwix)**

⭐ Если помогло — поставь звезду

</div>
