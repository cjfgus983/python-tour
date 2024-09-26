from clustering import clustering_path # 클러스팅 해서 구글맵에 표시
from find_main_area import find_area # 관광지의 소속구 비율 막대그래프로 
from city_visit import city_visit_graph # 방한외국인의 방문 도시를 막대그래프로
from satisfaction import satisfaction_graph
from visit_korea_count import visit_korea_count_func
from purpose_visit import purpose_visit_korea

# 방한 외국인 수
visit_korea_count_func('데이터셋/방한관광객.csv')

# 방한목적
purpose_visit_korea()

# # 만족도
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='전반적 만족도')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='출입국 절차')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='대중교통')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='숙박')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='음식')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='쇼핑')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='관광지 매력도')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='언어소통')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='여행경비')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='치안(안전성)')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='길 찾기')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='모바일,인터넷 이용 편의')
satisfaction_graph('데이터셋/만족도데이터.csv', column_type='관광안내서비스')

# 어디 도시를 많이 방문하는지
city_visit_graph('데이터셋/권역방문데이터.csv')

#서울에서 어디 구역에 관광지가 몰려있는지
find_area('데이터셋/서울전체.csv')
clustering_path('데이터셋/서울전체.csv', save_file_name="서울", k_count=3)

# 3개의 구역에서 어디에 안내소를 설치하면 좋을지
clustering_path('데이터셋/강남구.csv', save_file_name="강남구", k_count=3)
clustering_path('데이터셋/중구.csv', save_file_name="중구", k_count=3)
clustering_path('데이터셋/송파구.csv', save_file_name="송파구", k_count=3)