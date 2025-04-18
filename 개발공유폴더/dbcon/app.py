from db_def.db_insert_dataset import insert_dataset
from db_def.db_insert_hash import insert_hash
from db_def.db_print_dataset_table import print_dataset_table
from db_def.db_print_hash_table import print_hash_table

if __name__ == '__main__':
    csv_file = r"C:\Users\pth81\Desktop\data\dataset_malwares14.csv"

    #csv 에 있는 PE 값을 DB에 저장하는 함수
    #insert_dataset(csv_file, "TEE")

    #csv 에 있는 PE 값을 HASH화 해서 DB에 저장하는 함수
    #insert_hash(csv_file, "HAA")

    #TE 테이블 전체 출력
    #print_dataset_table("TEE")

    #HA 테이블 전체 출력
    print_hash_table("HAA")