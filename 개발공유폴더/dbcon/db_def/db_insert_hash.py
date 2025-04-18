import csv
import hashlib
from db.db_login import db_connect

def insert_hash(csv_file, table_name):
    db_connection = db_connect()
    cursor = db_connection.cursor()
    
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # 헤더 건너뜀

        for idx, row in enumerate(reader, start=1):
            row_data = ",".join(row)
            row_hash = hashlib.sha256(row_data.encode('utf-8')).hexdigest()

            # 해시값을 HE 테이블에 삽입
            insert_sql = f"INSERT INTO {table_name} (HashName) VALUES (?);"
            cursor.execute(insert_sql, (row_hash,))
            print(f"[{idx}] 해시 저장 완료 → {row_hash}")

        db_connection.commit()
        print("모든 해시값 커밋 완료 💾")
