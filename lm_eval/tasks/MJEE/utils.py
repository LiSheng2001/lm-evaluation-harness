import datasets
import re
import random

question_pattern = r"(.*?)\n([A-E]\. .*(?:\n[A-E]\. .*)*)"
options_pattern = r"[A-E]\. .*?(?=\n[A-E]\. |\Z)"

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        # 可以做一些简单的后处理
        # 但这里不需要，因此直接返回
        return doc
    
    def _filter_doc(doc):
        if "#need_image" in doc["Question"]:
            # 这边对需要图像的示例置None进行过滤
            return False
        return True

    dataset = dataset.map(_process_doc)
    dataset = dataset.filter(_filter_doc)
    return dataset


def process_docs_shuffle(dataset: datasets.Dataset) -> datasets.Dataset:
    # 在原来的基础上，打乱选项排列以减少记忆题目带来的增益
    def _filter_doc(doc):
        if "#need_image" in doc["Question"]:
            # 这边对需要图像的示例置None进行过滤
            return False
        return True

    def _process_doc(doc):
        # 打乱选项
        # 先分离问题和选项
        match = re.match(question_pattern, doc["Question"], re.DOTALL)
        old_question, old_answer = doc["Question"], doc["Answer"]

        if match:
            # 一般正常选项都可以走这个分支
            question_body = match.group(1).strip()
            options = match.group(2).strip()

            # 将选项拆分为列表
            options_list = re.findall(options_pattern, options, re.DOTALL)
            # 打乱选项
            random.shuffle(options_list)

            # 组合为新问题
            for i, option in enumerate(options_list, start=1):
                question_body += f"\n{chr(64 + i)}. {option[3:]}"
                # 处理正确选项的变更
                if option[0] == doc["Answer"]:
                    new_answer = f"{chr(64 + i)}"
            
            doc["Question"] = question_body
            doc["Answer"] = new_answer

        return doc
    
    
    dataset = dataset.filter(_filter_doc)
    dataset = dataset.map(_process_doc)
    return dataset