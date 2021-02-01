import json

def max_revenue(movies):

    result = '' # 수익이 가장 높은 영화 제목
    revenue = 0 # 수익이 가장 높은 영화의 수익

    for movie in movies:
        # movie id를 기준으로 movie 상세정보 파일 읽기 (movie_id.json 파일)
        movie_id = movie.get('id')
        movie_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_detail = json.load(movie_json)
        # print(movie_detail)

        #revenue 데이터 추출
        movie_revenue = movie_detail['revenue']
        movie_title = movie_detail['title']

        # 가장 높은 revenue를 기록한 movie title 찾기
        if movie_revenue > revenue:
            revenue = movie_revenue
            title = movie_title
    return title


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    

    print(max_revenue(movies_list))