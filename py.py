import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxc8e792abe62b4e0a8807ae40829d329e.mailgun.org/messages",
        auth=("api", "key-e2c43c98f6a756838662b39bf3c93253"),
        data={"from": "Notas Tecnico <notas@tecnico.ulisboa.pt>",
              "to": "Manuel <manuelsousamvs@gmail.com>",
              "subject": "Hello Manuel",
              "text": "Congratulations Manuel, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})


send_simple_message()