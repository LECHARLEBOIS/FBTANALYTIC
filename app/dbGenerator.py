import pymysql
def supplierGenerator ():
    conn = pymysql.connect(host='localhost', user='root', password='asdf1234', db='PEAKDB')
    cur = conn.cursor()

    with open("supplierEntry","r") as file:
        for line in file:
            supplier, name = line.strip().split(",")
            query = f"""INSERT INTO supplier (supplierCode, supplierName) VALUES ('{supplier}','{name}');"""
            cur.execute(query)
            conn.commit()

    cur.close()
    conn.close()


def processGenerator ():
    conn = pymysql.connect(host='localhost', user='root', password='asdf1234', db='PEAKDB')
    cur = conn.cursor()

    with open("processEntry","r") as file:
        for line in file:
            processID, processType = line.strip().split(",")
            query = f"""INSERT INTO process (processID, processType) VALUES ('{processID}','{processType}');"""
            cur.execute(query)
            conn.commit()

    cur.close()
    conn.close()

def vehiculeGenerator ():
    conn = pymysql.connect(host='localhost', user='root', password='asdf1234', db='PEAKDB')
    cur = conn.cursor()

    with open("vehiculeEntry","r") as file:
        for line in file:
            vehiculeID, vehiculeName = line.strip().split(",")
            query = f"""INSERT INTO vehicule (vehiculeID, vehiculeName) VALUES ('{vehiculeID}','{vehiculeName}');"""
            cur.execute(query)
            conn.commit()

    cur.close()
    conn.close()

def systemVehGenerator ():
    conn = pymysql.connect(host='localhost', user='root', password='asdf1234', db='PEAKDB')
    cur = conn.cursor()

    with open("systemVehEntry","r") as file:
        for line in file:
            systemID, systemName, lienVehicule = line.strip().split(",")
            query = f"""INSERT INTO systemVeh (systemID, systemName, lienVehicule) VALUES ('{systemID}','{systemName}','{lienVehicule}');"""
            cur.execute(query)
            conn.commit()

    cur.close()
    conn.close()

def partGenerator ():
    conn = pymysql.connect(host='localhost', user='root', password='asdf1234', db='PEAKDB')
    cur = conn.cursor()

    with open("partEntry","r") as file:
        for line in file:
            partnumber, description, materialgroup,liensupplier,lienprocess,liensystem = line.strip().split(",")
            query = f"""INSERT INTO part (partnumber, description, materialgroup, lienSupplier, lienProcess,lienSystem) VALUES ({partnumber},'{description}','{materialgroup}',{liensupplier},{lienprocess},{liensystem});"""
            cur.execute(query)
            conn.commit()

    cur.close()
    conn.close()

def indexDriverGenerator ():
    conn = pymysql.connect(host='localhost', user='root', password='asdf1234', db='PEAKDB')
    cur = conn.cursor()

    with open("indexDriverEntry","r") as file:
        for line in file:
            indexID, indexType, indexOrigin,indexAmount = line.strip().split(",")
            query = f"""INSERT INTO indexDriver (indexID, indexType, indexOrigin, indexAmount) VALUES ({indexID},'{indexType}','{indexOrigin}',{indexAmount});"""
            cur.execute(query)
            conn.commit()

    cur.close()
    conn.close()

def costDriverGenerator ():
    conn = pymysql.connect(host='localhost', user='root', password='asdf1234', db='PEAKDB')
    cur = conn.cursor()

    with open("costDriverEntry","r") as file:
        for line in file:
            costDriverID, costDriverType, costDriverPrice,costDriverDescr,lienPartNumber,lienIndex = line.split(",")
            query = f"""INSERT INTO costDriver (costDriverID, costDriverType, costDriverDescr, costDriverPrice, lienPartNumber, lienIndex) VALUES ({costDriverID},'{costDriverType}','{costDriverDescr}',{costDriverPrice},{lienPartNumber},{lienIndex});"""
            cur.execute(query)
            conn.commit()

    cur.close()
    conn.close()


def DBGeneration ():
    supplierGenerator()
    processGenerator()
    vehiculeGenerator()
    systemVehGenerator()
    partGenerator()
    indexDriverGenerator()
    costDriverGenerator()

DBGeneration()