
async def city_code(city):
    cities = {
    "Toshkent": "26005dca196f3fb5042ea30654681110f2ccdc1eff1ffa4ed3e8ddf059068d22",
    "Andijon": "89ae5dba571f5509012e735135c8ef2ebd01438af4b6625f1ca9a9ec3b1ece9e",
    "Namangan": "4a468e2c860d3c3ce503b03b860a283aeb51ac3719630cf1b5573611d3d20844",
    "Farg'ona": "52302c0b5811f321b73f43ba0e8786f26a65e981868d5a513a9f058bc03d048d",
    "Qarshi": "f5efb251d5e530c9d72bd61cff114f05d24ab8141fba1122879a6e97b9f38546",
    "Termiz": "8a4d5615cbd212193999e292fd0682efa393b3f9a360bae701cd7f15e7f97fe9",
    "Navoiy": "0d84e534fbdb39881eebc439e211affe042ad32e1cca129adc4f3c86fa017e92",
    "Samarqand": "ff4a605e15dbe9a66129fc07c268c43aba0865596c135cd9c07e750572f3682b",
    "Jizzax": "0bb8ffde0b77726813c5cde0ea42014a8eacd2743e7b199893d628a0543b37a9",
    "Guliston": "9af6f0d93a7f1f7a4073c7f60f1d2cdedbb8d749471a37d0383bc50342f52471",
    "Buxoro": "36fe35da82b685cecff753f966feb09231e17dbe6b7e156c85ac02a23775be88",
    "Urganch": "8c1d9726ac24522190d5a2e7b9bcc13662f1438ac7e5fe4b6baa63fe1ed17c16",
    "Nukus": "65b7d2efe306cc5812dfe712176e291485441299c2ce6dd9d6a1f0c0f8c89d2a"
    }
    city_code = cities[city]
    return city_code