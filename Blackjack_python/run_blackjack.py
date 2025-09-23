from Blackjack_python.strategy import BasicStrategy_
from Blackjack_python.game import (
    start,
    WINS,
    BLACKJACKS,
    CHARLIES,
    LOSSES,
    BUSTS,
    DEALER_BLACKJACKS,
    PUSHES,
)


def main() -> None:
    ngames = 1000
    seed = 42

    stats = start(BasicStrategy_(), ngames=ngames, seed=seed)

    nohands = stats.nohands if stats.nohands else 1
    mean = stats.pl / nohands
    print(
        f"{mean:9.6f} {stats.nohands:<9d} {stats.count[WINS]:<9d} "
        f"{stats.count[BLACKJACKS]:<9d} {stats.count[CHARLIES]:<9d} "
        f"{stats.count[LOSSES]:<9d} {stats.count[BUSTS]:<9d} "
        f"{stats.count[DEALER_BLACKJACKS]:<9d} {stats.count[PUSHES]:<9d}"
    )


if __name__ == "__main__":
    main()

from Blackjack_python.strategy import BasicStrategy_
from Blackjack_python.game import (
    start,
    WINS,
    BLACKJACKS,
    CHARLIES,
    LOSSES,
    BUSTS,
    DEALER_BLACKJACKS,
    PUSHES,
)


def main() -> None:
    ngames = 1000
    seed = 42

    stats = start(BasicStrategy_(), ngames=ngames, seed=seed)

    # Match the C++ printf layout:
    # mean, nohands, WINS, BLACKJACKS, CHARLIES, LOSSES, BUSTS, DEALER_BLACKJACKS, PUSHES
    nohands = stats.nohands if stats.nohands else 1
    mean = stats.pl / nohands
    print(
        f"{mean:9.6f} {stats.nohands:<9d} {stats.count[WINS]:<9d} "
        f"{stats.count[BLACKJACKS]:<9d} {stats.count[CHARLIES]:<9d} "
        f"{stats.count[LOSSES]:<9d} {stats.count[BUSTS]:<9d} "
        f"{stats.count[DEALER_BLACKJACKS]:<9d} {stats.count[PUSHES]:<9d}"
    )


if __name__ == "__main__":
    main()


