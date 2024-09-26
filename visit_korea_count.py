import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='GULIM')

def visit_korea_count_func(file_path):
    
    df = pd.read_csv(file_path, encoding='cp949')

    # '기준년월'과 '방한외래관광객' 열만 선택
    df_selected = df[['기준년월', '방한 외래관광객']]

    # 데이터를 리스트로 변환
    months = df_selected['기준년월'].tolist()
    months = [str(month) for month in months]  # Convert to string
    visitors = df_selected['방한 외래관광객'].tolist()


    plt.figure(figsize=(12, 6))
    plt.plot(months, visitors, marker='o')

    # 그래프 제목 및 축 레이블 설정
    plt.title('방한외래관광객 수 (기준년월별)', fontsize=16)
    plt.xlabel('기준년월', fontsize=14)
    plt.ylabel('방한외래관광객 수', fontsize=14)

    # x축 눈금 레이블 회전 설정
    plt.xticks(rotation=45)

    # 그래프 그리기
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("방한관광객 추이.png")
    plt.close()
