import pyodbc
import csv
import hashlib

def connect_to_db():
    print("🟡 DB 연결 시도 중...")  # 디버깅용 메시지

    try:
        connection = pyodbc.connect(
            r"Driver={ODBC Driver 18 for SQL Server};"
            r"Server=DESKTOP-LGI1JDQ\SQLEXPRESS;"
            r"Database=test;"
            r"UID=sa;"
            r"PWD=root;"
            r"TrustServerCertificate=yes;"
        )
        print("✅ DB 연결 성공")
        return connection
    except pyodbc.Error as e:
        print(f"❌ DB 연결 실패: {e}")  # 실패 이유 표시
        return None

def insert_hash_to_he(csv_file, db_connection):
    cursor = db_connection.cursor()
    
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # 헤더 건너뜀

        for idx, row in enumerate(reader, start=1):
            row_data = ",".join(row)
            row_hash = hashlib.sha256(row_data.encode('utf-8')).hexdigest()

            # 해시값을 HE 테이블에 삽입
            insert_sql = "INSERT INTO HE (HashName) VALUES (?);"
            cursor.execute(insert_sql, (row_hash,))
            print(f"[{idx}] 해시 저장 완료 → {row_hash}")

        db_connection.commit()
        print("모든 해시값 커밋 완료 💾")

def main():
    csv_file = r"C:\Users\pth81\Desktop\data\dataset_malwares.csv"
    db_connection = connect_to_db()
    if db_connection:
        insert_hash_to_he(csv_file, db_connection)
        db_connection.close()

if __name__ == "__main__":
    main()
