class Stats:
    """
    Инициализация статов
    """
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('topScore.txt', 'r') as ver:
            self.top_score = int(ver.readline())

    def reset_stats(self):
        """
        Сброс статов
        :return:
        """
        self.ship_hp = 2
        self.score = 0
