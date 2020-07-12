# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mvcRussia.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dsandshr <dsandshr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/07/11 01:16:58 by dsandshr          #+#    #+#              #
#    Updated: 2020/07/12 12:14:57 by dsandshr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import streamlit as st
import pandas as pd

DATA_URL = (r"./mvcRussia.csv") # Адресс файла

st.title("Motor Vehicle Collisions in Russia 2016-2018") # Создание тайтла
st.markdown("This application is a Streamlit dashboard that can be to analyze motor vehicle colision in Russia 2016-2018") # Приписка


@st.cache(allow_output_mutation=True) # Этими строчками даем понять Streamlit'у, что мы не боимся изменений data
def load_data(nrows): # Функция загрузки нужной информации с возможностью выбора колличества обработки строк
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['crash_date', 'crash_time']])
    data.dropna(subset=['latitude', 'longitude'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data

data = load_data(322518)


st.header("How many collisions occur during a given year?")
year = st.slider("Year to look at", 2016, 2018) # Слайдер времени     Этот блок кода отвечает за выбор года
data['years'] = data['date/time'].dt.year 

st.header("Where are the most peaople injured in Russia?") # Этот блок кода отвечает за выбор колличества пострадавших людей
injured_people = st.slider("Number of persons injured  in vehicle colisions", 1, 20) # Слайдер от 1 до 20 где числа означают поврежденных в аварии людей

st.map(data.query("years == @year and participants_amount >= @injured_people")[['latitude', 'longitude']].dropna(how='any')) # Вывод карты на которую влияют несколько ползунков


if  st.checkbox("Show Raw Dtata", False):    # Блок кода отвечающий за чекбокс(галочку) вывода всей информации 
    st.subheader('Raw Data') # Правда из-за большого колличества информации этот блок кода не срабатывает, если поменять колличество строк в load_data то все сработает
    st.write(data)


st.markdown("by **Ilya Andrushkevich**")
st.markdown('**Github** https://github.com/dsandshr')