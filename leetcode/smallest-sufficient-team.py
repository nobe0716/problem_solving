from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_to_no = {req_skills[_]: 2 ** _ for _ in range(len(req_skills))}
        people_to_skill = []
        for person_skill in people:
            skills = 0
            for skill in person_skill:
                skills |= skill_to_no[skill]
            people_to_skill.append(skills)

        t = {0: []}
        for new_member, new_skill in enumerate(people_to_skill):
            for skill, members in list(t.items()):
                if (skill | new_skill) not in t or len(t[skill | new_skill]) > len(members) + 1:
                    t[skill | new_skill] = members + [new_member]
        return t[2 ** len(req_skills) - 1]


s = Solution()
assert s.smallestSufficientTeam(["java", "nodejs", "reactjs"], [["java"], ["nodejs"], ["nodejs", "reactjs"]]) == [0, 2]
