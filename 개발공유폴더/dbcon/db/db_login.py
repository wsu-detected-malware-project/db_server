import pyodbc

# DB 연결 함수
def db_connect():
    try:
        # SQL Server 연결 (TrustServerCertificate=yes 추가)
        db_connection = pyodbc.connect(
            r"Driver={ODBC Driver 18 for SQL Server};"  # 드라이버 이름
            r"Server=DESKTOP-LGI1JDQ\SQLEXPRESS;"  # 서버 이름
            r"Database=test;"                      # 사용할 데이터베이스
            r"UID=sa;"                             # 사용자 이름
            r"PWD=root;"                           # 비밀번호
            r"TrustServerCertificate=yes;"         # SSL 인증서 문제 무시
        )

        # 연결 성공 확인
        if db_connection:
            print("SQL Server 데이터베이스에 연결되었습니다.")
        return db_connection
    except pyodbc.Error as err:
        print(f"Error: {err}")
        return None