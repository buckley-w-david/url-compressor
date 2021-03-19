import os
from url_compressor import create_app

port = int(os.getenv("PORT", 5000))
environment = os.getenv("URL_COMPRESSOR_ENV", "development")
app = create_app(environment)

if __name__ == "__main__":
    app.run(port=port)
