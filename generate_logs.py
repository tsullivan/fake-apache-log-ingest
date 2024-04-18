import json
import random
import time
from faker import Faker

def generate_log_entry():
    fake = Faker()
    log_entry = {}
    log_entry["host"] = fake.ipv4()
    log_entry["user_identifier"] = fake.user_name()
    log_entry["datetime"] = fake.date_time_this_year().isoformat()
    log_entry["method"] = random.choice(["GET", "POST", "PUT", "DELETE"])
    log_entry["request"] = fake.uri()
    log_entry["referer"] = fake.uri()
    log_entry["status"] = random.choice([200, 404, 500, 301])
    log_entry["bytes"] = random.randint(1, 5000)
    log_entry["user_agent"] = fake.user_agent();
    log_entry["message"] = fake.paragraph();
    return log_entry

if __name__ == "__main__":
    while True:
        log_entry = generate_log_entry()
        print(json.dumps(log_entry))
        time.sleep(0.1)  # pause for a tenth of a second
