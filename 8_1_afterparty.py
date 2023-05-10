import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

from textwrap import wrap

if __name__ == "__main__": 

    with open('7_config.txt') as file:
        settings=[float(i) for i in file.read().split('\n')]

    data_v  = np.loadtxt('7_data.txt', dtype=int) * settings[0]

    delta_t = 1 / settings[1]
    data_t  = np.array([i*delta_t for i in range(data_v.size)])

    fig, plot = plt.subplots(figsize=(10, 8), dpi=500)

    plot.axis([data_v.min(), data_t.max(), data_v.min(), data_v.max()+0.2])
    
    plot.plot(data_t, data_v, c='black', linewidth=2, label = 'V(t)')
    
    skip_amnt = 200
    plot.scatter(data_t[0:data_v.size:skip_amnt], data_v[0:data_v.size:skip_amnt], marker = 'o', c = 'green', s=100)

    plot.xaxis.set_major_locator(tck.MultipleLocator(2))
    plot.xaxis.set_minor_locator(tck.MultipleLocator(0.5))

    plot.yaxis.set_major_locator(tck.MultipleLocator(0.5))
    plot.yaxis.set_minor_locator(tck.MultipleLocator(0.1))


    plot.set_title("\n".join(wrap('Процесс заряжания/разряжания конденсатора в RC цепи', 60)), loc = 'center')

    plot.set_ylabel("Напряжение, В")
    plot.set_xlabel("Время, с")

    # plot.legend(shadow = False, loc = 'right', fontsize = 30)

    fig.savefig('8_result.png')
    fig.savefig('8_result.svg')

    print(data_v)
    print(data_t)

    exit()


# from matplotlib import pyplot
# import numpy
# from textwrap import wrap
# 


#считываем показания компаратора и переводим через шаг квантования в вольиты
#массив времен, создаваемый черед количество измерений и известный шаг по времени
#параметры фигуры
fig, plot=pyplot.subplots(figsize=(16, 10), dpi=500)

#минимальные и максимальные значения для осей
plot.axis([data_v.min(), data_t.max()+1, data_v.min(), data_v.max()+0.2])

#  Устанавливаем интервал основных делений:
plot.xaxis.set_major_locator(ticker.MultipleLocator(2))
#  Устанавливаем интервал вспомогательных делений:
plot.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

#  Тоже самое проделываем с делениями на оси "y":
plot.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
plot.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#название графика с условием для переноса строки и центрированием
plot.set_title("\n".join(wrap('процесс заряда и разряда конденсатора в RC цепи', 60)), loc = 'center')

#сетка основная и второстепенная
plot.grid(which='major', color = 'k')
plot.minorticks_on()
plot.grid(which='minor', color = 'gray', linestyle = ':')

#подпись осей
plot.set_ylabel("напряжение, В")
plot.set_xlabel("время, с")

#линия с легендой
plot.plot(data_t, data_v, c='black', linewidth=1, label = 'V(t)')
plot.scatter(data_t[0:data_v.size:20], data_v[0:data_v.size:20], marker = 's', c = 'blue', s=10)

plot.legend(shadow = False, loc = 'right', fontsize = 30)

#сохранение
fig.savefig('graph.png')
fig.savefig('graph.svg')

