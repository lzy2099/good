@asyncio.coroutine
def create_pool(loop, **kw):
	logging.info('create database connection pool...')
	global __pool
	__pool = yield from aiomysql.create_pool(
		host=kw.get('host', 'localhost'),
		port=kw.get('port, 3306'),
		user=kw.['user'],
		password=kw['password'],
		db=kw['db'],
		charset=kw.get('chartset', 'utf8'),
		autocommit=kw.get('autocommit', true),
		maxsize=kw.get('maxsize',10),
		minsize=kw.get('minsize',1),
		loop=loop
	)


