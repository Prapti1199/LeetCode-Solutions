class Solution {
    public int minEatingSpeed(int[] piles, int h) {

        int low = 0;
        int high = piles[0]; // Assume first element is max
        int ans = 0;

        for (int i = 1; i < piles.length; i++) {
            if (piles[i] > high) {
                high = piles[i];
            }
        }

        while (low <= high) {
            int mid = (low + high) / 2;
            int k = 0;

            for (int i = 0; i < piles.length; i++) {
                k += Math.ceil((double) piles[i] / mid);
            }

            if (k <= h) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;

    }
}