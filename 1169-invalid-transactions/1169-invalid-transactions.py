class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [tr.split(",") for tr in transactions]
        transactions.sort(key = lambda x: (x[0],int(x[1])))
        occ = defaultdict(list)
        ans = set()
        # print(transactions)
        for i in range(len(transactions)):
            name,time,amount,city = transactions[i]
            if int(amount) > 1000:
                ans.add(i)
                
            if name not in occ:
                occ[name].append((i,time,city))                
            else:
                for idx,ptime,pcity in occ[name]:
                    diff  = int(time) - int(ptime)
                    if diff <= 60 and city != pcity:
                        ans.add(i)
                        ans.add(idx)
                occ[name].append((i,time,city))   

                        
        return [",".join(transactions[i]) for i in ans]
            
            
        