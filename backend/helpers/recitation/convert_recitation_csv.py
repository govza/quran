'''Convert recitername.csv to django fixtures file'''
import json
from os import path
import csv
from collections import defaultdict
import ast


def structure_recitation_dict(data):
    '''Parse raw csv data and build structured dict'''
    recitation_dict = defaultdict(lambda: defaultdict(list))
    for surah, ayah, segments in data:
        #  convert string representation to list
        segments_list = ast.literal_eval(segments)
        #  remove unused elements, set start:end, ...] formatted list
        segments_sliced_list = list(
            [f'{segment[2]}:{segment[3]}' for segment in segments_list])
        segments_sliced_string = ','.join(segments_sliced_list)
        recitation_dict[surah][ayah].append(segments_sliced_string)
    return recitation_dict


def structure_recitation_json(recitation_dict, reciter_id):
    '''Form import ready recitation list json from structured dict'''
    list_of_recitation_ayahs = []
    for surah, ayahs in recitation_dict.items():
        for ayah, segments in ayahs.items():
            element = {
                "model": "recite.Recitation",
                "fields": {
                    "reciter": reciter_id,
                    "surah": surah,
                    "ayah": ayah,
                    "segments": ",".join(segments)
                }
            }
            list_of_recitation_ayahs.append(element)
    return list_of_recitation_ayahs


def get_reciters():
    with open('reciters.json', encoding='utf-8') as data_file:
        return json.load(data_file)


def write_reciters():
    reciters_dict = get_reciters()

    fixture_dir = path.abspath(
        path.join(path.dirname(__file__), '../../recite/fixtures'))
    fixture_filename = 'reciters_list.json'
    fixture_file = path.join(fixture_dir, fixture_filename)

    reciter_data = [
        {
            "model": "recite.Reciter",
            "fields": {
                "id": int(reciter['id']),
                "name": reciter['name'],
                "quality": reciter['quality'],
                "description": reciter['description'],
            }
        }
        for reciter in reciters_dict]

    with open(fixture_file, 'w') as fp:
        json.dump(reciter_data, fp, sort_keys=True, indent=4)


def write_recitations():
    reciters_dict = get_reciters()

    fixture_dir = path.abspath(
        path.join(path.dirname(__file__), '../../recite/fixtures/recitations'))

    for reciter in reciters_dict:
        recitation_csv_file = reciter["file"]
        reciter_id = reciter["id"]
        #  save fixture file as name of csv file with json extension
        fixture_file = path.join(
            fixture_dir,
            f'{path.splitext(recitation_csv_file)[0]}.json')
        data = []
        with open(recitation_csv_file, encoding='utf-8') as data_file:
            field_names = ("surah", "ayah", "segments")
            reader = csv.DictReader(data_file, field_names)
            for row in reader:
                data.append([
                    int(row.get("surah")),
                    int(row.get("ayah")),
                    row.get("segments")])

        recitation_dict = structure_recitation_dict(data)
        recitation_list = structure_recitation_json(
            recitation_dict, reciter_id)

        with open(fixture_file, 'w', encoding="utf8") as fp:
            json.dump(
                recitation_list, fp, sort_keys=True, indent=4,
                ensure_ascii=False)


def main():
    write_reciters()
    write_recitations()

if __name__ == "__main__":
    main()
