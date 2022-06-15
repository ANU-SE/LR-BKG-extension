from bug_tossing.types.bugs import Bugs
from bug_tossing.utils.file_util import FileUtil
from bug_tossing.utils.path_util import PathUtil


if __name__ == "__main__":
    filtered_bugs_filepath = PathUtil.get_filtered_eclipse_bugs_filepath()
    bugs = FileUtil.load_pickle(filtered_bugs_filepath)

    pcs = set()
    for bug in bugs:
        pcs.add(bug.product_component_pair)
    for pc in pcs:
        print(pc.product+'::'+pc.component)
   
    # print(len(pcs))
