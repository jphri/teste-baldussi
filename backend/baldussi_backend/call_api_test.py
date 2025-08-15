import baldussi_backend.call_api

def call_api_calls_raw_test():
    call_api.calls_raw()

def call_api_calls_test():
    call_api.calls()

def call_api_health_test():
    call_api.health()

if __name__ == "__main__":
    call_api_health_test()
    call_api_calls_test()
    call_api_calls_raw_test()
