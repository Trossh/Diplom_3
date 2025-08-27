class Config:
    BASE_URL = "https://stellarburgers.nomoreparties.site"
    LOGIN_URL = f"{BASE_URL}/login"
    REGISTER_URL = f"{BASE_URL}/register"
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_URL = f"{BASE_URL}/reset-password"
    PROFILE_URL = f"{BASE_URL}/account/profile"
    ORDER_HISTORY_URL = f"{BASE_URL}/account/order-history"
    ORDER_FEED_URL = f"{BASE_URL}/feed"