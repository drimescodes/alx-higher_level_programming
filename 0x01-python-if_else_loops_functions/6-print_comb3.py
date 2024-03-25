#!/usr/bin/python3
print(
    ", ".join(
        [
            ", ".join([str(i) + str(j) for j in range(i + 1, 10)])
            for i in range(0, 10)
        ]
    )
    .rstrip(", ")
    .format("")  # NOTE: had to use '.format("")', project requirement :)
)
