FROM continuumio/miniconda
WORKDIR /app
COPY . .
RUN conda env create -f environment.yml

CMD ["conda", "run", "-n", "pabd24", "gunicorn", "-b", "0.0.0.0", "-w",  "1",  "src.predict_app:app",  "--capture-output"]         
EXPOSE 8000