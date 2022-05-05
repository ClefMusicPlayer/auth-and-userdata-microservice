from app import app
from runconfig import DevConfig, ProdCofig

if __name__ == '__main__':
    app.config.from_object(DevConfig)
    app.run()