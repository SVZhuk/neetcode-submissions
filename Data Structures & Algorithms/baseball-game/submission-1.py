class Solution:
    def calPoints(self, operations: List[str]) -> int:
        self.record = []
        for elem in operations:
            if elem not in ["+", "D", "C"]:
                self.record.append(int(elem))
            if elem == "+":
                self.record.append(self.record[-2] + self.record[-1])
            if elem == "D":
                self.record.append(self.record[-1] * 2)
            if elem == "C":
                self.record.pop()

        return sum(self.record)
        