import win32com.client
import pythoncom
import sys

class XASessionReceiver: # 서버에 요청한 API 결과 값을 수신받는 결과
    def __init__(self) -> None:
        self.parent = None
    
    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인에 성공했습니다.")
            self.parent.response = True
        else:
            print(f"로그인 실패: {code} | {msg}")
            sys.exit()

    def OnDisconnect(self): # 서버 연결 문제시 발생 트리거
        print("서버와의 연결이 끊겼습니다.")
        sys.exit()


class XASession: # 로그인, 계좌정보
    def __init__(self, login_server) -> None:
        self.response = False
        self.login_server = self.set_server(login_server=login_server)
        self.session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionReceiver)
        self.session.parent = self # 상위 클래스에 권한 제공

    @staticmethod
    def set_server(login_server):
        if login_server == "실투자":
            return "api.ls-sec.co.kr"
        else:
            return "demo.ls-sec.co.kr"

    def connect_server(self): # 서버 연결 함수
        res = self.session.ConnectServer(self.login_server, 20001)
        
        if not res:
            error_code = self.GetLastError()
            error_msg = self.GetErrorMessage(error_code)
            print(error_msg)
            sys.exit()

    def disconnect_server(self):
        self.session.DisconnectServer()
        sys.exit()

    def login(self, crypto_wallet):
        _id = crypto_wallet["id"]
        _pw = crypto_wallet["pwd"]
        _cert = crypto_wallet["cert_pwd"]

        self.session.Login(_id, _pw, _cert, 0, False)

        while not self.response:
            pythoncom.PumpWaitingMessages() # 메시지를 받을때까지 기다림

    def get_account_list(self): # 계좌 가져오기
        cnt = self.session.GetAccountListCount()
        account_list = list()
        for idx in range(cnt):
            account_num = self.session.GetAccountList(idx)
            account_list.append(account_num)

        return account_list