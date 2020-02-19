/**
 * Module Utils
 * @author Siderlan Santos
 */


/**
 * Retrive the day name by day number.
 * 
 * @param {number} dayNumber An integer number from 0 to 6.
 */
const getDayName = (dayNumber) => {
  if (!/[0-6]/.test(dayNumber.toString())) {
    throw new Error('Invalid day number. The day number should be in [0-6].');
  }

  const dayNames = 'Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday'.split(',');
  return dayNames[dayNumber];
}

module.exports = {
  getDayName
}