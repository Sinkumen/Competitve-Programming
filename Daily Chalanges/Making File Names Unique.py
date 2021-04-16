class Solution:
    def getFolderNames(self, names):
        created = {}
        res = []
        for name in names:
            if name in created:
                cur = created[name]
                while f"{name}({cur})" in created:
                    cur += 1
                res.append(f"{name}({cur})")
                created[name] = cur+1
                created[f"{name}({cur})"] = 1
            else:
                created[name] = 1
                res.append(name)
        return res
