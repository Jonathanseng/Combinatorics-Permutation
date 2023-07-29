def pigeonhole_principle_3(n, k, min_value, max_value):
    if n <= k:
        return "All pigeons can have their own hole"
    else:
        if min_value > max_value:
            raise ValueError(
                "min_value must be less than or equal to max_value. min_value = {} and max_value = {}".format(
                    min_value, max_value
                )
            )
        return (
            "At least two pigeons must share a hole with a value between {} and {}".format(
                min_value, max_value
            )
        )


def main():
    print(pigeonhole_principle_3(3, 2, 1, 3))
    print(pigeonhole_principle_3(3, 3, 1, 3))


if __name__ == "__main__":
    main()
