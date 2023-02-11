from decouple import config


URL_TO_DB = f"mysql+{config('DRIVER')}:" \
            f"//{config('USER')}:" \
            f"@{config('ADDRESS')}:" \
            f"{config('PORT', cast=int)}/" \
            f"{config('DATABASE')}"
