U
    ��#g�  �                   @   sd   d dl Z d dlZd dlZe�d�e _ejd Ze jjj	ded�gdd�Z
ee
d d  d	 d
 � dS )�    N�OPENAI_API_KEY�   �user)�role�contentzgpt-3.5-turbo)�messages�model�choices�messager   )�openai�sys�os�getenv�api_key�argv�user_message�chat�completions�create�response�print� r   r   �\C:\Users\Owner\OneDrive\Desktop\GitHub_OpenAI_Assistant\openai-assistants-api-demo\openai.py�<module>   s   

�