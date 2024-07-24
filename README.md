# Описание
Данный алгоритм решает поставленную задачу путём перебора возможных комбинаций полей для получения кратчайшего ключа. 
Для оптимизации используются следующие техники:
1. Упорядочивание набора ключей по длинне
   При простом комбинаторном переборе наборов ключей их чесло будет часто и немонотонно варьироваться, что может привести к проверке субоптимальных комбинаций ключей. Для решения этой проблемы в коде порядок проверки наборов учитывает их размер  —  это позволяет завершить программу сразу при нахождении оптимальной комбинации
2. Анализ плотности
   Если рассматривать ключи, как оси системы координат, а множество записей, как множество точек  —  наборы значений по ключу становятся проекциями точек на соответствующие оси. Различные проекции называются кластерами, большее их количество указывает на высокий потенциал ключа: вероятно, ключ, по которому почти нет совпадений (количество кластеров близко к количеству точек) надо дополнить совсем чуть-чуть, а ключ двумя кластерами, один из которых соответствует единственной точке, сможет различить только пару исходных точек.
# Схема
! [scheme][image]

[scheme]: https://github.com/TNBul/2024Garpix/blob/main/diagram.json
[image]: https://github.com/TNBul/2024Garpix/blob/main/diagram.png
