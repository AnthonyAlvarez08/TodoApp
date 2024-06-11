from configparser import ConfigParser


# define the port and host just incase I change it in the future, for now localhost 5000
HOST = '127.0.0.1'
PORT = 5000
SECRET_KEY = 'fdasf'

config_file = 'AppConfig.ini'

configur = ConfigParser()
configur.read(config_file)
SECRET_KEY = configur.get('Secrets', 'secret_key')

EndPoint = configur.get('Database', 'endpoint')
PortNum = configur.get('Database', 'port_number')
Username = configur.get('Database', 'user_name')
dbPass = configur.get('Database', 'user_pwd')
dbName = configur.get('Database', 'db_name')
RegionName = configur.get('Database', 'region_name')