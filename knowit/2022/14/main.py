total_packages = 1_000_000
total_distance = 100_000_000 # meter
stage_distance = 1_000_000 # meter
packages_per_stage = 10_000 # meter
package_weight = 100 # gram
total_package_weight = 100 * total_packages
santa_weight = 100_000
sled_weight = 900_000
reindeer_weight = 100_000
weight = total_package_weight + santa_weight + sled_weight


def next_stage():
    return weight - package_weight * packages_per_stage


for stage in range(101):
    weight = next_stage()
    print(weight)