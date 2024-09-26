import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.rc('font', family='GULIM')

def purpose_visit_korea():
    data = pd.read_csv('데이터셋/2019_총괄.csv', encoding='cp949')
    reason_korea = data['문5-2. 한국 방문 선택 시 고려 요인1']
    reason_np = np.array(reason_korea)
    reason_1 = len(data.loc[data['문5-1. 주요 방한 목적'] == 1])
    reason_2 = len(data.loc[data['문5-1. 주요 방한 목적'] == 2])
    reason_3 = len(data.loc[data['문5-1. 주요 방한 목적'] == 3])
    reason_4 = len(data.loc[data['문5-1. 주요 방한 목적'] == 4])
    reason_5 = len(data.loc[data['문5-1. 주요 방한 목적'] == 5])
    reason_6 = len(data.loc[data['문5-1. 주요 방한 목적'] == 6])
    
    reason_x = ["1. 여가, 위락, 휴식", "2. 친구, 친지 방문", "3. 사업 또는 전문활동", "4. 교육", "5. 종교 및 순례", "6. 기타"]
    reason_y = [reason_1, reason_2, reason_3, reason_4, reason_5, reason_6]
    plt.figure(figsize=(12, 10))
    plt.bar(reason_x, reason_y)
    plt.xticks(reason_x, reason_x)

    plt.xticks(rotation=45)

    plt.title("why visit Korea")

    plt.savefig("한국 방문 목적.png")
    plt.close()