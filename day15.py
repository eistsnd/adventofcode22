import re
from point import Point, Range, trim_ranges, union_of_ranges


def process_line(text):
    result = [int(d) for d in re.findall(r'-?\d+', text)]

    sensor = Point(result[0], result[1])
    beacon = Point(result[2], result[3])
    return {
        'sensor': sensor,
        'beacon': beacon,
        'dist': abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
    }


def sensor_coverage_at(sensor, dist, y):
    lr_span = dist - abs(sensor.y - y)
    if 0 <= lr_span:
        return Range(sensor.x - lr_span, sensor.x + lr_span)


if __name__ == '__main__':
    with open('day15_input.txt') as file:
        sabs = [process_line(line) for line in file]

    y = 2000000
    beacons_at_y = len(set([sab['beacon'] for sab in sabs if sab['beacon'].y == y]))

    coverages = union_of_ranges(
        list(
            filter(
                lambda item: item is not None,
                (sensor_coverage_at(sab['sensor'], sab['dist'], y) for sab in sabs)
            )
        )
    )

    total_coverage = sum([coverage.end-coverage.start for coverage in coverages])

    # 4737442
    print(total_coverage - beacons_at_y)

    # part 2
    distress = None
    for y in range(0, 4000001):
        coverages = union_of_ranges(
            list(
                filter(
                    lambda item: item is not None,
                    (sensor_coverage_at(sab['sensor'], sab['dist'], y) for sab in sabs)
                )
            )
        )

        trim_ranges(coverages, Range(0, 4000000))

        # kurva nagy faszom lenne ha megirtam volna az intersectiont es akkor 0,4000000-al intersect
        # es akkor osszegyujtene h mik nincsenek lefedve es azokat osszedni... nyiiilvan
        if coverages[0].end - coverages[0].start < 4000000:
            if len(coverages) == 2:
                distress = Point(coverages[0].end+1, y)
            elif coverages[0].start != 0:
                distress = Point(0, y)
            else:
                distress = Point(4000000, y)
            break

    frequency = distress.x * 4000000 + distress.y

    # 11482462818989
    print(frequency)

