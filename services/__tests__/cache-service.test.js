const NodeCache = require('node-cache')
const CacheService = require('../cache-service')

jest.mock('node-cache');

beforeEach(() => {
  NodeCache.mockClear();
})

it('uses a NodeCache to store the cache', () => {
  const stdTTL = 500;
  const checkperiod = stdTTL * 0.2;

  const cacheService = new CacheService(stdTTL);

  expect(NodeCache).toHaveBeenCalledWith({ stdTTL, checkperiod });
  expect(NodeCache).toHaveBeenCalledTimes(1);
})

it('Execute callback function and store on cache if cache is invalid', async () => {
  const data = 'my-data';
  const key = 'cache-key';

  const callback = function() {
    return Promise.resolve(data);
  };

  const cacheService = new CacheService(5000);
  const noCachedData = await cacheService.get(key, callback);

  expect(noCachedData).toBe(data);

  const [ mockNodeCacheInstance ] = NodeCache.mock.instances;
  const mockNodeCacheGet = mockNodeCacheInstance.get;
  const mockNodeCacheSet = mockNodeCacheInstance.set;

  expect(mockNodeCacheGet).toHaveBeenCalledTimes(1);
  expect(mockNodeCacheGet).toHaveReturnedWith(undefined);
  expect(mockNodeCacheSet).toHaveBeenCalledTimes(1);
})

it('Removes from the cache by a key', () => {
  const cacheService = new CacheService(500);
  
  const key = 'cache-key'
  cacheService.remove(key);

  const [ mockNodeCacheInstance ] = NodeCache.mock.instances;
  const mockNodeCacheDel = mockNodeCacheInstance.del;

  expect(mockNodeCacheDel).toHaveBeenCalledWith(key);
  expect(mockNodeCacheDel).toHaveBeenCalledTimes(1);
})

it('Flush all cache', () => {
  const cacheService = new CacheService(500);
  
  cacheService.flush();

  const [ mockNodeCacheInstance ] = NodeCache.mock.instances;
  const mockNodecacheFlush = mockNodeCacheInstance.flushAll;

  expect(mockNodecacheFlush).toHaveBeenCalledTimes(1);
})
