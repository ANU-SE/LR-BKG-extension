from bug_tossing.utils.file_util import FileUtil
from bug_tossing.utils.path_util import PathUtil
from sklearn.metrics import davies_bouldin_score


if __name__ == "__main__":
    train_bugs = FileUtil.load_pickle(PathUtil.get_train_bugs_filepath())
    pc_list = FileUtil.load_pickle(PathUtil.get_pc_filepath())
    pc_index_dict = dict()
    for index, pc in enumerate(pc_list):
        pc_index_dict[pc] = pc_index_dict.get(pc, index)
    bug_info_list = []
    labels = []
    for bug in train_bugs:
        bug_info_list.append(bug.summary_tfidf_vec)
        labels.append(pc_index_dict[bug.product_component_pair])
    dbi_score = davies_bouldin_score(bug_info_list, labels)
    print(dbi_score)