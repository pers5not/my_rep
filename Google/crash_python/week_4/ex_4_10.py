# Функция email_list получает словарь, который содержит имена доменов в качестве ключей и список пользователей в качестве значений. Заполните пустые поля, чтобы создать список, содержащий полные адреса электронной почты (например, diana.prince@gmail.com).
def email_list(domains):
    emails = []
    for domain in domains:
        for user in domains[domain]:
            emails.append(user + '@' + domain)
    return(emails)


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
      "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
