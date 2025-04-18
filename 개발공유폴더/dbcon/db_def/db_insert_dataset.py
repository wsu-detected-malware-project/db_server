import csv
from db.db_login import db_connect
from columns.db_columns import column_order  # 컬럼 리스트 가져옴

def insert_dataset(csv_file, table_name):
    db_connection = db_connect()
    cursor = db_connection.cursor()

    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # 헤더는 건너뜀

        # INSERT 쿼리 생성 (너가 짠 방식으로)
        insert_query = f"""
            INSERT INTO [dbo].[{table_name}] (
                {', '.join(column_order)}
            ) VALUES ({', '.join(['?'] * len(column_order))});
        """

        for idx, row in enumerate(csv_reader, start=1):
            # row 개수가 컬럼 개수랑 다르면 스킵 또는 예외 처리
            if len(row) != len(column_order):
                print(f"[{idx}] ⚠️ 데이터 컬럼 수 불일치 (row length={len(row)}), 건너뜀")
                continue

            cursor.execute(insert_query, row)
            print(f"[{idx}] 삽입 성공")

        db_connection.commit()
        print("✅ 모든 데이터 삽입 완료!")

    cursor.close()
    db_connection.close()
