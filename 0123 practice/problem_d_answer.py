import json


def max_revenue(movies):
    pass
    # 여기에 코드를 작성합니다.  
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))