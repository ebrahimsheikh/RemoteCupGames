import conf


if conf.game == 'Simple':
    import Games.Simple.Server.Server as Game
elif conf.game == 'Snake':
    import Games.Snake.Server.Server as Game


def main():
    g = Game.Server()
    g.connect()
    g.run()


if __name__ == "__main__":
    main()
