import pymysql
def supplierGenerator ():
    conn = pymysql.connect(host='localhost', user='root', password='asdf1234', db='PEAKDB')
    cur = conn.cursor()

    supplierList = []

    with open("supplierEntry","r") as file:
        for line in file:
            supplier, name = line.strip().split(",")
            query = f"""INSERT INTO supplier (supplierCode, supplierName) VALUES ('{supplier}','{name}');"""
            cur.execute(query)
            conn.commit()

    cur.close()
    conn.close()


def DBGeneration ():
    supplierGenerator()


DBGeneration()