from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()


def send_reminder(user, date):

    print(f"🔔 Lembrete para {user}: sua consulta é em {date}")


def schedule_reminders(user, date):

    # para teste vamos disparar lembretes após alguns segundos
    scheduler.add_job(send_reminder, "date", run_date=None, args=[user, date])