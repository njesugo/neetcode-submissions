class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        dict_counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
        for num, freq in counter.items():
            if freq not in dict_counter:
                dict_counter[freq] = []
            dict_counter[freq].append(num)

        list_count = sorted(list(dict_counter.keys()), reverse=True)
        
        app_dict_elt = []
        for count in list_count:
            dict_elt = dict_counter[count]
            if len(dict_elt) == k:
                app_dict_elt.extend(dict_elt)
                return app_dict_elt
            elif len(dict_elt) < k:
                app_dict_elt.extend(dict_elt)
                k -= len(dict_elt)
            else:
                app_dict_elt.extend(dict_elt[:k])
                return app_dict_elt
        return app_dict_elt