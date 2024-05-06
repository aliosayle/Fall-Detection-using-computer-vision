import time

last_call_time = 0

def call_with_cooldown(cooldown_time = 5):
    global last_call_time
    current_time = time.time()
    if current_time - last_call_time >= cooldown_time:
        last_call_time = current_time
        print("true")
        return True
    else:
        print("false")
        return False

# Example usage:
cooldown_time = 5  # Cooldown time of 5 seconds

print(call_with_cooldown(cooldown_time))  # First call, returns True
time.sleep(3)  # Simulate some time passing
print(call_with_cooldown(cooldown_time))  # Second call within cooldown time, returns False
time.sleep(3)  # Simulate more time passing
print(call_with_cooldown(cooldown_time))  # Third call after cooldown time, returns True
call_with_cooldown()
call_with_cooldown()
time.sleep(5)
call_with_cooldown()