import pandas as pd

EPL_CSV_FILE = "league/data/epl_standings_2000-2022.csv"


class Table:
    def __init__(self):
        self.table = pd.read_csv(EPL_CSV_FILE)
        self.get_seasons()

    def get_seasons(self):
        seasons = list(self.table["Season"])
        seasons_slash = []
        for season in seasons:
            splits = season.split("-")
            year1 = splits[0]
            year2 = f'{year1[0:2]}{splits[1]}'
            seasons_slash.append(f'{year1}/{year2}')
        self.table["Season"] = seasons_slash

    def select_season(self, season):
        """
        Select a season and find results
        """
        return self.table[self.table["Season"] == season]


if __name__ == "__main__":
    table_inst = Table()
    print(table_inst)
    print(table_inst.select_season("2009/2010"))
