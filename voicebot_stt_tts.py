import streamlit as st

def main():

    # set_page_config : 타이틀 세팅
    st.set_page_config(page_title='음성 챗봇', layout='wide')
    st.header('음성 챗봇 프로그램')
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

# 함수를 해당 파일 내에서만 사용할 수 있게 만드는 코드
if __name__ == '__main__':
    main()