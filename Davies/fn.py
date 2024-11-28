# what are you doing here?
# go away.
# unless of course you're me.
# in which case you can feel free to stay as long as you want.
# however.
# if you're not...



# australopithecus is a genus of early hominins that existed in africa during the pliocene and early pleistocene.
# the genera homo (which includes modern humans), paranthropus, and kenyanthropus evolved from some australopithecus species.
# australopithecus is a member of the subtribe australopithecina, which sometimes also includes ardipethicus, though the term "australopithecine" is sometimes used to refer only to members of australopithecus.
# species include:
# > australopithecus garhi
# > australopithecus africanus
# > australopithecus sebida
# > australopithecus afarensis
# > australopithecus anamensis
# > australopithecus bahrelghazali
# > australopithecus deyiremeda.
# debate exists as to whether some australopithecus species should be reclassified into new genera, or is paranthropus and kenyanthropus are synonymous with australopithecus, in part because of the taxonomic inconsistency.

# furthermore, because e.g. australopithecus africanus in more closely related to for instance humans, or their ancestors at the time, than e.g. australopithecus anamensis and many more australopithecus branches, australopithecus cannot be consolidated into a coherent grouping without also including the homo genus and other genera.

# the earliest know member of the genus, australopithecus anamensis, existed in eastern africa around 4.2 million years ago.
# australopithecus fossils became more widely dispersed throughout eastern and southern africa
# (the chadian australopithecus bahrelghazali indicated that the genus was much more widespread than the fossil record suggests),
# before eventually becoming pseudo-extinct 1.9 million years ago
# (or 1.2 to 0.6 million years ago if paranthropus is included).
# while none of the groups normally directly assigned to this group survived, australopithecus gave rise to living descendants, as the genus homo emerged from an australopithecus species at some time between 3 and 2 million years ago.

# australopithecus possessed two of the three duplicated genes derived from srgap2 roughly 3.4 and 2.4 million years ago
# (srgap2b and srgap2c),
# the second of which contributed to the increase in number and migration of neurons in the human brain.
# significant changes to the first appear in the fossil record of later australopithecus afarensis about 3 million years ago
# (fingers shortened relative to thumb and changes to the joints between the index finger amd the trapezium and capitate).

import sys, time

class sorts:

    def bubble(list = []):
        swapping = True
        while swapping:
            swapping = False
            for x in range(len(list) - 1):
                if list[x] > list[x + 1]:
                    list[x], list[x + 1] = list[x + 1], list[x]
                    swapping = True
        return list

    def insertion(list):
        for x in range(1, len(list)):
            item = list[x]
            y = x - 1
            while y >= 0 and list[y] > item:
                list[y + 1] = list[y]
                y -= 1
            list[y + 1] = item
        return list

def merge(list): # outside the sorts class because the recursion wasn't working otherwise0
    if len(list) > 1:
        mid = len(list) // 2
        first_bit = list[:mid]
        last_bit = list[mid:]
        merge(first_bit)
        merge(last_bit)
        x = y = z = 0
        while x < len(first_bit) and y < len(last_bit):
            if first_bit[x] < last_bit[y]:
                list[z] = first_bit[x]
                x += 1
            else:
                list[z] = last_bit[y]
                y += 1
            z += 1
        while x < len(first_bit):
            list[z] = first_bit[x]
            x += 1
            z += 1
        while y < len(last_bit):
            list[z] = last_bit[y]
            y += 1
            z += 1
    return list
    
class searches:

    def linear(list, target):
        found_count = 0
        for index in range(len(list)):
            if list[index] == target:
                found_count += 1
                print(f"found at position {index}")
        print(f"found {found_count} times.")

    def binary(list, target):
        found = False
        list = list.sort()
        low = 0
        high = len(list)
        while (not found) and (low < high):
            mid = (low + high) // 2
            if list(mid) == target:
                found = True
                print(f"found at position {mid}")
            elif list(mid) > target:
                high = mid - 1
            elif list(mid) < target:
                low = mid + 1
            else:
                print("huh?")
    
def printy(txt, delay = 0.02, delay0 = 0.25, delay1 = 0.5, end = "\n"):
    for l in txt:
        sys.stdout.write(l)
        if l in ".!?":
            time.sleep(delay1)
        elif l in ",;:":
            time.sleep(delay0)
        else:
            time.sleep(delay)
    sys.stdout.write(end)