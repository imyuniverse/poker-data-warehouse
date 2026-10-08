import pandas as pd
import os

def explore_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    filepath = os.path.join(current_dir, '..', 'data', 'poker_tournament_survival.csv')
    
    print("正在读取数据...")
    
    # 加个 try-except 防止编码报错
    try:
        df = pd.read_csv(filepath)
    except UnicodeDecodeError:
        print("遇到编码错误，尝试用 latin-1 编码重新读取...")
        df = pd.read_csv(filepath, encoding='latin-1')
        
    print("✅ 读取成功！")
    print("========================")
    print("数据形状（行数, 列数）:", df.shape)
    print("========================")
    
    print("\n前 5 行数据：")
    print(df.head())
    
    print("\n各列数据类型：")
    print(df.dtypes)
    
    print("\n各列缺失值数量：")
    print(df.isnull().sum())

if __name__ == "__main__":
    explore_data()
