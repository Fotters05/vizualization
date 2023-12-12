#Цель: на данной практической работе необходимо использовать датасет с прошлой практической работы
#и визуализировать данные в виде графиков.

import pandas as pd
import matplotlib.pyplot as plt

netflix = pd.read_csv("netflix_titles.csv")
print(netflix)

#Сначала был создан линейный график с продолжительностью фильмов.

# plt.plot(netflix.index[:20], netflix["duration"].head(20), color="pink", label="Продолжительность")
# plt.xlabel ('Index')
# plt.ylabel("Продолжительность")
# plt.title('Продолжительность')
# plt.grid()
# plt.show()


#Затем был создан линейный график с годом релиза фильмов.

# plt.plot(netflix.index[:20], netflix["release_year"].head(20), color="blue", label="Год релиза")
# plt.xlabel ('Index')
# plt.ylabel("Год")
# plt.title('Год релиза')
# plt.grid()
# plt.show()


#После чего был создан линейный график который показывает, где идет фильм.

# plt.plot(netflix.index[:20], netflix["type"].head(20), color="purple", label="Тип")
# plt.xlabel ('Index')
# plt.ylabel("Тип")
# plt.title('Тип фильма')
# plt.grid()
# plt.show()

#Далее был создан столбчатый график который показывает, дату добавления фильма.

# plt.bar(netflix.index[:20], netflix["date_added"].head(20), color="black", label="Дата добавления")
# plt.xlabel('Index')
# plt.ylabel('Дата')
# plt.title('Дата добавления')
# plt.legend()
# plt.show()

#Затем был создан столбчатый график, показывающий продолжительность.

# plt.bar(netflix.index[:20], netflix["duration"].head(20), color="green", label="Продолжительность")
# plt.xlabel('Index')
# plt.ylabel('Продолжительность')
# plt.title('Продолжительность')
# plt.legend()
# plt.show()

#После чего, был создан столбчатый график, показывающий, где идет фильм.

# plt.bar(netflix.index[:20], netflix["type"].head(20), color="yellow", label="Тип")
# plt.xlabel('Index')
# plt.ylabel('Тип')
# plt.title('Тип фильма')
# plt.legend()
# plt.show()

#Затем была создана диаграмма, которая показывает страну производителя.

# data = netflix["country"].value_counts().head()
# plt.pie(data, labels = data.index, colors = ["blue", "red"],autopct="%1.1f%%")
# plt.legend()
# plt.show()

#Далее была создана круговая диаграмма, указывающая жанр.

# data = netflix["listed_in"].value_counts().head()
# plt.pie(data, labels = data.index, colors = ["blue", "red"],autopct="%1.1f%%")
# plt.legend()
# plt.show()

#После чего, был создан график рассеивания, который показывает, где показывали тот или иной жанр.

# plt.scatter(netflix["type"].head(20), netflix["listed_in"].head(20))
# plt.show()

#Потом был создан график рассеивания, который показывает продолжительность фильмов в том или ином году.

# plt.scatter(netflix["release_year"].tail(20), netflix["duration"].tail(20))
# plt.show()

#Была представлена гистограмма, показывающая год релиза.

# plt.hist(netflix["release_year"].head(20), bins=30, edgecolor="black")
# plt.legend()
# plt.show()

#Была представлена гистограмма, показывающая тип.

# plt.hist(netflix["type"].head(20), bins=30, edgecolor="black")
# plt.legend()
# plt.show()

#Была представлена гистограмма, показывающая время воспроизведения фильмвов.


# plt.hist(netflix["duration"].head(20), bins=30, edgecolor="black")
# plt.legend()
# plt.show()


#Вывод: в данной практической работе использовать датасет с прошлой практической работы
#и визуализировать данные в виде графиков.