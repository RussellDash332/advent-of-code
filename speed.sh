export Y=2023
export TIMEFORMAT='Time: %3R seconds'
cd ~/advent-of-code/aoc-$Y
for i in $(seq -f '%02g' 1 25)
do echo "Day $i:" && aocd $Y $i > Day-$i/$i.in && time python Day-$i/Python/main.py < Day-$i/$i.in && echo
done