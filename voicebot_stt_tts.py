import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('OPEN_API_KEY')
client = openai.OpenAI(api_key=api_key)

# 메인 함수
def main():

    # 기본설정
    st.set_page_config(page_title='음성 챗봇', layout='wide')

    # 제목
    st.header('음성 챗봇 프로그램')

    # 구분선
    st.markdown('---')

    # expander 만들기
    with st.expander('음성 챗봇 프로그램에 관하여', expanded=True):
        st.write(
        '''
        - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용합니다.
        - STT(Sppech-To-Text)는 OpenAI의 Whisper를 활용합니다.
        - 답변은 OpenAI의 GPT 모델을 활용합니다.
        - TTS(Test-To-Speech)는 OpenAI의 TTS를 활용합니다.
        '''
        )
        st.markdown('')

    # 사이드바 생성
    with st.sidebar:
        model = st.radio(label='GPT 모델', options=["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo"])
        st.markdown('---')

        # 버튼 생성
        if st.button(label='초기화'):
            pass
    
    # 기능 구현 컬럼
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('질문하기')
    
    with col2:
        st.subheader('질문/답변')

# 함수를 해당 파일 내에서만 사용할 수 있게 만드는 코드
if __name__ == '__main__':
    main()