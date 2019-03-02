class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        all_rows = [[1]]
        
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:   
            for i in range(2,numRows+1):
                new_row = [1]
                for j in range(len(all_rows[-1])-1):
                    new_row.append(all_rows[-1][j] + all_rows[-1][j+1])
                new_row.append(1)
                all_rows.append(new_row[:])
        return all_rows
