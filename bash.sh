# flask
# nohup python -u /home/reed/pabd24/src/predict_app.py > /home/reed/pabd24/flask.log 2>&1 &

# gunicorn
gunicorn -b 0.0.0.0 -w 1 src.predict_app:app --daemon --access-logfile /home/reed/pabd24/gunicorn.log --capture-output