import streamlit as st
from prd import generate
from datetime import date

st.title("📄 PRD Generator")
title = st.text_input("Название", "Новый онбординг")
problem = st.text_area("Проблема", "Пользователи не понимают ценность продукта")
audience = st.text_area("Аудитория", "Новые B2C-пользователи")
goals = st.text_area("Цели/метрики", "Retention D7: +10%")
features = st.text_area("Требования", "- [ ] Шаг 1\n- [ ] Шаг 2")

md = generate(title=title, problem=problem, audience=audience,
              goals=goals, features=features, date=str(date.today()))
st.markdown(md)
st.download_button("Скачать PRD.md", md, file_name="PRD.md")
