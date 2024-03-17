import streamlit as st
import pandas as pd

def main():
    st.title('웹 대시보드')

    df = pd.read_csv('data/iris.csv')

    # 버튼
    if st.button('데이터 보기'):
        st.write(df)

    name = 'Mike'
    # 대문자 버튼을 누르면, 대문자로 표시하고
    # 소문자 버튼을 누르면, 소문자로 나오게 하자.
    if st.button('대문자'):
        st.text(name.upper())
    if st.button('소문자'):
        st.text(name.lower())

    st.dataframe(df)

    # petal_length 컬럼을 정렬하고 싶다.
    # 오름차순정렬, 내림차순 정렬 두가지 옵션 선택토록

    status = st.radio('정렬을 선택하세요.', ['오름차순', '내림차순'])
    # 오름차순이나 내림차순을 선택했을 때 리턴을 status에
    # print(status) # 오름차순 or 내림차순
    if status == '오름차순':
        st.dataframe(df.sort_values('petal_length'))
    elif status == '내림차순':
        st.dataframe(df.sort_values('petal_length', ascending=False))

    if st.checkbox('데이터프레임 보이기'): # True 또는 False 리턴
        st.dataframe(df.head(3))
    else:
        st.write('데이터가 없습니다.')
    

    # 여러개 중에 1개를 선택
    language = ['Python', 'Java', 'C', 'Go', 'PHP']
    selected_lang = st.selectbox('선호하는 언어를 선택!', language)
    if selected_lang == 'Python':
        st.text('파이썬이 최고지')
    elif selected_lang == 'Java':
        st.text('자바 어렵지')
    
    # 데이터 프레임의 컬럼이름을 보여주고,
    # 유저가 컬럼을 선택하면
    # 해당 컬럼만 데이터프레임을 보여주고 싶다.
    columns_list = st.multiselect('컬럼을 선택하세요', df.columns) # 리스트로 리턴, 누른 순서대로 나옴.
    st.dataframe(df[columns_list]) # 리스트를 바로 넣어도 작동함.

    age = st.slider('나이', min_value=30, max_value=110, step=1, value=50) # min_value= 안 넣고 숫자만 바로 넣어도 됨.
    # step은 움직이는 간격, value는 기본값
    st.text(f'나이는 {age}입니다.')
    
    # 확장하는거
    with st.expander('hello'):
        st.text('안녕하세요')

if __name__ == '__main__':
    main()
