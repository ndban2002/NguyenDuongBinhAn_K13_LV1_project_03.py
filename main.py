import pandas as pd

def load_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError as err:
        raise 'Load Error'
def replace_wrong_year(df):
    return df['release_date'].replace(year=df['release_year'])
def task1(df):
    df['release_date'] = pd.to_datetime(df['release_date'], format='%m/%d/%y')
    df['release_date'] = df.apply(replace_wrong_year, axis=1)
    df_sorted = df.sort_values(by = 'release_date', ascending=False)
    df_sorted.to_csv('task1.csv')
    return df_sorted
def task2(df):
    result = df.loc[df['vote_average'] > 7.5]
    result.sort_values(by='vote_average', ascending=False)
    result.to_csv('task2.csv')
    return result
def task3(df):
    df = df.loc[df['revenue_adj'] > 0]
    max = df.loc[df['revenue_adj'] == df['revenue_adj'].max()]
    min = df.loc[df['revenue_adj'] == df['revenue_adj'].min()]
    return max, min
def task4(df):
    return df['revenue'].sum()
def task5(df):
    df['profit'] = df['revenue_adj'] - df['budget_adj']
    result = df.sort_values(by = 'profit', ascending=False).head(10)
    return result
def task6(df):
    df_split = df['cast'].str.split('|').explode().reset_index(drop=True)
    df_exploded = pd.DataFrame({'director': df['director'],'cast': df_split})
    cast_count = df_exploded.value_counts(subset='cast')

    director_count = df_exploded.value_counts(subset='director')
    return director_count.head(1), cast_count.head(1)
def task7(df):
    df_split = df['genres'].str.split('|').explode().reset_index(drop=True)
    df_exploded = pd.DataFrame({'genres': df_split})
    return df_exploded.value_counts(subset='genres')
if __name__ == '__main__':
    #Load file csv
    file_path = 'https://raw.githubusercontent.com/yinghaoz1/tmdb-movie-dataset-analysis/master/tmdb-movies.csv'
    df = load_file(file_path)
    #Task 1
    print(task1(df).head())

    #Task 2
    print(task2(df).head())

    #Task 3
    max, min = task3(df)
    print('Highest Revenue: ', max.to_string())
    print('Lowest Revenues: ', min.to_string())

    #Task 4
    print('Total Revenue: ', task4(df).to_string())

    #Task 5
    print('Top 10 highest revenue movie: ', task5(df).to_string())

    #Task 6
    director, cast = task6(df)
    print(director.to_string())
    print(cast.to_string())

    #Task 7
    print(task7(df).to_string())