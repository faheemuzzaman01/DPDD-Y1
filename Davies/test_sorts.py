import fn

test_list = [34, 1, 12, 8, 96, 4, 39, 3, 43, 35]
test_list = fn.sorts.bubble(test_list)
fn.printy(f"bubble: {test_list}")

test_list = [34, 1, 12, 8, 96, 4, 39, 3, 43, 35]
test_list = fn.sorts.insertion(test_list)
fn.printy(f"insertion: {test_list}")

test_list = [34, 1, 12, 8, 96, 4, 39, 3, 43, 35]
test_list = fn.merge(test_list)
fn.printy(f"merge: {test_list}")