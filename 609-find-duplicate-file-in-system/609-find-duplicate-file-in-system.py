class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for path in paths:
            # print(path)
            files = path.split()
            for i in range(1,len(files)):
                file,content = files[i].split("(")
                mapping[content[:-1]].append(files[0]+"/"+file)
                
        return [val for val in mapping.values() if len(val) > 1]

            