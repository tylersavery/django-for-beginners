from .environment import ENV


SECRET_KEY = ENV.str("SECRET_KEY")
