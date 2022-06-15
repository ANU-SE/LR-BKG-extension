from pathlib import Path
from config import DATA_DIR
from bug_tossing.types.bugs import Bugs
from bug_tossing.utils.file_util import FileUtil
from bug_tossing.utils.path_util import PathUtil


if __name__ == "__main__":
    """
    sort bugs by creation time
    and split bugs into training set and testing set by different ways
    80% training dataset
    20% testing dataset
    """
    bugs = FileUtil.load_pickle(Path(DATA_DIR, "filtered_eclipse_bugs_pc50.json"))
    # print("ok")
    train_bugs_filepath = PathUtil.get_train_bugs_filepath()
    train_bugs = FileUtil.load_pickle(train_bugs_filepath)
    test_bugs_filepath = PathUtil.get_test_bugs_filepath()
    test_bugs = FileUtil.load_pickle(test_bugs_filepath)

    train_pcs = set()
    for train_bug in train_bugs:
        train_pcs.add(train_bug.product_component_pair)
    test_pcs = set()
    for test_bug in test_bugs:
        test_pcs.add(test_bug.product_component_pair)
    print(len(train_pcs))
    print(len(test_pcs))

    pcs = train_pcs.intersection(test_pcs)
    print(len(pcs))
    
    filtered_bugs = []
    for bug in bugs:
        if bug.product_component_pair in pcs:
            # print('OK')
            filtered_bugs.append(bug)
    print(len(bugs.bugs))
    print(len(filtered_bugs))
    print(len(bugs.bugs) - len(filtered_bugs)) 
    filtered_bugs_filepath = PathUtil.get_filtered_eclipse_bugs_filepath()
    FileUtil.dump_pickle(PathUtil.get_filtered_eclipse_bugs_filepath(), Bugs(filtered_bugs))

