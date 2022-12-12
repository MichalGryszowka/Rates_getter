import requests
import csv
from datetime import datetime
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMETextVCS


class MainClass:
    def __init__(self, name, api_link):
        self.name = name
        self.api_link = api_link

    def __repr__(self):
        return f'({self.name}, {self.api_link})'

    def get_single_currency(self):
        request = requests.get(self.api_link)
        currency_dict = {
            self.name: ["{:.2f}".format(request.json()['rates'][0]['mid']), request.json()['rates'][0]['effectiveDate'],
                        datetime.now().strftime("%H:%M:%S")]}
        return currency_dict


def get_all_currency(list_1):
    all_currency_data = []
    for elem in list_1:
        all_currency_data.append(elem.get_single_currency())
    return all_currency_data


def get_average(list_1):
    rates_avg = "{:.2f}".format(sum(list_1) / len(list_1))
    return rates_avg


def get_rates_of_single_currency(all_currency_list, currency):
    single_currency = [float(elem["rate"]) for elem in all_currency_list if currency in elem["currency"]]
    return single_currency


def save_results_to_file_1_and_2(result_1: list, currencies=None):
    if currencies is None:
        currencies = ["usd", "chf", "gbp"]
    with open("Wyniki_1.csv", 'a', newline="") as f1, \
            open("Wyniki_1.csv", "r") as f2, \
            open("Wyniki_2.csv", "w", newline='') as f3:
        fieldnames1 = ["currency ", "rate ", "date ", "time "]
        writer1 = csv.DictWriter(f1, fieldnames=fieldnames1)
        writer1.writerows(
            [dict(zip(fieldnames1, (k, v1, v2, v3))) for elem in result_1 for k, [v1, v2, v3] in elem.items()])
        fieldnames2 = ["currency", "average_rate"]
        writer2 = csv.DictWriter(f3, fieldnames=fieldnames2)
        data = list(csv.DictReader(f2, delimiter=","))
        writer2.writeheader()
        for curr in currencies:
            curr_rates = get_rates_of_single_currency(data, curr)
            curr_average = get_average(curr_rates)
            writer2.writerow({"currency": curr, "average_rate": curr_average})


def send_email():
    port = 465
    smtp_serwer = "smtp.gmail.com"
    nadawca = "michal.gryszowka2@gmail.com"
    odbiorca = "michal.gryszowka2@gmail.com"
    haslo = input("Please fill in your password:\n")
    temat = "Average currencies"
    tresc = "Drogi Januszu,\n" \
            "W zalaczniku przesylam Ci srednie kursy walut.\n" \
            "Serdecznie pozdrawiam,\n" \
            "Elon Musk"

    plik = "Wyniki_2.csv"

    wiadomosc = MIMEMultipart()
    wiadomosc["From"] = nadawca
    wiadomosc["To"] = odbiorca
    wiadomosc["Subject"] = temat
    wiadomosc.attach(MIMEText(tresc, "plain"))

    with open(plik, "rb") as f:
        zalacznik = MIMEBase("application", "octet-stream")
        zalacznik.set_payload(f.read())

    encoders.encode_base64(zalacznik)

    zalacznik.add_header(
        "Content-Disposition",
        f"attachment; filename= {plik}")

    wiadomosc.attach(zalacznik)
    tekst = wiadomosc.as_string()
    ssl_pol = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_serwer, port, context=ssl_pol) as serwer:
        serwer.login(nadawca, haslo)
        serwer.sendmail(nadawca, odbiorca, tekst)


dollar = MainClass("usd", "https://api.nbp.pl/api/exchangerates/rates/A/usd/today?format=json")
frank = MainClass("chf", "https://api.nbp.pl/api/exchangerates/rates/A/chf/today?format=json")
funt = MainClass("gbp", "https://api.nbp.pl/api/exchangerates/rates/A/gbp/today?format=json")

list_all_currency = [dollar, frank, funt]


def main():
    all_currency = get_all_currency(list_all_currency)
    save_results_to_file_1_and_2(all_currency)
    send_email()


if __name__ == '__main__':
    main()

