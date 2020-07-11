#!/bin/bash
 
# > /dev/null - Означает подавление вывода, этой командой я подавляю все потоки данных
echo "Wait 10 sec ..."
tar -xvf mvcRussia.tar.xz > /dev/null
pip3 install pandas > /dev/null
pip3 install streamlit > /dev/null
streamlit run mvcRussia.py # Решил не подавлять вывод этой команды, поскольку пользователю стоит знать, запустилось ли приложение в браузере или нет