import streamlit as st

def hello ():
    return 'Aprendendo Docker'



def main():
    st.write(hello())
    st.image('docker-27.png', width=100)

if __name__ == '__main__':
    main()