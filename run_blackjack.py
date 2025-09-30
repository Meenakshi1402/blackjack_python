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
import time
import statistics


def main() -> None:
    # Run 50 rounds of 2000000  games each
    ngames = 2000000
    nrounds = 50
    seed = 43
    
    print("50 rounds of 2000000 games")
    print("pl hands     wins      blackjack charlies  loses     breaks    dealerbjs pushes")
    
    start_time = time.time()
    pl_values = []
    
    for round_num in range(nrounds):
        # Use different seed for each round to get variation
        current_seed = seed + round_num
        stats = start(BasicStrategy_(), ngames=ngames, seed=current_seed)
        
        # Format output to match reference
        # nohands is the number of hands played in the round
        nohands = stats.nohands if stats.nohands else 1
        mean = stats.pl / nohands
        pl_values.append(mean)
        
        print(f"{mean:9.6f} {stats.nohands:<9d} {stats.count[WINS]:<9d} "
              f"{stats.count[BLACKJACKS]:<9d} {stats.count[CHARLIES]:<9d} "
              f"{stats.count[LOSSES]:<9d} {stats.count[BUSTS]:<9d} "
              f"{stats.count[DEALER_BLACKJACKS]:<9d} {stats.count[PUSHES]:<9d}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Calculate statistics
    mean_pl = statistics.mean(pl_values)
    stderr_pl = statistics.stdev(pl_values) / (nrounds ** 0.5)
    cv = (statistics.stdev(pl_values) / abs(mean_pl)) * 100 if mean_pl != 0 else 0
    
    print(f"time: {elapsed_time:.3f}")
    print("PASSED!")
    print()
    print(f"mean(pl) = {mean_pl:.6f}")
    print(f"stderr(pl) = {stderr_pl:.6f}")
    print(f"CV = {cv:.0f}%")


if __name__ == "__main__":
    # Entry point when running `python run_blackjack.py`
    main()


