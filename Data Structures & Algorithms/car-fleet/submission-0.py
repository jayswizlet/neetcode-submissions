class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #How many units away for each i-th car moving at their respective speed
        #i.e. Position 1 moving at 3 speed -> 3 units away
        #Likewise, Position 4 moving at 2 speed -> 3 units away
        #We could update it every iteration?

        currFleet = []
        unitsAway = []
        pair = []
        for index, pos in enumerate(position):
            pair.append([pos, speed[index]])

        sortedPair = sorted(pair, reverse=True)
        for sortedPos, sortedSpd in sortedPair:
            units = target - sortedPos
            away = units / sortedSpd
            unitsAway.append(away)
        
        while unitsAway:
            idx = 0
            awayFront = unitsAway.pop(0)
            if not currFleet:
                currFleet.append(awayFront)
            if currFleet[-1] < awayFront:
                currFleet.append(awayFront)
            idx += 1

        return len(currFleet)

            # units = target - pos
            # away = units / speed[index]
            # unitsAway.append(away)


