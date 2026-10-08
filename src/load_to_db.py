import pandas as pd
import sqlite3
import os

def load_to_sqlite():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, '..', 'data', 'poker_tournament_survival.csv')
    db_path = os.path.join(current_dir, '..', 'poker.db') # 数据库会生成在根目录

    print("正在读取CSV数据...")
    # 自动处理编码
    try:
        df = pd.read_csv(csv_path)
    except UnicodeDecodeError:
        df = pd.read_csv(csv_path, encoding='latin-1')

    print("正在连接SQLite数据库并写入数据...")
    conn = sqlite3.connect(db_path)
    
    # 将DataFrame写入数据库，表名就叫 poker_raw
    df.to_sql('poker_raw', conn, if_exists='replace', index=False)
    
    # 验证一下写进去了没有
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM poker_raw;")
    row_count = cursor.fetchone()[0]
    
    print(f"✅ 成功写入数据库！表名: poker_raw, 总行数: {row_count}")
    conn.close()

if __name__ == "__main__":
    load_to_sqlite()