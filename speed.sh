export Y=2024
export TIMEFORMAT='Time: %3R seconds'
cd ~/advent-of-code/aoc-$Y
for i in $(seq -f '%02g' 1 25)
do aocd $Y $i > Day-$i/$i.in
done
for i in $(seq -f '%02g' 1 25)
do echo "Day $i:" && time python Day-$i/Python/main.py < Day-$i/$i.in && echo
done