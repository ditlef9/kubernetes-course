import datetime
import os
import socket

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():

    # Datetime
    now: datetime.datetime = datetime.datetime.now()
    timezone_offset: str = now.strftime("%z")  # +0200
    formatted_timezone: str = f"UTC{timezone_offset[:3]}"  # timezone_offset[:3] gives the "+02" part
    if formatted_timezone == "UTC+00":
        formatted_timezone = "UTC"
    datetime_ymdhms_saying: str = now.strftime("%d.%m.%Y %H:%M:%S") + f" {formatted_timezone}"

    # Hostname
    hostname = socket.gethostname()

    # Return
    data: dict = {
        "datetime_ymdhms_saying": datetime_ymdhms_saying,
        "hostname": hostname
    }

    return {"message": "Hello from backend", "data": data, "error": ""}, 200


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))