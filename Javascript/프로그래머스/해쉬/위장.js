const solution = (clothes) => {
  let combi = 1;
  const clothMap = {};

  clothes.forEach(([cloth, type]) => {
    clothMap[type] = clothMap[type] ? clothMap[type] : [];
    clothMap[type].push(cloth);
  });

  Object.values(clothMap).map(
    (clothes) => (combi = combi * (clothes.length + 1))
  );

  return combi - 1;
};
