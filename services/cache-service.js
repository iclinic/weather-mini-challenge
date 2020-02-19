const NodeCache = require('node-cache');

/**
 * CacheService Class
 * 
 * @author Siderlan Santos
 * @use NodeCache
 * 
 * @since 1.0.0
 */
class CacheService {
  /**
   * Creates an instance of CacheService
   * 
   * @param {number} ttlSeconds The cache TTL in seconds.
   */
  constructor(ttlSeconds) {
    this.cache = new NodeCache({ stdTTL: ttlSeconds, checkperiod: ttlSeconds * 0.2 });
  }

  /**
   * Retrieve data from the cache if it exists.
   * If data does not exists or it's expired
   * new data will be requested calling the callback
   * function on resolve the new data will be stored on the cache.
   * 
   * @param {string} key The cache identifier.
   * @param {Function} callback The function that will retrieve new data.
   */
  get(key, callback) {
    const value = this.cache.get(key);

    if (value) {
      return Promise.resolve(value);
    }

    return callback().then((result) => {
      this.cache.set(key, result);
      return result;
    });
  }

  /**
   * Remove data from the cache by a key.
   * @param {string} key The cache identifier.
   */
  remove(key) {
    this.cache.del(key);
  }

  /**
   * Flush all the cache.
   */
  flush() {
    this.cache.flushAll();
  }
}

module.exports = CacheService;