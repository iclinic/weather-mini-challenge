const Utils = require('../index');

it('Returns the name of the day based on its number', () => {
  const day = Utils.getDayName(2);
  expect(day).toBe('Tuesday');
})

it('Throw an error on invalid day number', () => {
  const day = Utils.getDayName(-1);
  expect(Utils.getDayName).toThrow();
})