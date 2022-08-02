def appearance(intervals: dict):
    start_lesson = intervals["lesson"][0]
    end_lesson = intervals["lesson"][1]
    tutors_time = intervals["tutor"]
    pupil_time = intervals["pupil"]
    shared_online_time = 0

    for x in range(0, len(tutors_time), 2):
        tutor_joined = tutors_time[x]
        tutor_disconnected = tutors_time[x + 1]
        print('TUTOR', tutor_joined, tutor_disconnected)

        if tutor_joined < start_lesson and tutor_disconnected < start_lesson:
            continue
        if tutor_joined > end_lesson and tutor_disconnected > end_lesson:
            continue
        if tutor_joined <= start_lesson <= tutor_disconnected:
            tutor_joined = start_lesson
        elif tutor_joined <= end_lesson <= tutor_disconnected:
            tutor_disconnected = end_lesson

        for p in range(0, len(pupil_time), 2):
            pupil_joined = pupil_time[p]
            pupil_disconnected = pupil_time[p + 1]
            print('pupil', pupil_joined, pupil_disconnected)

            if pupil_joined < tutor_joined and pupil_disconnected < tutor_joined:
                continue
            elif pupil_joined > tutor_disconnected and pupil_disconnected > tutor_disconnected:
                continue

            elif tutor_joined <= pupil_joined and pupil_disconnected <= tutor_disconnected:
                shared_online_time += pupil_disconnected - pupil_joined
                print(shared_online_time)
            elif tutor_joined <= pupil_joined and tutor_disconnected <= pupil_disconnected:
                shared_online_time += tutor_disconnected - pupil_joined
                print(shared_online_time)
            elif pupil_joined <= tutor_joined and pupil_disconnected <= tutor_disconnected:
                shared_online_time += pupil_disconnected - tutor_joined
                print(shared_online_time)
            elif pupil_joined <= tutor_joined and tutor_disconnected <= pupil_disconnected:
                shared_online_time += tutor_disconnected - tutor_joined
                print(shared_online_time)

    return shared_online_time


print(appearance({'lesson': [1594692000, 1594695600],
                  'pupil': [1594692033, 1594696347],
                  'tutor': [1594692017, 1594692066, 1594692068, 1594696341]}))
