import glob as glob
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
plt.rc('font', family='GULIM')
import pandas as pd


def find_area(file_path): 
    
    allSeoul = pd.read_csv(file_path, encoding='cp949')

    allSeoul['소속구'] = allSeoul['주소'].str.split(" ").str[1]
    allSeoul
    
    CountStatus = pd.value_counts(allSeoul['소속구'].values, sort=True)
    CountStatus.plot.bar()
    CountStatus.plot.bar(grid=True, figsize=(8,6), fontsize=15)
    plt.title('Distribution of Areas', fontsize=18)
    plt.xticks(rotation = 45)
    plt.savefig("서울관광지 소속구 분포.png")
    plt.close()