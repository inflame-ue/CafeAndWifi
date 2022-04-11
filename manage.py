# imports
from cafes import create_app, db
from flask_migrate import Migrate
import os
import dotenv

# load the dotenv file
dotenv.load_dotenv("C://EnvironmentalVariables//.env")

# init the app
app = create_app(os.environ.get("FLASK_CONFIG") or "default")

# init the extensions
migrate = Migrate(app=app, db=db)

# run config
if __name__ == "__main__":
    app.run()
