import os
from clustering import clustering_path
from find_main_area import find_area
from city_visit import city_visit_graph
from satisfaction import satisfaction_graph
from visit_korea_count import visit_korea_count_func
from purpose_visit import purpose_visit_korea

def test_visit_korea_count_func():
    try:
        visit_korea_count_func('데이터셋/방한관광객.csv')
        print("visit_korea_count_func passed")
    except Exception as e:
        print(f"visit_korea_count_func failed: {e}")

def test_purpose_visit_korea():
    try:
        purpose_visit_korea()
        print("purpose_visit_korea passed")
    except Exception as e:
        print(f"purpose_visit_korea failed: {e}")

def test_satisfaction_graph():
    columns = [
        '전반적 만족도', '출입국 절차', '대중교통', '숙박', '음식', 
        '쇼핑', '관광지 매력도', '언어소통', '여행경비', '치안(안전성)', 
        '길 찾기', '모바일,인터넷 이용 편의', '관광안내서비스'
    ]
    for column in columns:
        try:
            satisfaction_graph('데이터셋/만족도데이터.csv', column_type=column)
            print(f"satisfaction_graph for {column} passed")
        except Exception as e:
            print(f"satisfaction_graph for {column} failed: {e}")

def test_city_visit_graph():
    try:
        city_visit_graph('데이터셋/권역방문데이터.csv')
        print("city_visit_graph passed")
    except Exception as e:
        print(f"city_visit_graph failed: {e}")

def test_find_area():
    try:
        find_area('데이터셋/서울전체.csv')
        print("find_area passed")
    except Exception as e:
        print(f"find_area failed: {e}")

def test_clustering_path():
    clustering_tests = [
        ('데이터셋/서울전체.csv', "서울", 3),
        ('데이터셋/강남구.csv', "강남구", 3),
        ('데이터셋/중구.csv', "중구", 3),
        ('데이터셋/송파구.csv', "송파구", 3)
    ]
    for dataset, save_file_name, k_count in clustering_tests:
        try:
            clustering_path(dataset, save_file_name, k_count)
            print(f"clustering_path for {save_file_name} passed")
        except Exception as e:
            print(f"clustering_path for {save_file_name} failed: {e}")

if __name__ == "__main__":
    test_visit_korea_count_func()
    test_purpose_visit_korea()
    test_satisfaction_graph()
    test_city_visit_graph()
    test_find_area()
    test_clustering_path()
