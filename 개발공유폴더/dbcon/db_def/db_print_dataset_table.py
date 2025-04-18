import pyodbc
from db.db_login import db_connect

def print_dataset_table(table_name):
    try:
        db_connection = db_connect()

        # 커서 객체 생성
        cursor = db_connection.cursor()

        # TE 테이블에서 모든 데이터 조회
        select_sql = f"SELECT * FROM [dbo].[{table_name}];"

        cursor.execute(select_sql)
        rows = cursor.fetchall()  # 모든 행을 가져옵니다

        # 조회된 데이터를 출력
        print(f"{table_name} 테이블의 모든 데이터:")
        num = 0
        for row in rows:
            print(row)
            num += 1


        print(num, "개")
        # 연결 종료
        db_connection.close()

    except pyodbc.Error as err:
        print(f"Error: {err}")