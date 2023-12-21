class FrequencyTracker:
    def __init__(self):
        # Initialize an empty array to store numbers
        self.data = {}
        self.freq_dict = {}

    def add(self, number):
        if number not in self.data:
            self.data[number] = 0
        self.data[number] += 1

        if self.data[number] > 1:
            self.freq_dict[self.data[number] - 1] -= 1
        if self.data[number] not in self.freq_dict:
            self.freq_dict[self.data[number]] = 1
        else:
            self.freq_dict[self.data[number]] += 1

    def deleteOne(self, number):
        if number in self.data and self.data[number] > 0:
            self.freq_dict[self.data[number]] -= 1
            self.data[number] -= 1
            if self.data[number] > 0:
                self.freq_dict[self.data[number]] += 1

    def hasFrequency(self, frequency):
        return frequency in self.freq_dict and self.freq_dict[frequency] > 0

            
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)