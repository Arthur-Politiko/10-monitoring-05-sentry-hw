import sentry_sdk

sentry_sdk.init(
    dsn="https://ce7a5dce2f3f993666f0799910ba0657@o4511052853018624.ingest.de.sentry.io/4511064010719312",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

if __name__ == "__main__":
    division_by_zero = 1 / 0
    print(division_by_zero)