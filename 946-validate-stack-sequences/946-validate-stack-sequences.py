class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        st = []
        
        for pop in popped:
            if pop in pushed:
                index = pushed.index(pop)
                for val in pushed[:index+1]:
                    st.append(val)
                print(st)
                st.pop()
                pushed = pushed[index+1:]
            else:
                print(pop,st)
                if len(st) and st[-1] == pop:
                    st.pop()
                else:
                    return False
        return True