# -*- coding: utf-8 -*-


from logging import raiseExceptions

end = 0


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.sets = 0


class TennisGame:
    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)

    def won_point(self, playerName):
        if playerName == self.player1.name:
            self.player1.points += 1
        else:
            self.player2.points += 1
        if playerName != self.player1.name or self.player2.name:
            raiseExceptions("Player not existing!")
        if (self.player1.points >= 4 or self.player2.points >= 4) and abs(
            self.player1.points - self.player2.points
        ) >= 2:
            raiseExceptions("Game is over !")

    def won_set(self):
        global end
        if (self.player1.points >= 4 or self.player2.points >= 4) and abs(
            self.player1.points - self.player2.points
        ) >= 2:
            if self.player1.points - self.player2.points == 2:
                self.player1.sets = +1
            elif self.player2.points - self.player1.points == 2:
                self.player2.sets = +1
        while end == 0:
            if (self.player1.sets == 6 or self.player2.sets == 6) and abs(
                self.player1.sets - self.player2.sets
            ) >= 2:
                if self.player1.sets - self.player2.sets == 2:
                    end = 1
                    return self.player1.name + "won ! Congratulations !!!"
                elif self.player2.sets - self.player1.sets == 2:
                    end = 1
                    return self.player2.name + "won ! Congratulations !!!"
            elif self.player1.sets == 7:
                end = 1
                return self.player1.name + "won ! Congratulations !!!"
            elif self.player2.sets == 7:
                end = 1
                return self.player2.name + "won ! Congratulations !!!"

    def reset_game(self):
        global end
        if end == 0:
            raiseExceptions("Game isn't over yet !")
        else:
            end = 0
            print("Restarting a new game !")
            print("What will be the name of the first new player ?")
            name1 = str(input())
            print("What will be the name of the new opponent ?")
            name2 = str(input())
            TennisGame(name1, name2)

    def score(self):
        if (self.player1.points < 4 and self.player2.points < 4) and (
            self.player1.points + self.player2.points < 6
        ):
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            s = points[self.player1.points]
            return (
                s + "-All"
                if (self.player1.points == self.player2.points)
                else s + "-" + points[self.player2.points]
            )
        else:
            if self.player1.points == self.player2.points:
                return "Deuce"
            s = (
                self.player1.name
                if self.player1.points > self.player2.points
                else self.player2.name
            )
            return (
                "Advantage " + s
                if (
                    (self.player1.points - self.player2.points)
                    * (self.player1.points - self.player2.points)
                    == 1
                )
                else "Win for " + s
            )
