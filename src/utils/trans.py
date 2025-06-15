doc_string = """
현지일자,locdate,locdate,char,8;
		현지시간,loctime,loctime,char,6;
		한국일자,kordate,kordate,char,8;
		한국시간,kortime,kortime,char,6;
		현재가,price,price,double,15.6;
		전일대비구분,sign,sign,char,1;
		전일대비,diff,diff,double,15.6;
		등락률,rate,rate,float,6.2;
		시가,open,open,double,15.6;
		고가,high,high,double,15.6;
		저가,low,low,double,15.6;
		체결량,exevol,exevol,long,10;
		체결구분,cgubun,cgubun,char,1;
		소숫점자릿수,floatpoint,floatpoint,char,1;
"""

item = list()
item2 = list()
data = doc_string.split("\n")[1:-1]

for idx in range(len(data)):
    res = data[idx].split(",")
    item.append(res[1].replace("\t", "").replace(" ", "").replace(";", ""))
    item2.append(res[0].replace("\t", "").replace(" ", "").replace(";", ""))

print(item)
print(item2)