# 계좌 잔고 조회 COSOQ00201
BALANCE_IN_BLOCK_CODE = ['RecCnt', 'AcntNo', 'Pwd', 'BaseDt', 'CrcyCode', 'AstkBalTpCode']
BALANCE_IN_BLOCK_NAME = ['레코드갯수', '계좌번호', '비밀번호', '기준일자', '통화코드', '해외증권잔고구분코드']
BALANCE_OUT_BLOCK_2_CODE = ['RecCnt', 'ErnRat', 'DpsConvEvalAmt', 'StkConvEvalAmt', 'DpsastConvEvalAmt', 'WonEvalSumAmt', 'ConvEvalPnlAmt', 'WonDpsBalAmt', 'D2EstiDps', 'LoanAmt']
BALANCE_OUT_BLOCK_2_NAME = ['레코드갯수', '수익율', '예수금환산평가금액', '주식환산평가금액', '예탁자산환산평가금액', '원화평가합계금액', '환산평가손익금액', '원화예수금잔고금액', 'D2추정예수금', '대출금액']
BALANCE_OUT_BLOCK_3_CODE = ['CrcyCode', 'FcurrDps', 'FcurrEvalAmt', 'FcurrEvalPnlAmt', 'PnlRat', 'BaseXchrat', 'DpsConvEvalAmt', 'PchsAmt', 'StkConvEvalAmt', 'ConvEvalPnlAmt', 'FcurrBuyAmt', 'FcurrOrdAbleAmt', 'LoanAmt']
BALANCE_OUT_BLOCK_3_NAME = ['통화코드', '외화예수금', '외화평가금액', '외화평가손익금액', '손익율', '기준환율', '예수금환산평가금액', '매입금액', '주식환산평가금액', '환산평가손익금액', '외화매수금액', '외화주문가능금액', '대출금액']
BALANCE_OUT_BLOCK_4_CODE = ['CrcyCode', 'ShtnIsuNo', 'IsuNo', 'JpnMktHanglIsuNm', 'AstkBalTpCode', 'AstkBalTpCodeNm', 'AstkBalQty', 'AstkSellAbleQty', 'FcstckUprc', 'FcurrBuyAmt', 'FcstckMktIsuCode', 'OvrsScrtsCurpri', 'FcurrEvalAmt', 'FcurrEvalPnlAmt', 'PnlRat', 'BaseXchrat', 'PchsAmt', 'DpsConvEvalAmt', 'StkConvEvalAmt', 'ConvEvalPnlAmt', 'AstkSettQty', 'MktTpNm', 'FcurrMktCode', 'LoanDt', 'LoanDtlClssCode', 'LoanAmt', 'DueDt', 'AstkBasePrc']
BALANCE_OUT_BLOCK_4_NAME = ['통화코드', '단축종목번호', '종목번호', '일본시장한글종목명', '해외증권잔고구분코드', '해외증권잔고구분코드명', '해외증권잔고수량', '해외증권매도가능수량', '외화증권단가', '외화매수금액', '외화증권시장종목코드', '해외증권시세', '외화평가금액', '외화평가손익금액', '손익율', '기준환율', '매입금액', '예수금환산평가금액', '주식환산평가금액', '환산평가손익금액', '해외증권결제수량', '시장구분명', '외화시장코드', '대출일자', '대출상세분류코드', '대출금액', '만기일자', '해외증권기준가격']

# 예수금 조회 COSOQ02701
DEPOSIT_IN_BLOCK_CODE = ['RecCnt', 'AcntNo', 'Pwd', 'CrcyCode']
DEPOSIT_IN_BLOCK_NAME = ['레코드갯수', '계좌번호', '비밀번호', '통화코드']

# 계좌주문체결내역 조회 COSAQ00102
OUT_STANDING_IN_BLOCK_CODE = ['RecCnt', 'QryTpCode', 'BkseqTpCode', 'OrdMktCode', 'AcntNo', 'Pwd', 'BnsTpCode', 'IsuNo', 'SrtOrdNo', 'OrdDt', 'ExecYn', 'CrcyCode', 'ThdayBnsAppYn', 'LoanBalHldYn']
OUT_STANDING_IN_BLOCK_NAME = ['레코드갯수', '조회구분코드', '역순구분코드', '주문시장코드', '계좌번호', '비밀번호', '매매구분코드', '종목번호', '시작주문번호', '주문일자', '체결여부', '통화코드', '당일매매적용여부', '대출잔고보유여부']
OUT_STANDING_OUT_BLOCK_1_CODE = ['RecCnt', 'QryTpCode', 'BkseqTpCode', 'OrdMktCode', 'AcntNo', 'Pwd', 'BnsTpCode', 'IsuNo', 'SrtOrdNo', 'OrdDt', 'ExecYn', 'CrcyCode', 'ThdayBnsAppYn', 'LoanBalHldYn']
OUT_STANDING_OUT_BLOCK_1_NAME = ['레코드갯수', '조회구분코드', '역순구분코드', '주문시장코드', '계좌번호', '비밀번호', '매매구분코드', '종목번호', '시작주문번호', '주문일자', '체결여부', '통화코드', '당일매매적용여부', '대출잔고보유여부']
OUT_STANDING_OUT_BLOCK_2_CODE = ['RecCnt', 'AcntNm', 'JpnMktHanglIsuNm', 'MgmtBrnNm', 'SellExecFcurrAmt', 'SellExecQty', 'BuyExecFcurrAmt', 'BuyExecQty']
OUT_STANDING_OUT_BLOCK_2_NAME = ['레코드갯수', '계좌명', '일본시장한글종목명', '관리지점명', '매도체결외화금액', '매도체결수량', '매수체결외화금액', '매수체결수량']
OUT_STANDING_OUT_BLOCK_3_CODE = ['MgmtBrnNo', 'AcntNo', 'AcntNm', 'ExecTime', 'OrdTime', 'OrdNo', 'OrgOrdNo', 'ShtnIsuNo', 'OrdTrxPtnNm', 'OrdTrxPtnCode', 'MrcAbleQty', 'OrdQty', 'OvrsOrdPrc', 'ExecQty', 'OvrsExecPrc', 'OrdprcPtnCode', 'OrdprcPtnNm', 'OrdPtnNm', 'OrdPtnCode', 'MrcTpCode', 'MrcTpNm', 'AllExecQty', 'CommdaCode', 'OrdMktCode', 'MktNm', 'CommdaNm', 'JpnMktHanglIsuNm', 'UnercQty', 'CnfQty', 'CrcyCode', 'RegMktCode', 'IsuNo', 'BrkTpCode', 'OppBrkNm', 'BnsTpCode', 'LoanDt', 'LoanAmt']
OUT_STANDING_OUT_BLOCK_3_NAME = ['관리지점번호', '계좌번호', '계좌명', '체결시각', '주문시각', '주문번호', '원주문번호', '단축종목번호', '주문처리유형명', '주문처리유형코드', '정정취소가능수량', '주문수량', '해외주문가', '체결수량', '해외체결가', '호가유형코드', '호가유형명', '주문유형명', '주문유형코드', '정정취소구분코드', '정정취소구분명', '전체체결수량', '통신매체코드', '주문시장코드', '시장명', '통신매체명', '일본시장한글종목명', '미체결수량', '확인수량', '통화코드', '등록시장코드', '종목번호', '중개인구분코드', '상대중개인명', '매매구분코드', '대출일자', '대출금액']

# 현재가조회 g3101
G3101_IN_BLOCK_CODE = ['delaygb', 'keysymbol', 'exchcd', 'symbol']
G3101_IN_BLOCK_NAME = ['지연구분', 'KEY종목코드', '거래소코드', '종목코드']
G3101_OUT_BLOCK_CODE = ['delaygb', 'keysymbol', 'exchcd', 'exchange', 'suspend', 'sellonly', 'symbol', 'korname', 'induname', 'floatpoint', 'currency', 'price', 'sign', 'diff', 'rate', 'volume', 'amount', 'high52p', 'low52p', 'uplimit', 'dnlimit', 'open', 'high', 'low', 'perv', 'epsv']
G3101_OUT_BLOCK_NAME = ['지연구분', 'KEY종목코드', '거래소코드', '거래소ID', '거래상태', '매매구분', '종목코드', '한글종목명', '업종한글명', '소숫점자릿수', '외환코드', '현재가', '전일대비구분', '전일대비', '등락률', '거래량', '거래대금', '52주최고가', '52주최저가', '상한가', '하한가', '시가', '고가', '저가', 'PER', 'EPS']

# 해외주식 시간대별 g3102
G3102_IN_BLOCK_CODE = ['delaygb', 'keysymbol', 'exchcd', 'symbol', 'readcnt', 'cts_seq']
G3102_IN_BLOCK_NAME = ['지연구분', 'KEY종목코드', '거래소코드', '종목코드', '조회갯수', '연속시퀀스']
G3102_OUT_BLOCK_CODE = ['delaygb', 'keysymbol', 'exchcd', 'symbol', 'cts_seq', 'rec_count']
G3102_OUT_BLOCK_NAME = ['지연구분', 'KEY종목코드', '거래소코드', '종목코드', '연속시퀀스', '레코드카운트']
G3102_OUT_BLOCK_1_CODE = ['locdate', 'loctime', 'kordate', 'kortime', 'price', 'sign', 'diff', 'rate', 'open', 'high', 'low', 'exevol', 'cgubun', 'floatpoint']
G3102_OUT_BLOCK_1_NAME = ['현지일자', '현지시간', '한국일자', '한국시간', '현재가', '전일대비구분', '전일대비', '등락률', '시가', '고가', '저가', '체결량', '체결구분', '소숫점자릿수']