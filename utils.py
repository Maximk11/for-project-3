import requests

def get_conversion_rate(from_currency: str, to_currency: str, api_key: str) -> float:

    """
    Получает курс обмена между двумя валютами с использованием ExchangeRate-API.

    Параметры:
    from_currency (str): Валюта, из которой производится конвертация (например, "USD").
    to_currency (str): Валюта, в которую производится конвертация (например, "EUR").
    api_key (str): API-ключ для доступа к ExchangeRate-API.

    Возвращает:
    float: Курс обмена между валютами.
    """

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        if to_currency in data['conversion_rates']:
            return data['conversion_rates'][to_currency]
        else:
            raise ValueError(f"Невозможно найти курс для валюты {to_currency}.")
    else:
        raise ValueError(f"Ошибка API: {data.get('error-type', 'Неизвестная ошибка')}")


def convert_currency(amount: float, from_currency: str, to_currency: str, api_key: str) -> float:

    """
    Конвертирует сумму из одной валюты в другую.

    Параметры:
    amount (float): Сумма для конвертации.
    from_currency (str): Валюта, из которой производится конвертация.
    to_currency (str): Валюта, в которую производится конвертация.
    api_key (str): API-ключ для доступа к ExchangeRate-API.

    Возвращает:
    float: Конвертированная сумма в целевой валюте.
    """

    rate = get_conversion_rate(from_currency, to_currency, api_key)
    return amount * rate

if __name__ == "__main__":
    print("Конвертер валют.")

    api_key = ''

    from_currency = input("Введите валюту, из которой хотите конвертировать (например, USD): ").upper()
    to_currency = input("Введите валюту, в которую хотите конвертировать (например, EUR): ").upper()
    amount = float(input("Введите сумму для конвертации: "))

    try:
        converted_amount = convert_currency(amount, from_currency, to_currency, api_key)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)