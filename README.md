# Phase vocoder using Fourier transform

Completed by: `Grudinin Mikhail Artemovich (Грудинин Михаил Артемович)`

## Start a project
Before use you need the `numpy`, `matplotlib` and `scipy` libraries.
In order to run the project, you need to run the following commands:
1.  ```cd phaseVocoder```
2.  If necessary for Unix-like systems: ```chmod +x run.sh```
3.  ```./run.sh <input.wav> <output.wav> <time_stretch_ratio> ```

    Example of speeding up the audio recording test_mono.wav by 2 times:
    ```
    ./run.sh examples/test_mono.wav examples/test_mono_r2.wav 2
    ```

## Task condition:
Требуется реализовать алгоритм pitch-shifter по ссылке в статье: http://www.guitarpitchshifter.com/algorithm.html
Алгоритм предназначен для изменения цифрового аудио-сигнала без изменения питча.
Язык реализации: Python или C++.
При помощи реализованного алгоритма необходимо ускорить растянуть в 2 раза и сжать в 2 раза (по отношению к исходному) прилагаемую аудиозапись.
При реализации алгоритма используйте библиотечные функции для чтения wav-файлов, прямого и обратного преобразования.

Пример входных данных лежит по ссылке: https://cloud.mail.ru/public/Fmgg/873MiULKM

В качестве решения нужно прислать архив phaseVocoder.zip (размещенный аналогично в cloud.mail.ru), внутри которого папка phaseVocoder, в которой размещен bash-script run.sh, который запускает решение задания. Помимо этого в папке могут быть любые файлы, необходимые Вам для решения задачи, не противоречат условию (например, .py, .cpp, мейкфайлы и тд).

Кроме кода необходимо приложить результаты работы программы для тестового файла в виде: test_mono_r05.wav (сжатый в 2 раза), test_mono_r2.wav (растянутый в 2 раза test_mono.wav).

Проверка будет проходить следующим образом:
```cd phaseVocoder && ./run.sh <input.wav> <output.wav> <time_stretch_ratio>```
где:
- <input.wav> -- путь для исходного файла,
- <output.wav> -- путь до файла, который будет результатом работы программы,
- <time_stretch_ratio> -- параметр алгоритма (r < 1 - сжимаем, 1 <= r - растягиваем).
