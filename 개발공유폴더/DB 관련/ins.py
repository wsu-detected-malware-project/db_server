import pyodbc
import csv

def check_sql_server_connection():
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

def insert_data_from_csv(csv_file, db_connection):
    cursor = db_connection.cursor()

    # CSV 파일 열기
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # 헤더는 건너뜁니다

        # 각 행을 데이터베이스에 삽입
        for row in csv_reader:
            # 데이터가 올바른지 확인하고, 삽입할 SQL 문을 작성
            insert_sql = f"""
                INSERT INTO [dbo].[TE] (
                    Name, e_magic, e_cblp, e_cp, e_crlc, e_cparhdr, e_minalloc, e_maxalloc, e_ss,
                    e_sp, e_csum, e_ip, e_cs, e_lfarlc, e_ovno, e_oemid, e_oeminfo, e_lfanew, Machine,
                    NumberOfSections, TimeDateStamp, PointerToSymbolTable, NumberOfSymbols, SizeOfOptionalHeader,
                    Characteristics, Magic, MajorLinkerVersion, MinorLinkerVersion, SizeOfCode,
                    SizeOfInitializedData, SizeOfUninitializedData, AddressOfEntryPoint, BaseOfCode, ImageBase,
                    SectionAlignment, FileAlignment, MajorOperatingSystemVersion, MinorOperatingSystemVersion,
                    MajorImageVersion, MinorImageVersion, MajorSubsystemVersion, MinorSubsystemVersion,
                    SizeOfHeaders, CheckSum, SizeOfImage, Subsystem, DllCharacteristics, SizeOfStackReserve,
                    SizeOfStackCommit, SizeOfHeapReserve, SizeOfHeapCommit, LoaderFlags, NumberOfRvaAndSizes,
                    Malware, SuspiciousImportFunctions, SuspiciousNameSection, SectionsLength, SectionMinEntropy,
                    SectionMaxEntropy, SectionMinRawsize, SectionMaxRawsize, SectionMinVirtualsize,
                    SectionMaxVirtualsize, SectionMaxPhysical, SectionMinPhysical, SectionMaxVirtual,
                    SectionMinVirtual, SectionMaxPointerData, SectionMinPointerData, SectionMaxChar,
                    SectionMainChar, DirectoryEntryImport, DirectoryEntryImportSize, DirectoryEntryExport,
                    ImageDirectoryEntryExport, ImageDirectoryEntryImport, ImageDirectoryEntryResource,
                    ImageDirectoryEntryException, ImageDirectoryEntrySecurity
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """

            # 데이터 삽입
            cursor.execute(insert_sql, row)

        # 변경사항 커밋
        db_connection.commit()


def main():
    #csv_file = "path_to_your_csv_file.csv"  # CSV 파일 경로를 여기에 넣으세요
    csv_file = r"C:\Users\pth81\Desktop\data\dataset_malwares.csv"
    
    # SQL Server에 연결
    db_connection = check_sql_server_connection()
    if db_connection:
        # CSV 파일에서 데이터를 읽어와 테이블에 삽입
        insert_data_from_csv(csv_file, db_connection)

        # 연결 종료
        db_connection.close()


if __name__ == "__main__":
    main()