import glob as glob
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
plt.rc('font', family='GULIM')
import pandas as pd
import folium
import googlemaps
import webbrowser
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer


gmaps_key = 'AIzaSyACFxEfY-a2bR_B7h86pyw07qTz4RKCCIc'  # API설정할 때 얻은 key
gmaps = googlemaps.Client(key=gmaps_key)

def clustering_path(file_path, save_file_name, k_count):
    allSeoul = pd.read_csv(file_path, encoding='cp949')

    allSeoul['소속구'] = allSeoul['주소'].str.split(" ").str[1]
    allSeoul

    gmaps = googlemaps.Client(key=gmaps_key)

    lat = []
    lng = []
    for name in allSeoul['주소']:
        try:
            tmpMap = gmaps.geocode(name, language='ko')
            tmpLoc = tmpMap[0].get('geometry')
            lat.append(tmpLoc['location']['lat'])
            lng.append(tmpLoc['location']['lng'])
        except:
            print("{} Address Error".format(name))
            lat.append(None)
            lng.append(None)
    allSeoul['위도'] = lat
    allSeoul['경도'] = lng
    
    data = allSeoul[['위도', '경도']]
    data = data.dropna()
    
    # 적절한 군집수 찾기
    # Inertia(군집 내 거리제곱합의 합) value (적정 군집수)

# 엘보우 주석 부분 =======================================
    # ks = range(1,10)
    # inertias = []

    # for k in ks:
    #     model = KMeans(n_clusters=k)
    #     model.fit(data)
    #     inertias.append(model.inertia_)

    # # Plot ks vs inertias
    # plt.figure(figsize=(4, 4))

    # plt.plot(ks, inertias, '-o')
    # plt.xlabel('number of clusters, k')
    # plt.ylabel('inertia')
    # plt.xticks(ks)
    # plt.savefig(save_file_name + "ElbowMethod.png")
    # plt.close()


    # == 엘보우 메소드 == 
    scaler = MinMaxScaler()
    data_scale = scaler.fit_transform(data)
    model = KMeans()
    visualizer = KElbowVisualizer(model, k=(1,10))
    visualizer.fit(data_scale)
    visualizer.show(outpath=save_file_name + "elbow_method.png")
    plt.clf()
    plt.cla()
    
    # K-Means 모델과 군집 예측값을 생성

    # 클러스터 모델 생성 파라미터는 원할 경우 추가
    clust_model = KMeans(n_clusters = k_count # 클러스터 갯수
                        )

    # 생성한 모델로 데이터를 학습시킴
    clust_model.fit(data) # unsupervised learning 

    # 결과 값을 변수에 저장
    centers = clust_model.cluster_centers_ # 각 군집의 중심점
    pred = clust_model.predict(data) # 각 예측군집

    # print(pd.DataFrame(centers))
    # print(pred[:10])
    Seoulcenter = pd.DataFrame(centers)
    Seoulcenter
    Seoulcenter.columns = ['위도','경도']
    Seoulcenter
    clust_df = data.copy()
    clust_df['clust'] = pred
    clust_df.head()
    df_f=data.copy()
    # scaling하지 않은 데이터를 학습하고 시각화하기

    plt.figure(figsize=(20, 6))

    X = clust_df

    plt.subplot(131)
    sns.scatterplot(x=X.iloc[:,0], y=X.iloc[:,1], data=df_f, hue=clust_model.labels_, palette='coolwarm')
    plt.scatter(centers[:,0], centers[:,1], c='black', alpha=0.8, s=150)

    plt.savefig(save_file_name + "Clustering.png")
    plt.close()
    # 정규화 진행
    data_size = len(allSeoul)
    loc = [37.533286,126.909059]

    centerdata_size = len(Seoulcenter)

    map = folium.Map(location=loc, zoom_start=12)

    for i in range(data_size):
        folium.Marker(list(allSeoul.iloc[i][['위도', '경도']]),icon=folium.Icon(color = 'blue')).add_to(map)

    for i in range(centerdata_size):
        folium.Marker(list(Seoulcenter.iloc[i][['위도', '경도']]), icon=folium.Icon(color = 'red')).add_to(map)


    map.save(save_file_name + ".html")

    # 웹 브라우저에서 열기
    webbrowser.open(save_file_name + ".html")
    