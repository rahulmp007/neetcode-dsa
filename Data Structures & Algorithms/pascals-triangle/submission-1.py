class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result : int = []

        for i in range(numRows):
            current_row = [1] * (i+1)

            for j in range(1,i):
                current_row[j] = result[i-1][j-1] + result[i-1][j]
            
            result.append(current_row)
            
        return result

        