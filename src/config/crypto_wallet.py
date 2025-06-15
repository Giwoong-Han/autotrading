from dotenv import load_dotenv
import os

load_dotenv()

CRYPTO_WALLET = {
    "실투자": {
        "id": f"{os.getenv('ID')}", # 투혼 ID
        "pwd": f"{os.getenv('PW')}", # 투혼 비밀번호
        "cert_pwd": f"{os.getenv('CERT_PW')}", # 공인인증서 비밀번호
        "acc_pwd": f"{os.getenv('ACCOUNT_PW')}" # 계좌 비밀번호
    },
    "모의투자": {
        "id": f"{os.getenv('ID')}",
        "pwd": f"{os.getenv('PW')}",
        "cert_pwd": "",
        "acc_pwd": "0000"
    }
}