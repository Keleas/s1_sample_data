# External searching

## Формат обучающей выборки

К каждому изображению приложен файл в формате txt, где в каждой строке записана аннотация месторасположения объекта разметки.
Таким образом получается следующая структура обучающей выборки:
```
root
├──labels (папка)
├  ├── 1.txt
├  ├── 2.txt
├  └── n.txt
├──images (папка)
├  ├── 1.jpg
├  ├── 2.jpg
├  └── n.jpg
```
Пример структура обучающей выборки приведен в папке [```train_dataset_example/```](train_dataset_example/).

Если файл с разметкой пустой, то на изображении отсутствуют объекты разметки.
Каждая непустая строка с разметкой имеет следующий порядок: ```label```, ```xc```, ```yc```, ```w```, ```h```, где: 
- ```label``` - код класса объекта, 
- ```xc``` - х координата центра ограничивающего прямоугольника, 
- ```yc``` - у координата центра ограничивающего прямоугольника, 
- ```w``` - ширина ограничивающего прямоугольника, 
- ```h``` - высота ограничивающего прямоугольника.

Код класса объекта -- порядковый номер класса в нотации приведенной в файле [```classes.txt```](train_dataset_example/classes.txt)

## Докер-контейнер для Площадки

Пример корректного образа докер-контейнера приведен в файле [```Dockerfile```](docker_sample/Dockerfile) в папке
[```docker_sample```](docker_sample/).

Исходные файлы дя предсказания (изображения из валидационной выборки) будут расположены в имени окружения ```DATA_ROOT_PATH```.
Результатом запуска докер-контейнера должен быть созданный файл ```submission.csv``` в корне рабочего окружения контейнера.

### Формат выходных данных

Выходной файл должен иметь имя ```submission.csv``` и иметь следующую структуру:
- каждая строка таблицы содержит описание предсказания для одного объекта
- таблица имеет следующие поля
  - ```image_id``` - наименование файла изображения без расширения,
  - ```xmin``` - х координата правого верхнего угла ограничивающего прямоугольника,
  - ```ymin``` - у координата правого верхнего угла ограничивающего прямоугольника,
  - ```xmax``` - х координата левого нижнего угла ограничивающего прямоугольника,
  - ```ymax``` - у координата левого нижнего угла ограничивающего прямоугольника,
  - ```label``` - код класса объекта,
  - ```score``` - вероятность предсказания.

Пример такого файла для тестовых изображений приведен в [```sample_submission.csv```](sample_submission.csv).

## Метрика оценки решения

В качестве метрики для оценки качества решения задачи поиска используется mean Average Precision (mAP). Значение метрики
лежит в диапазоне от 0 до 1. Чем значение mAP выше к 1, тем точнее предсказание совпадает с истинным значением разметки.

Особенностью реализации метрики является то, что в случае если в разметке и в предсказании отсутствуют объекты поиска, то 
значение метрики ```mAP = 1.0```.

Реализация метрики оценки решения приведена в файле [```metrics.py```](metrics.py).

## Лицензии

Лицензированный в соответствии [MIT license](http://opensource.org/licenses/MIT).
