<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0a0a,50:5865F2,100:0a0a0a&height=170&section=header&text=Discord%20Token%20Checker&fontSize=44&fontColor=ffffff&fontAlignY=42&desc=Fast%20token%20validator&descAlignY=64&descSize=15" width="100%"/>
</div>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10%2B-5865F2?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Version-2.0-5865F2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-5865F2?style=for-the-badge"/>
</p>

---

## ✨ Что делает

- ✅ Проверяет валидность Discord-токенов
- 📋 Показывает полную информацию: username, ID, email, phone, 2FA, Nitro, billing, серверы
- 📦 Три режима: один токен, список из файла, вставить вручную
- 💾 Сохраняет валидные токены в `valid_tokens.txt`
- 🎨 Красивый цветной вывод в консоль
- ⚡ Работает быстро, с паузами между запросами (обход rate-limit)

---

## 🚀 Установка

**1. Клонировать**

`git clone https://github.com/QwixxTwix/Discord-Test-Token.git`

`cd Discord-Test-Token`

**2. Установить зависимости**

`pip install -r requirements.txt`

**3. Запуск**

- **Windows:** двойной клик по `run.bat`
- **Linux / macOS:** `python3 main.py`

---

## 🎯 Использование

При запуске откроется меню:

- **[1]** Проверить один токен
- **[2]** Проверить список из файла (`tokens.txt`)
- **[3]** Вставить список вручную
- **[0]** Выход

**Режим 1 — один токен**

Вставь токен — получишь отчёт:

- `[✓]` или `[✗]` — статус
- ID, Username, Display Name
- Email (+ проверка)
- Phone
- 2FA: ON / OFF
- Nitro: None / Classic / Nitro / Basic
- Billing: YES / no
- Guilds: количество серверов
- Locale

**Режим 2 — список из файла**

Создай `tokens.txt` рядом с `main.py`, по одному токену в строке. Запусти.

**Режим 3 — вручную**

Вставляй токены построчно. Пустая строка — запуск.

---

## 📁 Куда сохраняются валидные токены

Все рабочие токены автоматически пишутся в `valid_tokens.txt` в формате JSON (по одной строке на токен).

---

## 🖼 Скриншот

<div align="center">
<img width="788" alt="demo" src="https://github.com/user-attachments/assets/3aaa5a53-d11f-4d28-b64a-0194204ab1c6"/>
</div>

---

## ⚙️ Технические детали

- **API:** Discord v10
- **Timeout:** 10 сек
- **User-Agent:** Chrome 120 (спуфинг)
- **Rate-limit:** пауза 0.5с между запросами
- **Формат сохранения:** JSON Lines

**Доп. запросы для валидных токенов:**

- `/users/@me/billing/payment-sources` — платежи
- `/users/@me/guilds` — серверы

---

## ⚠️ Дисклеймер

> Инструмент создан исключительно в образовательных целях.
> Проверяй только свои токены.
> Использование чужих токенов — нарушение Discord ToS и может преследоваться по закону.
> Автор не несёт ответственности за любое использование.

---

<div align="center">

**by <a href="https://github.com/QwixxTwix">QwixxTwix</a>**

⭐ Если помогло — поставь звезду

</div>
