# Предиктивная аналитика больших данных
Учебный проект для демонстрации основных этапов жизненного цикла проекта предиктивной аналитики.  

## Установка
### Для Linux установка conda будет выглядеть:
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

rm -rf Miniconda3-latest-Linux-x86_64.sh
```

### Клонируйте репозиторий, создайте виртуальное окружение, активируйте и установите зависимости:  
```bash
git clone https://github.com/Ontologico/pabd24.git
cd pabd24

conda env create -f environment.yml
conda activate pabd24
```

## Настройка терминала для удобства
### Открытие bash сразу с нужным окружением
```bash
# Открываем .bashrc файл в текстовом редакторе
nano ~/.bashrc

# Дописываем в конец файла и сохраняем: 
conda activate pabd24
```
### При работе в VS Code выбираем терминал по умолчанию в настройке:
**Terminal › Integrated › Default Profile: Linux**

## Использование
### Запуск приложения flask/gunicorn
```bash
# flask
python src/predict_app.py

# gunicorn
gunicorn -b 0.0.0.0 -w 1 src.predict_app:app --daemon --access-logfile ./gunicorn.log --capture-output

# или
source bash.sh
```

### Демонстрация
**gunicorn:** http://87.242.101.208:8000/ \
**Токен для авторизации:** pabd24

### Docker
```bash
# flask
docker run ontologico/pabd24:latest

# gunicorn
docker run ontologico/pabd24:gunicorn
```
