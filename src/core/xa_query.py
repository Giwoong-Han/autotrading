from src.config.menulist import *
import win32com.client
import pythoncom
import sys
import time

class XAQueryReceiver: # 서버에 요청한 API 결과 값을 수신받는 결과
    def __init__(self) -> None:
        self.parent = None
    
    def OnReceiveMessage(self, _, code, msg):
        print(f"OnReceiveMessage: {code} | {msg}")
        self.parent.response = True

    def OnReceiveData(self, event): # 요청한 데이터를 수신
        if event == "COSOQ00201":
            account_dict = dict()

            item = list()
            for idx in range(len(BALANCE_OUT_BLOCK_2_CODE)):
                out_block_code = BALANCE_OUT_BLOCK_2_CODE[idx]
                data = self.parent.query.GetFieldData("COSOQ00201OutBlock2", out_block_code, 0) # 서버로부터 데이터를 받아오는 부분, 만약에 accurs를 사용하는 경우 반복해서 가져오는 것이니 0 대신 idx를 사용
                item.append(data)
            # print(dict(zip(BALANCE_OUT_BLOCK_2_NAME, item)))

            item = list()
            for idx in range(len(BALANCE_OUT_BLOCK_3_CODE)):
                out_block_code = BALANCE_OUT_BLOCK_3_CODE[idx]
                data = self.parent.query.GetFieldData("COSOQ00201OutBlock3", out_block_code, 0)
                item.append(data)
            # print(dict(zip(BALANCE_OUT_BLOCK_3_NAME, item)))

            count = self.parent.query.GetBlockCount("COSOQ00201OutBlock4") # 데이터 조회에서 해외잔고의 종목의 수만큼 데이터를 조회, Count가 몇개 담겨있는지 length 알려주는 함수
            for cnt in range(count):
                item = list()
                for idx in range(len(BALANCE_OUT_BLOCK_4_CODE)):
                    out_block_code = BALANCE_OUT_BLOCK_4_CODE[idx]
                    data = self.parent.query.GetFieldData("COSOQ00201OutBlock2", out_block_code, cnt)
                    item.append(data)
                # print(dict(zip(BALANCE_OUT_BLOCK_4_NAME, item)))

                code = item[1]
                account_dict[code] = dict(zip(BALANCE_OUT_BLOCK_4_NAME, item))

            self.parent.account_dict = account_dict

        elif event == "COSOQ02701":
            self.parent.deposit = self.parent.query.GetFieldData("COSOQ02701OutBlock3", "FcurrOrdAbleAmt", 0) # 외화주문 가능금액

        elif event == "COSAQ00102":
            out_standing = dict()

            item = list()
            for idx in range(len(OUT_STANDING_OUT_BLOCK_1_CODE)):
                out_block_code = OUT_STANDING_OUT_BLOCK_1_CODE[idx]
                data = self.parent.query.GetFieldData("COSAQ00102OutBlock1", out_block_code, 0) # 서버로부터 데이터를 받아오는 부분, 만약에 accurs를 사용하는 경우 반복해서 가져오는 것이니 0 대신 idx를 사용
                item.append(data)
            # print(dict(zip(BALANCE_OUT_BLOCK_2_NAME, item)))

            item = list()
            for idx in range(len(OUT_STANDING_OUT_BLOCK_2_CODE)):
                out_block_code = OUT_STANDING_OUT_BLOCK_2_CODE[idx]
                data = self.parent.query.GetFieldData("COSAQ00102OutBlock2", out_block_code, 0)
                item.append(data)
            # print(dict(zip(BALANCE_OUT_BLOCK_3_NAME, item)))

            count = self.parent.query.GetBlockCount("COSAQ00102OutBlock3") # 데이터 조회에서 해외잔고의 종목의 수만큼 데이터를 조회, Count가 몇개 담겨있는지 length 알려주는 함수
            for cnt in range(count):
                item = list()
                for idx in range(len(OUT_STANDING_OUT_BLOCK_3_CODE)):
                    out_block_code = OUT_STANDING_OUT_BLOCK_3_CODE[idx]
                    data = self.parent.query.GetFieldData("COSAQ00102OutBlock3", out_block_code, cnt)
                    item.append(data)
                # print(dict(zip(BALANCE_OUT_BLOCK_4_NAME, item)))

                code = item[7]
                out_standing[code] = dict(zip(OUT_STANDING_OUT_BLOCK_3_NAME, item))

            self.parent.out_standing = out_standing

        elif event == "g3101":
            item = list()
            for idx in range(len(G3101_OUT_BLOCK_CODE)):
                out_block_code = G3101_OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData("g3101OutBlock", out_block_code, 0)
                item.append(data)
            print(dict(zip(G3101_OUT_BLOCK_NAME, item)))

        elif event == "g3102":
            item = list()
            # 단일 조회
            for idx in range(len(G3102_OUT_BLOCK_CODE)):
                out_block_code = G3102_OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData("g3102OutBlock", out_block_code, 0)
                item.append(data)
            print(dict(zip(G3102_OUT_BLOCK_NAME, item)))
            record = dict(zip(G3102_OUT_BLOCK_NAME, item))

            count = self.parent.query.GetBlockCount("g3102OutBlock1")
            for cnt in range(count):
                item = list()
                for idx in range(len(G3102_OUT_BLOCK_1_CODE)):
                    out_block_code = G3102_OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData("g3102OutBlock1", out_block_code, cnt)
                    item.append(data)
                print(dict(zip(G3102_OUT_BLOCK_1_NAME, item)))

            # 연속조회
            time.sleep(0.2)
            self.parent.g3102(exchange_code="82", symbol="TSLA", next_seq=record["연속시퀀스"], cont=True)



class XAQuery: # 주식 데이터 가져오기
    def __init__(self) -> None:
        self.deposit = 0
        self.account_dict = dict()
        self.out_standing = dict()
        self.response = False
        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryReceiver)
        self.query.parent = self # 상위 클래스에 권한 제공

    def request(self, cont=False):
        res = self.query.Request(cont) # 데이터 조회 - 연속조회 : True
        if res < 0 :
            print("데이터 요청에 실패했습니다.")
        
        self.response = False
        while not self.response:
            pythoncom.PumpWaitingMessages() # 데이터를 요청 받을때까지 기다림

    def request_balance(self, account_num, password):
        self.query.ResFileName = "c:/LS_SEC/xingAPI/Res/COSOQ00201.res"
        datas = ["00001", account_num, password, "", "USD", "00"]

        for idx in range(len(datas)):
            self.query.SetFieldData("COSOQ00201InBlock1", BALANCE_IN_BLOCK_CODE[idx], 0, datas[idx])

        self.request()

        return self.account_dict
    
    def request_deposit(self, account_num, password): # 예수금 조회
        self.query.ResFileName = "c:/LS_SEC/xingAPI/Res/COSOQ02701.res"
        datas = ["00001", account_num, password, "USD"]

        for idx in range(len(datas)):
            self.query.SetFieldData("COSOQ02701InBlock1", DEPOSIT_IN_BLOCK_CODE[idx], 0, datas[idx])

        self.request()

        return self.deposit

    def request_out_standing(self, account_num, password): # 미체결 잔고 조회
        self.query.ResFileName = "c:/LS_SEC/xingAPI/Res/COSAQ00102.res"
        datas = ["00001", "1", "2", "82", account_num, password, "0", "", "0", "", "2", "USD", "1", "0"] # 81뉴욕, 82나스닥

        for idx in range(len(datas)):
            self.query.SetFieldData("COSAQ00102InBlock1", OUT_STANDING_IN_BLOCK_CODE[idx], 0, datas[idx])

        self.request()

        return self.out_standing
    
    def g3101(self, exchange_code, symbol): # 현재가 조회
        '''
        exchange_code : 거래소 코드 (81-뉴욕, 82-나스닥)
        symbol : 종목코드
        '''
        self.query.ResFileName = "c:/LS_SEC/xingAPI/Res/g3101.res"
        datas = ["R", exchange_code + symbol, exchange_code, symbol] 

        for idx in range(len(datas)):
            self.query.SetFieldData("g3101InBlock", G3101_IN_BLOCK_CODE[idx], 0, datas[idx])

        self.request()
    
    def g3102(self, exchange_code, symbol, next_seq="", cont=False): # 해외주식 시간대별
        '''
        연속조회는 Occurs 데이터의 총 갯수가 너무 많아서 한번에 다 가져오지 못하는 것을 여러 번에 걸쳐서 가져오는 것입니다.
        -> 과거 데이터 계속해서 연속적으로 출력해 볼 수 있음 (나중에 이전 시퀀스 정보 필요시 사용가능한 코드)
        exchange_code : 거래소 코드 (81-뉴욕, 82-나스닥)
        symbol : 종목코드
        next_seq : 연속 조회용 시퀀스
        '''
        self.query.ResFileName = "c:/LS_SEC/xingAPI/Res/g3102.res"
        datas = ["R", exchange_code + symbol, exchange_code, symbol, "", next_seq] 

        for idx in range(len(datas)):
            self.query.SetFieldData("g3102InBlock", G3102_IN_BLOCK_CODE[idx], 0, datas[idx])

        self.request(cont=cont)

                