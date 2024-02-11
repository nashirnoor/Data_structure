class CharacterFrequencyCounter:
    def __init__(self):
        self.frequency_table = {}

    def count_frequency(self, string):
        for char in string:
            if char in self.frequency_table:
                self.frequency_table[char] += 1
            else:
                self.frequency_table[char] = 1

    def display_frequency(self):
        for char, frequency in self.frequency_table.items():
            print(f"Character '{char}' occurs {frequency} times.")

string = "hello world"
counter = CharacterFrequencyCounter()
counter.count_frequency(string)
counter.display_frequency()
