class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num  in nums:
            counter[num] = counter.get(num, 0) + 1
        
        dict_counter = {}
        for num, freq in counter.items():
            if freq not in dict_counter:
                dict_counter[freq] = []
            dict_counter[freq].append(num)
        
        list_counter = list(dict_counter.keys())
        list_counter = sorted(list_counter, reverse=True)

        append_values = []
        for count in list_counter:
            values = dict_counter[count]
            if len(values) == k:
                append_values.extend(values)
                return append_values
            elif len(values) > k:
                append_values.extend(values[:k])
                return append_values
            else:
                append_values.extend(values)
                k -= len(values)
        return append_values