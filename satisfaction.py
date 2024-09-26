from pandas._libs.hashtable import value_count
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
plt.rc('font', family='GULIM')

def satisfaction_graph(file_name, column_type):
    input_file = file_name
    data = pd.read_csv(input_file, encoding='cp949')
    
    # column_type 열의 값을 1&2로 합쳐서 처리
    data[column_type].replace({0 : 1,1: 1, 2: 1}, inplace=True)
    
    # column_type 열의 값들의 빈도를 계산
    satis = data[column_type].value_counts()
    
    # 각 값의 빈도를 배열로 변환하여 사용
    y_data = satis.values
    
    ratio = y_data / y_data.sum()
    # x 라벨도 1&2로 변경
    x_label = ['1&2' if label == 1 else label for label in satis.index.tolist()]
    
    plt.pie(ratio,
            labels=x_label,
            autopct='%.1f%%',
            startangle=90,
            counterclock=True,
            shadow=True,
            colors=['#ff9999', '#ffc000', '#8fd9b6', '#d395d0'],
            wedgeprops={'width':0.7, 'edgecolor':'w', 'linewidth':3}
            )
    plt.title(column_type, fontsize=20)
    plt.savefig(column_type + ".png")
    plt.close()
