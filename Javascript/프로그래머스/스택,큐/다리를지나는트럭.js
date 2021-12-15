function solution(bridge_length, weight, truck_weights) {
  let ans = 0;
  let onBridgeWeight = 0;
  let arrivedTruck = 0;
  let onBridgeTruck = [];
  const truckNum = truck_weights.length;

  while (arrivedTruck < truckNum) {
    const frontTruck = truck_weights[0];
    ans += 1;

    onBridgeTruck = onBridgeTruck
      .map((x) => {
        x.time -= 1;
        return x;
      })
      .filter((x) => {
        if (x.time === 0) {
          arrivedTruck += 1;
          onBridgeWeight -= x.weight;
          return false;
        }
        return true;
      });

    if (onBridgeWeight + frontTruck <= weight) {
      onBridgeWeight += frontTruck;
      onBridgeTruck.push({ weight: frontTruck, time: bridge_length });
      truck_weights.shift();
    }
  }
  return ans;
}
