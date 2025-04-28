from setuptools import setup, find_packages

setup(
    name='banking_chatbot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'llama_index',
    ],
    entry_points={
        'console_scripts': [
            'banking-chatbot=app.streamlit_app:main'
        ],
    },
)
