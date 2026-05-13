class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> h;
        int diff;

        for (int i = 0; i < nums.size(); i++) {
            diff = target - nums[i];
            if (h.count(diff) && h[diff] != i) {
                return {h[diff], i};
            } else {
                h[nums[i]] = i;
            }
        }

        return {};
    }
};
