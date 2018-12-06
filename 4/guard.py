from operator import itemgetter


def get_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def sort_content(content):
    logs = []
    for log in content:
        time = log[:18].strip('[]')
        note = log[18:].strip()
        logs.append({'time': time, 'note': note})
    return sorted(logs, key=itemgetter('time'))


def get_parsed_content(sorted_content):
    guard_asleep = {}
    current_guard = ''
    asleep_start = None
    for log in content:
        (hour, minute) = (int(time)
                          for time in log['time'].split(' ')[1].split(':'))
        note = log['note']
        if '#' in note:
            current_guard = note.split('#')[1].split(' ')[0]
            if current_guard not in guard_asleep:
                guard_asleep[current_guard] = {}
        if 'fall' in note:
            asleep_start = {'hour': hour, 'minute': minute}
        if 'wake' in note and asleep_start:
            hour_diff = (hour - asleep_start['hour']) % 24
            min_diff = (minute - asleep_start['minute']) % 60
            for h in range(asleep_start['hour'], asleep_start['hour'] + hour_diff + 1):
                for m in range(asleep_start['minute'], asleep_start['minute'] + min_diff):
                    timestamp = str(h % 24) + '-' + str(m % 60)
                    if timestamp not in guard_asleep[current_guard]:
                        guard_asleep[current_guard][timestamp] = 0
                    guard_asleep[current_guard][timestamp] = guard_asleep[current_guard][timestamp] + 1
    return guard_asleep


def get_most_sleepy_checksum(parsed_content):
    max_total_sleep = 0
    most_sleepy_guard = ''
    for guard in parsed_content.keys():
        sleep = sum(parsed_content[guard].values())
        if max_total_sleep < sleep:
            max_total_sleep = sleep
            most_sleepy_guard = guard
    most_sleepy_minute = max(
        parsed_content[most_sleepy_guard].items(), key=itemgetter(1))[0]
    print("Guard", most_sleepy_guard, "Total sleep",
          max_total_sleep, "Sleepiest minute", most_sleepy_minute, "Checksum", (int(most_sleepy_guard) * int(most_sleepy_minute.split('-')[1])))


def get_most_frequent_checksum(parsed_content):
    most_frequent_total = 0
    most_sleepy_minute = ''
    most_sleepy_guard = ''
    for guard in parsed_content.keys():
        if not parsed_content[guard].items():
            break
        guards_most_sleepy_minute = max(
            parsed_content[guard].items(), key=itemgetter(1))[0]
        if parsed_content[guard][guards_most_sleepy_minute] > most_frequent_total:
            most_frequent_total = parsed_content[guard][guards_most_sleepy_minute]
            most_sleepy_minute = guards_most_sleepy_minute
            most_sleepy_guard = guard
    print("Guard", most_sleepy_guard, "Sleepiest minute", most_sleepy_minute, "Total sleep on most frequent minute",
          most_frequent_total, "Checksum", (int(most_sleepy_guard) * int(most_sleepy_minute.split('-')[1])))


content = get_content('input.txt')
content = sort_content(content)
content = get_parsed_content(content)
get_most_sleepy_checksum(content)
get_most_frequent_checksum(content)
