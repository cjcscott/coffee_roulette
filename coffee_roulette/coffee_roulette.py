"""Main module."""

import numpy as np


class CoffeeGenerator:
    def __init__(self, namelist, min_allowed=2, max_allowed = 4):

        self.namelist = namelist
        self.nentries = len(namelist)
        self.min = min_allowed
        self.max = max_allowed
        # If we have no wiggle room why are you asking?
        assert(self.min < self.max)
        assert(self.min < self.nentries and self.max < self.nentries)
        if not self.min > 1:
            print("Warning: could end up with people on their own...")

    def run(self, partitioning = "input"):
        # First, determine the number of groups and their sizes.
        split = self.decide_partitioning(partitioning)
        # Now randomly shuffle the namelist.
        order = np.copy(self.namelist)
        np.random.shuffle(order)
        # Then go through in this random order and split into appropriate groups to give final result.
        ndone = 0
        res = []
        for i,v in split.items():
            for j in range(v):
                res += [order[ndone:ndone+i]]
                ndone += i
        return res

    def decide_partitioning(self, partitioning):
        if type(partitioning) == dict:
            return partitioning

        if partitioning == "max":
            # Want to maximise the size of all groups, within the maximum constraint provided.
            # The number of groups must be greater than this.
            ngroups = int(np.ceil(self.nentries / self.max))
            min_per_group = self.nentries // ngroups
            if min_per_group < self.min:
                print("Too few people to effectively use max algorithm; results may be suboptimal.")
            deviation = self.nentries - min_per_group * ngroups
            partition = {
                    min_per_group:ngroups - deviation,
                    min_per_group+1:deviation
                }
            return partition
        elif partitioning == "min":
            # Want to minimise the size of all groups, within the minimum constraint provided.
            # The number of groups must be less than this.
            ngroups = self.nentries // self.min
            max_per_group = int(np.ceil(self.nentries / ngroups))
            if max_per_group > self.max:
                print("Too few people to effectively use min algorithm; results may be suboptimal.")
            deviation = max_per_group * ngroups - self.nentries
            partition = {
                    max_per_group:ngroups - deviation,
                    max_per_group-1:deviation
                }
            return partition

        elif partitioning in ["random", "input"]:
            # Need to generate all possible partitionings, then either choose randomly or via user input.
            partitions = self.gen_partitions()
            
            if partitioning == "random":
                return partitions[np.randdom.randint(self.nentries)]
            else:
                print("Possible partitionings:")
                for i in range(len(partitions)):
                    print(i, partitions[i])
                while True:
                    count = 0
                    try:
                        choice = int(input("Please select desired partitioning number:\n"))
                        if choice < 0 or not (choice<len(partitions)):
                            raise ValueError("Provided value is outside of range of allowed values.")
                    except Exception as e:
                        if count < 5:
                            print("I didn't understand that; please try again, entering an appropriate integer.")
                        else:
                            raise e
                        count += 1
                    else:
                        break

                return partitions[choice]
        else:
            raise valueError("Unknown partitioning scheme requested.")


    def gen_partitions(self):
        """
        """
        pass

        

