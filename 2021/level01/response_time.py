# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/tempo/


n = int(input())
contacts = []
events = []
result = {}
e_used = []


def get_e(i_r):
    list_events = events[i_r:]
    list_contacts = contacts[i_r:]
    for i in range(len(list_events)):
        if (list_events[i] != 'E') | (
            len(e_used) != 0 and list_events[i] not in e_used
        ):
            if list_events[i] != 'T':
                result[list_contacts[i]] = result.get(list_contacts[i], 0) + 1
            else:
                for k, _ in result.items():
                    result[k] += list_contacts[i]

        elif list_contacts[i] != list_contacts[0]:
            print('caiu')
        else:
            e_used.append(i)
            return i


if n >= 1 and n <= 20:
    for i in range(n):
        r, p = input().split()
        events.append(r)
        contacts.append(int(p))

    for i in range(len(events)):
        if events[i] == 'R':
            get_e(i)
    print(result)
