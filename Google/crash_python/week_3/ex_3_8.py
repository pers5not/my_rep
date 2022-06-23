# Функция повтора пытается выполнить операцию, которая может завершиться неудачей, она повторяет операцию несколько раз. В настоящее время код будет продолжать выполнять функцию, даже если она будет успешной. Заполните пробел, чтобы код прекратил попытки после успешного выполнения операции.
def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
            break
        else:
            print("Attempt " + str(n) + " failed")


retry(create_user, 3)
retry(stop_service, 5)
