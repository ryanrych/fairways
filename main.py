import requests


def get_course_id_pairs():
    """
    Get all courses and their ids
    :return: dict pairing course names to their id
    """
    response = requests.get("https://fairways-api-ryanrychlak.koyeb.app/courses")

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Couldn't retrieve data. Error code {response.status_code}")


def get_course_data_by_id(course_id):
    """
    View all data of a specific course
    :param course_id: id of course
    :return: dict containing basic data of the course as well as hole information for all of the holes
    """
    response = requests.get(f"https://fairways-api-ryanrychlak.koyeb.app/courses/{course_id}")

    if response.status_code == 200:
        course_data = response.json()
        response = requests.get(f"https://fairways-api-ryanrychlak.koyeb.app/courses/{course_id}/holes")

        if response.status_code == 200:
            course_data["holes"] = response.json()

            return course_data
        else:
            raise Exception(f"Couldn't retrieve data. Error code {response.status_code}")
    else:
        raise Exception(f"Couldn't retrieve data. Error code {response.status_code}")


id_pairs = get_course_id_pairs()

print(get_course_data_by_id(69))
