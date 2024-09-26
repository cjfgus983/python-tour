import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='GULIM')

def city_visit_graph(file_name):
    plt.rcParams['axes.unicode_minus'] =False

    # CSV 파일 읽기
    input_file = file_name
    df = pd.read_csv(input_file, encoding='cp949')

    # 각 칼럼의 값이 있는 개수 세기
    count_data = df.notnull().sum()

    # 막대그래프 그리기 
    plt.figure(figsize=(10, 6))
    plt.bar(count_data.index, count_data.values)

    # x축 레이블을 45도 기울임
    plt.xticks(rotation=45)

    plt.xlabel('지역')
    plt.ylabel('Count')
    plt.title('외국인 방문 지역')

    plt.savefig("외국인 방문 지역 그래프.png")
    plt.close()
