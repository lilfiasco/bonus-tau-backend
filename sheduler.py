import schedule
import time
import psycopg2
from psycopg2.extras import execute_values
from centercredit_parser import center_parser
from halyk_bank_parser import halyk_parser
from home_bank_parser import home_parser

def main():
    # Подключение к базе данных
    conn = psycopg2.connect("dbname=hacknu user=postgres password=alik030808")
    cur = conn.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS cards (title TEXT, cash INT)")
    
    data = center_parser() + home_parser() + halyk_parser()
    execute_values(cur, "INSERT INTO cards (title, cash) VALUES %s", data)
    
    conn.commit()
    cur.close()
    conn.close()

def update_date():
    print('start update')
    main()

schedule.every().wednesday.at("10:00").do(update_date)

while True:
    schedule.run_pending()
    time.sleep(10)