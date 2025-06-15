from src.config.crypto_wallet import CRYPTO_WALLET
from src.core.xa_query import XAQuery
from src.core.xa_session import XASession

class Main:
    def __init__(self) -> None:
        # Settings
        login_server = "실투자" # 모의투자
        crypto_wallet = CRYPTO_WALLET[login_server]

        # Login
        xa_session = XASession(login_server=login_server)
        xa_session.connect_server()
        xa_session.login(crypto_wallet=crypto_wallet)

        # 계좌번호
        account_num = xa_session.get_account_list()
        
        # TR
        xa_query = XAQuery()
        account_dict = xa_query.request_balance(account_num=account_num[0], password=crypto_wallet["acc_pwd"]) # 현재 계좌에 담긴 해외주식이 없는 경우 안보임
        deposit = xa_query.request_deposit(account_num=account_num[0], password=crypto_wallet["acc_pwd"])
        out_standing = xa_query.request_out_standing(account_num=account_num[0], password=crypto_wallet["acc_pwd"])

        # 현재가
        xa_query.g3101(exchange_code="82", symbol="TSLA")

        # 과거 데이터 연속조회
        # xa_query.g3102(exchange_code="82", symbol="TSLA")

if __name__ == "__main__":
    Main()