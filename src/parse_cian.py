""" Парсер ЦИАН
https://github.com/lenarsaitov/cianparser
"""

import datetime

import cianparser
import pandas as pd

moscow_parser = cianparser.CianParser(location="Москва")

def main():
    t = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    for n_rooms in range(1, 4):
        csv_path = f'data/raw/{n_rooms}_{t}.csv'
        data = moscow_parser.get_flats(
            deal_type="sale",
            rooms=(n_rooms,),
            with_saving_csv=False,
            additional_settings={
                "start_page": 1,
                "end_page": 10,
                "object_type": "secondary"
            })
        df = pd.DataFrame(data).iloc[:50, :]

        df.to_csv(csv_path,
                encoding='utf-8',
                index=False)


if __name__ == '__main__':
    main()
