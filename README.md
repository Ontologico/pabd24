# Предиктивная аналитика больших данных

Учебный проект для демонстрации основных этапов жизненного цикла проекта предиктивной аналитики.  

## Installation 

### Для Linux установка conda будет выглядеть:
```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

rm -rf Miniconda3-latest-Linux-x86_64.sh
```

### Клонируйте репозиторий, создайте виртуальное окружение, активируйте и установите зависимости:  

```sh
git clone https://github.com/Ontologico/pabd24.git
cd pabd24

conda env create -f environment.yml
conda activate pabd24
```

## Usage

### Запуск приложения flask/gunicorn

```sh
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
