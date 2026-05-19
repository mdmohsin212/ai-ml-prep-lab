class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)

        rank_map = {val: i + 1 for i, val in enumerate(sorted_scores)}
        final_ranks = [rank_map[val] for val in score]

        for idx, rank in enumerate(final_ranks):
            if rank == 1:
                final_ranks[idx] = "Gold Medal"
            elif rank == 2:
                final_ranks[idx] = "Silver Medal"
            elif rank == 3:
                final_ranks[idx] = "Bronze Medal"
            else:
                final_ranks[idx] = str(rank)
                
        return final_ranks