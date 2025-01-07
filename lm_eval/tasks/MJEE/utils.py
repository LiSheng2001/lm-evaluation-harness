import datasets

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