# Discord Token Checker
# Created by Qwixx
# github.com/QwixxTwix

import os
import sys
import json
import time
import requests
from colorama import Fore, Style, init

init(autoreset=True)

# ─── Цвета ───
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
M = Fore.MAGENTA
W = Fore.WHITE
B = Style.BRIGHT
RST = Style.RESET_ALL

API = "https://discord.com/api/v10"
TIMEOUT = 10


BANNER = f"""{B}{M}
   ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
   ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
   ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
   ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
   ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
   ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
{RST}{B}{W}              Discord  Token  Checker{RST}
{B}{C}                  by Qwixx  ·  v2.0{RST}
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def check_token(token: str) -> dict | None:
    """Проверка одного токена. Возвращает dict или None."""
    token = token.strip()
    if not token:
        return None

    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
    }

    try:
        r = requests.get(f"{API}/users/@me", headers=headers, timeout=TIMEOUT)
    except requests.RequestException as exc:
        return {"valid": False, "error": f"Network: {exc}"}

    if r.status_code == 401:
        return {"valid": False, "error": "Invalid token"}
    if r.status_code == 403:
        return {"valid": False, "error": "Token locked / banned"}
    if r.status_code == 429:
        retry = r.headers.get("Retry-After", "?")
        return {"valid": False, "error": f"Rate limited (retry after {retry}s)"}
    if r.status_code != 200:
        return {"valid": False, "error": f"HTTP {r.status_code}"}

    try:
        data = r.json()
    except Exception:
        return {"valid": False, "error": "Bad JSON"}

    # Доп. запрос: биллинг / нитро
    nitro = "—"
    billing_ok = False
    try:
        br = requests.get(f"{API}/users/@me/billing/payment-sources",
                          headers=headers, timeout=TIMEOUT)
        if br.status_code == 200:
            sources = br.json()
            billing_ok = bool(sources)
    except Exception:
        pass

    # Доп. запрос: гильдии
    guilds = "—"
    try:
        gr = requests.get(f"{API}/users/@me/guilds",
                          headers=headers, timeout=TIMEOUT)
        if gr.status_code == 200:
            guilds = len(gr.json())
    except Exception:
        pass

    return {
        "valid": True,
        "id": data.get("id", "—"),
        "username": data.get("username", "—"),
        "discriminator": data.get("discriminator", "0"),
        "global_name": data.get("global_name") or "—",
        "email": data.get("email") or "—",
        "phone": data.get("phone") or "—",
        "verified": data.get("verified", False),
        "mfa_enabled": data.get("mfa_enabled", False),
        "nitro_type": data.get("premium_type", 0),
        "locale": data.get("locale", "—"),
        "billing": billing_ok,
        "guilds": guilds,
        "flags": data.get("public_flags", 0),
    }


NITRO_TYPES = {
    0: "None",
    1: "Nitro Classic",
    2: "Nitro",
    3: "Nitro Basic",
}


def print_token(token: str, info: dict | None) -> None:
    """Печатает результат проверки одного токена."""
    masked = token[:25] + "…" + token[-5:] if len(token) > 32 else token

    if info is None:
        print(f"{R}[✗]{RST} {W}{masked}{RST}  →  {R}Empty{RST}")
        return

    if not info.get("valid"):
        err = info.get("error", "Invalid")
        print(f"{R}[✗]{RST} {W}{masked}{RST}  →  {R}{err}{RST}")
        return

    print(f"{G}[✓]{RST} {W}{masked}{RST}  →  {G}VALID{RST}")
    print(f"    {C}ID       :{RST} {info['id']}")
    print(f"    {C}Username :{RST} {info['username']}"
          f"#{info['discriminator']}")
    if info["global_name"] != "—":
        print(f"    {C}Display  :{RST} {info['global_name']}")
    print(f"    {C}Email    :{RST} "
          f"{G + info['email'] + RST if info['email'] != '—' else '—'} "
          f"{'✓' if info['verified'] else '✗'}")
    if info["phone"] != "—":
        print(f"    {C}Phone    :{RST} {G}{info['phone']}{RST}")
    print(f"    {C}2FA      :{RST} "
          f"{G + 'ON' + RST if info['mfa_enabled'] else 'OFF'}")
    print(f"    {C}Nitro    :{RST} "
          f"{Y + NITRO_TYPES.get(info['nitro_type'], '?') + RST}")
    print(f"    {C}Billing  :{RST} "
          f"{G + 'YES' + RST if info['billing'] else 'no'}")
    print(f"    {C}Guilds   :{RST} {info['guilds']}")
    print(f"    {C}Locale   :{RST} {info['locale']}")
    print()


def load_tokens_from_file(path: str) -> list[str]:
    """Загрузить токены из файла (по одному в строке)."""
    if not os.path.isfile(path):
        print(f"{R}Файл не найден: {path}{RST}")
        return []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f
                if line.strip() and not line.startswith("#")]


def save_result(path: str, entry: dict) -> None:
    """Сохранить валидный токен в файл."""
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass


def menu() -> str:
    print(BANNER)
    print(f"{B}{W}  Выбери режим:{RST}\n")
    print(f"  {M}[1]{RST} Проверить один токен")
    print(f"  {M}[2]{RST} Проверить список из файла (tokens.txt)")
    print(f"  {M}[3]{RST} Вставить список вручную (по одному в строке)")
    print(f"  {M}[0]{RST} Выход\n")
    return input(f"{B}{M}  > {RST}").strip()


def mode_single() -> None:
    token = input(f"\n{B}{M}  Token > {RST}").strip()
    if not token:
        return
    print()
    info = check_token(token)
    print_token(token, info)
    if info and info.get("valid"):
        save_result("valid_tokens.txt", {"token": token, "info": info})
        print(f"{G}  ✓ Сохранено в valid_tokens.txt{RST}\n")


def mode_file() -> None:
    path = input(f"\n{B}{M}  Файл [tokens.txt] > {RST}").strip() or "tokens.txt"
    tokens = load_tokens_from_file(path)
    if not tokens:
        print(f"{R}  Нет токенов для проверки.{RST}\n")
        return
    print(f"\n{C}  Проверяю {len(tokens)} токен(ов)…{RST}\n")
    for i, tok in enumerate(tokens, 1):
        print(f"{Y}  [{i}/{len(tokens)}]{RST}")
        info = check_token(tok)
        print_token(tok, info)
        if info and info.get("valid"):
            save_result("valid_tokens.txt", {"token": tok, "info": info})
        time.sleep(0.5)


def mode_manual() -> None:
    print(f"\n{C}  Вставляй токены по одному. Пустая строка — конец.{RST}\n")
    tokens = []
    while True:
        line = input(f"{B}{M}  Token > {RST}").strip()
        if not line:
            break
        tokens.append(line)

    if not tokens:
        return
    print(f"\n{C}  Проверяю {len(tokens)} токен(ов)…{RST}\n")
    for i, tok in enumerate(tokens, 1):
        print(f"{Y}  [{i}/{len(tokens)}]{RST}")
        info = check_token(tok)
        print_token(tok, info)
        if info and info.get("valid"):
            save_result("valid_tokens.txt", {"token": tok, "info": info})
        time.sleep(0.5)


def main() -> None:
    while True:
        try:
            choice = menu()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{M}  Выход.{RST}")
            break

        if choice == "0":
            print(f"\n{M}  До встречи, хакер!{RST}\n")
            break
        elif choice == "1":
            mode_single()
        elif choice == "2":
            mode_file()
        elif choice == "3":
            mode_manual()
        else:
            print(f"{R}  Неверный выбор.{RST}\n")

        input(f"{C}  Enter — назад в меню…{RST}")
        clear()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{M}  Прервано.{RST}")
        sys.exit(0)
