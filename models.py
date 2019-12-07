from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class promoter(Base):
	__tablename__ = 'promoter'

	pr_id = Column('pr_id', INTEGER, primary_key=True)
	pr_name = Column('pr_name', TEXT)
	pr_regplace = Column('pr_regplace', TEXT)

	def __str__(self):
		return 'pr_id={pr_id}, pr_name={pr_name}, pr_regplace={pr_regplace},'.format(pr_id=self.pr_id,pr_name=self.pr_name,pr_regplace=self.pr_regplace)

	def __repr__(self):
		return str(self)

	@classmethod
	def get_columns(cls):
		return [promoter.pr_id,promoter.pr_name,promoter.pr_regplace]

	@classmethod
	def create(cls):
		return promoter()

class ad(Base):
	__tablename__ = 'ad'

	ad_id = Column('ad_id', INTEGER, primary_key=True)
	ad_type = Column('ad_type', TEXT)
	ad_name = Column('ad_name', TEXT)
	ad_price = Column('ad_price', NUMERIC(8, 0))
	ad_views = Column('ad_views', BIGINT)
	ad_theme = Column('ad_theme', INTEGER)
	ad_promoter = Column('ad_promoter', INTEGER)
	ad_product = Column('ad_product', INTEGER)
	ad_file = Column('ad_file', TEXT)

	def __str__(self):
		return 'ad_id={ad_id}, ad_type={ad_type}, ad_name={ad_name}, ad_price={ad_price}, ad_views={ad_views}, ad_theme={ad_theme}, ad_promoter={ad_promoter}, ad_product={ad_product}, ad_file={ad_file},'.format(ad_id=self.ad_id,ad_type=self.ad_type,ad_name=self.ad_name,ad_price=self.ad_price,ad_views=self.ad_views,ad_theme=self.ad_theme,ad_promoter=self.ad_promoter,ad_product=self.ad_product,ad_file=self.ad_file)

	def __repr__(self):
		return str(self)

	@classmethod
	def get_columns(cls):
		return [ad.ad_id,ad.ad_type,ad.ad_name,ad.ad_price,ad.ad_views,ad.ad_theme,ad.ad_promoter,ad.ad_product,ad.ad_file]

	@classmethod
	def create(cls):
		return ad()

class theme(Base):
	__tablename__ = 'theme'

	th_id = Column('th_id', INTEGER, primary_key=True)
	th_keyword = Column('th_keyword', TEXT)

	def __str__(self):
		return 'th_id={th_id}, th_keyword={th_keyword},'.format(th_id=self.th_id,th_keyword=self.th_keyword)

	def __repr__(self):
		return str(self)

	@classmethod
	def get_columns(cls):
		return [theme.th_id,theme.th_keyword]

	@classmethod
	def create(cls):
		return theme()

class user(Base):
	__tablename__ = 'user'

	us_id = Column('us_id', INTEGER, primary_key=True)
	us_email = Column('us_email', TEXT)
	us_last_session = Column('us_last_session', INTEGER)

	def __str__(self):
		return 'us_id={us_id}, us_email={us_email}, us_last_session={us_last_session},'.format(us_id=self.us_id,us_email=self.us_email,us_last_session=self.us_last_session)

	def __repr__(self):
		return str(self)

	@classmethod
	def get_columns(cls):
		return [user.us_id,user.us_email,user.us_last_session]

	@classmethod
	def create(cls):
		return user()

class user_theme(Base):
	__tablename__ = 'user_theme'

	us_th_id = Column('us_th_id', INTEGER, primary_key=True)
	us_th_thid = Column('us_th_thid', INTEGER)
	us_th_usid = Column('us_th_usid', INTEGER)

	def __str__(self):
		return 'us_th_id={us_th_id}, us_th_thid={us_th_thid}, us_th_usid={us_th_usid},'.format(us_th_id=self.us_th_id,us_th_thid=self.us_th_thid,us_th_usid=self.us_th_usid)

	def __repr__(self):
		return str(self)

	@classmethod
	def get_columns(cls):
		return [user_theme.us_th_id,user_theme.us_th_thid,user_theme.us_th_usid]

	@classmethod
	def create(cls):
		return user_theme()

class product(Base):
	__tablename__ = 'product'

	prd_id = Column('prd_id', INTEGER, primary_key=True)
	prd_name = Column('prd_name', TEXT)
	prd_keyword = Column('prd_keyword', TEXT)

	def __str__(self):
		return 'prd_id={prd_id}, prd_name={prd_name}, prd_keyword={prd_keyword},'.format(prd_id=self.prd_id,prd_name=self.prd_name,prd_keyword=self.prd_keyword)

	def __repr__(self):
		return str(self)

	@classmethod
	def get_columns(cls):
		return [product.prd_id,product.prd_name,product.prd_keyword]

	@classmethod
	def create(cls):
		return product()

class session(Base):
	__tablename__ = 'session'

	ss_id = Column('ss_id', INTEGER, primary_key=True)
	ss_nickname = Column('ss_nickname', TEXT)
	ss_ip = Column('ss_ip', TEXT)
	ss_start_time = Column('ss_start_time', DATE)
	ss_end_time = Column('ss_end_time', DATE)
	ss_with_adblock = Column('ss_with_adblock', BOOLEAN)

	def __str__(self):
		return 'ss_id={ss_id}, ss_nickname={ss_nickname}, ss_ip={ss_ip}, ss_start_time={ss_start_time}, ss_end_time={ss_end_time}, ss_with_adblock={ss_with_adblock},'.format(ss_id=self.ss_id,ss_nickname=self.ss_nickname,ss_ip=self.ss_ip,ss_start_time=self.ss_start_time,ss_end_time=self.ss_end_time,ss_with_adblock=self.ss_with_adblock)

	def __repr__(self):
		return str(self)

	@classmethod
	def get_columns(cls):
		return [session.ss_id,session.ss_nickname,session.ss_ip,session.ss_start_time,session.ss_end_time,session.ss_with_adblock]

	@classmethod
	def create(cls):
		return session()

